"""pytest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from apps.main import views as main_views
from apps.tests import views as test_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', main_views.IndexView.as_view()),
    url(r'^login/$', main_views.LoginView.as_view()),
    url(r'^new-user/$', main_views.new_user),
    url(r'^sign-up/$', main_views.login),
    url(r'^register/$', main_views.RegView.as_view()),
    url(r'^logout/$', main_views.logout),

    url(r'^tests/$', test_views.TestListView.as_view()),
    url(r'^test/id(?P<test_id>[0-9])/$', test_views.TestingView.as_view()),
    url(r'^test/id(?P<test_id>[0-9])/step(?P<step>[0-9])/$', test_views.TestingView.as_view()),
    url(r'^total/id(?P<test_id>[0-9])/$', test_views.TotalView.as_view()),
]
