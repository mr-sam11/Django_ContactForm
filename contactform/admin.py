from django.contrib import admin

from .models.form import Contactform


# Register your models here.

class AdminContactform(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']


admin.site.register(Contactform, AdminContactform)
