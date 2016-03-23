from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import UserForm
from django.contrib.auth import login
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get(self, request):

        return self.render_to_response({
            'title': 'Test',
        })


def new_user(request):
    form = UserForm(request.POST)

    if form.is_valid():
        new_user = User.objects.create_user(**form.cleaned_data)
        login(new_user)

        return HttpResponseRedirect("/login/")

    else:
        return HttpResponseRedirect("/register/")


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/tests/")

    else:
        return HttpResponseRedirect("/login/")


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")


class LoginView(TemplateView):
    template_name = 'main/login.html'

    def get(self, request):
        form = UserForm()

        return self.render_to_response({
            'form': form,
            'title': 'Login',
        })


class RegView(TemplateView):
    template_name = 'main/reg.html'

    def get(self, request):
        form = UserForm()

        return self.render_to_response({
            'form': form,
            'title': 'Register',
        })
