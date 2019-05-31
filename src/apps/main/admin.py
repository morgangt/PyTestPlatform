from django.contrib import admin
from .models import UsersTests
from .forms import AddTestForm, AddAnswerForm, AddQuestionsForm


class UsersTestsAdmin(admin.ModelAdmin):
    list_display = ('user', 'test', 'start_date', 'end_date', 'status', 'total')

admin.site.register(UsersTests, UsersTestsAdmin)
