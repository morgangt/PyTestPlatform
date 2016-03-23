from django.contrib import admin
from  .models import UsersTests


class UsersTestsAdmin(admin.ModelAdmin):
    list_display = ('user', 'test', 'start_date', 'end_date', 'status', 'total')

admin.site.register(UsersTests, UsersTestsAdmin)