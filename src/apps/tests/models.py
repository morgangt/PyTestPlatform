from django.db import models


class Tests(models.Model):
    name = models.CharField(max_length=256, verbose_name='Название теста')
    description = models.TextField(verbose_name='Описание теста')
    sum = models.SmallIntegerField(verbose_name='Количество вопросов в тесте', blank=True, null=True)

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.name


class Questions(models.Model):
    test = models.ForeignKey(Tests)
    title = models.CharField(max_length=256, verbose_name='Название вопроса')
    text = models.TextField(verbose_name='Текст вопроса')
    index = models.SmallIntegerField(verbose_name='Порядок вопроса', blank=True, null=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.test.name + ' ' + self.title


class Variant(models.Model):
    questions = models.ForeignKey(Questions)
    title = models.CharField(max_length=256, verbose_name='Текст варианта')
    correct = models.BooleanField(verbose_name='Коректный вариант или нет')

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'

    def __str__(self):
        return self.title
