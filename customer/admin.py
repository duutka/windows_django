from django.contrib import admin
from .models import *
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Customer._meta.fields] #достает все поля автоматически и выводит в Django admin.
    #exlude = ["email"] с помощью этой записи можно исключить любое поле, а БД - это поле останентся, как и прежде.
    #fields = ["email"] противоположен методу exclude (данные не удалятся из БД)
    class Meta:
        model = Customer
admin.site.register(Customer, CustomerAdmin)
