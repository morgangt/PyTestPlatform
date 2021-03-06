# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-21 00:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название вопроса')),
                ('text', models.TextField(verbose_name='Текст вопроса')),
                ('index', models.SmallIntegerField(blank=True, null=True, verbose_name='Порядок вопроса')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Название теста')),
                ('description', models.TextField(verbose_name='Описание теста')),
                ('sum', models.SmallIntegerField(blank=True, null=True, verbose_name='Количество вопросов в тесте')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Текст варианта')),
                ('correct', models.BooleanField(verbose_name='Коректный вариант или нет')),
                ('questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Questions')),
            ],
            options={
                'verbose_name': 'Вариант',
                'verbose_name_plural': 'Варианты',
            },
        ),
        migrations.AddField(
            model_name='questions',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.Tests'),
        ),
    ]
