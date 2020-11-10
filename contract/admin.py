from django.contrib import admin
from .models import *
# Register your models here.

class ProviderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Provider._meta.fields] #достает все поля автоматически и выводит в Django admin.
    #exlude = ["email"] с помощью этой записи можно исключить любое поле, а БД - это поле останентся, как и прежде.
    #fields = ["email"] противоположен методу exclude (данные не удалятся из БД)
    class Meta:
        model = Provider
admin.site.register(Provider, ProviderAdmin)

class ContractAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contract._meta.fields] #достает все поля автоматически и выводит в Django admin.
    #exlude = ["email"] с помощью этой записи можно исключить любое поле, а БД - это поле останентся, как и прежде.
    #fields = ["email"] противоположен методу exclude (данные не удалятся из БД)
    class Meta:
        model = Contract
admin.site.register(Contract, ContractAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Transaction._meta.fields]
    class Meta:
        model = Transaction
admin.site.register(Transaction, TransactionAdmin)

class MontageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Montage._meta.fields]
    class Meta:
        model = Montage
admin.site.register(Montage, MontageAdmin)
