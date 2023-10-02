from django.contrib import admin
from .models import practice, customer_data, apis


# Register your models here.

class register_practice(admin.ModelAdmin):
    list_display = ('Name', 'Age')

admin.site.register(practice,register_practice)

class admin_customer_data(admin.ModelAdmin):
    list_display = ('Firstname', 'Lastname', 'Email_Address', 'Phone_Number', 'Age', 'DOB', 'Nationality', 'State_Of_Origin')

admin.site.register(customer_data,admin_customer_data)

class admin_api(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Department')

admin.site.register(apis,admin_api)