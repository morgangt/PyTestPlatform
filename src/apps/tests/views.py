from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.generic import TemplateView
from apps.main.models import UsersTests, AnswerQuestions
from datetime import datetime
from .models import *
import random


class TestListView(TemplateView):
    template_name = 'tests/test_list.html'

    def get(self, request):

        if request.user.is_authenticated():
            try:
                list_tests = Tests.objects.all()
            except Tests.DoesNotExist:
                list_tests = None

            return self.render_to_response({
                'title': 'List tests',
                'list_test': list_tests,
            })

        else:
            return HttpResponseRedirect("/login/")


class TestingView(TemplateView):
    template_name = 'tests/test.html'

    def get(self, request, test_id, step=1):

        if request.user.is_authenticated():
            """ Прверяем авторезацию  """
            try:
                """ Проверяем наличие запрашиваемого теста """
                test = Tests.objects.get(id=test_id)
            except Tests.DoesNotExist:
                return HttpResponseRedirect('/tests/')

        try:
            """ Не менять на get_or_create() """
            user_test = UsersTests.objects.get(user=request.user, test=test)
        except UsersTests.DoesNotExist:
            user_test = UsersTests(user=request.user, test=test)
            user_test.save()

        if request.GET.get('variant'):
            """ Если нам прислали ответ на вопрос """
            if test.sum == step and user_test.status == test:
                ## ToDo: Делаем запись в AnswerQuestions

                return HttpResponseRedirect('/total/' + test_id + '/')

            return HttpResponseRedirect('/test/id' + test_id + '/step' + step)

        else:
            """ Если у нас запросили вопрос """
            try:
                """ Достаем все вопросы к тесту """
                questions = Questions.objects.filter(id=test_id)
            except Questions.DoesNotExist:
                return HttpResponseRedirect('/tests/')

            try:
                """ Если все вопросы к тесту идут попорядку берем следующий """
                questions = questions.get(index=int(step))

                if not user_test.status:
                    """ Если пользователь начинал тест у него уже должн быть статус если нет, то мы пишем ему статус"""
                    user_test = UsersTests.objects.get(user=request.user, test=test)
                    user_test.status = questions
                    user_test.save()

            except questions.DoesNotExist:
                """ Если вопросы идут в разнобой """
                step = AnswerQuestions.objects.filter(test=user_test)

                random_step = random.sample(step, test.sum)

                questions = questions.get(index=random_step)

                if not user_test.status:
                    """ Если пользователь начинал тест у него уже должн быть статус если нет, то мы пишем ему статус"""
                    user_test = UsersTests.objects.get(user=request.user, test=test)
                    user_test.status = questions
                    user_test.seve()

            try:
                variant = Variant.objects.filter(questions=questions)
            except Variant.DoesNotExist:
                return HttpResponseRedirect('/tests/')

            if variant.filter(correct=True).count() > 1:
                input_type = 'checkbox'
            else:
                input_type = 'radio'

            return self.render_to_response({
                'title': test.name,
                'test': test,
                'type': input_type,
                'questions': questions,
                'variant': variant,
                'next_step': int(step) + 1,
            })


class TotalView(TemplateView):
    template_name = 'tests/total.html'

    def get(self, request, test_id):

        if request.user.is_authenticated():
            """ Прверяем авторезацию  """
            try:
                """ Проверяем наличие запрашиваемого теста """
                test = Tests.objects.get(id=test_id)
            except Tests.DoesNotExist:
                return HttpResponseRedirect('/tests/')

        total = UsersTests.objects.filter(user=request.user, test=test)

        bad = AnswerQuestions.objects.filter(test=test, variant__correct=True)
        good = AnswerQuestions.objects.filter(test=test, variant__correct=False)

        procent = test.sum / 100 * good.count()

        return self.render_to_response({
            'title': test.name,
            'test': test,
            'total': total,
            'procent': procent,
            'good': good,
            'bad': bad,
        })
