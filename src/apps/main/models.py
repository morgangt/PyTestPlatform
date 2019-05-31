from apps.tests.models import *
from django.contrib.auth.models import User
from datetime import datetime


class UsersTests(models.Model):
    user = models.ForeignKey(User)
    test = models.ForeignKey(Tests)
    start_date = models.DateTimeField(verbose_name='Время начала теста', default=datetime.now())
    end_date = models.DateTimeField(verbose_name='Время окончания теста', blank=True, null=True)
    status = models.ForeignKey(Questions, blank=True, null=True, default=None, verbose_name='Статус')
    total = models.IntegerField(blank=True, null=True, verbose_name='Итог')

    class Meta:
        verbose_name = 'Тест пользователя'
        verbose_name_plural = 'Тесты пользователя'


class AnswerQuestions(models.Model):
    test = models.ForeignKey(UsersTests)
    variant = models.ForeignKey(Variant)

    class Meta:
        verbose_name = 'Ответ пользователя'
        verbose_name_plural = 'Ответы пользователя'
