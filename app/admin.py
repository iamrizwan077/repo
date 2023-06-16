from django.contrib import admin
from .models import *

# Register your models here.

# @admin.register(CustomUser)
# class CustomUserModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'username', 'email', 'role']

admin.site.register(CustomUser)
admin.site.register(Receptionist)
admin.site.register(Doctor)
admin.site.register(Nurse)
