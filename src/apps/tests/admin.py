from django.contrib import admin
from .models import Tests, Questions, Variant


class TestsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'sum')


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('test', 'title', 'text', 'index')


class VariantAdmin(admin.ModelAdmin):
    list_display = ('questions', 'title', 'correct')


admin.site.register(Tests, TestsAdmin)
admin.site.register(Questions, QuestionsAdmin)
admin.site.register(Variant, VariantAdmin)