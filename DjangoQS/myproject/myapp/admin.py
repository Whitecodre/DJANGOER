from django.contrib import admin
from .models import *

# Register your models here.

class admin_real_model(admin.ModelAdmin):
    list_display = ("id","first_name","last_name","gender","age","department")

admin.site.register(real_model, admin_real_model)