from django.contrib import admin
from .models import *
# Register your models here.

class GoodInline(admin.TabularInline):
    model=Good
    extra=0

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields] #достает все поля автоматически и выводит в Django admin.
    #exlude = ["email"] с помощью этой записи можно исключить любое поле, а БД - это поле останентся, как и прежде.
    #fields = ["email"] противоположен методу exclude (данные не удалятся из БД)
    inlines = [GoodInline]
    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)

class GoodImageInline(admin.TabularInline):
    model = GoodImage
    extra = 0

class GoodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Good._meta.fields] #достает все поля автоматически и выводит в Django admin.
    #exlude = ["email"] с помощью этой записи можно исключить любое поле, а БД - это поле останентся, как и прежде.
    #fields = ["email"] противоположен методу exclude (данные не удалятся из БД)
    inlines = [GoodImageInline]
    class Meta:
        model = Good

admin.site.register(Good, GoodAdmin)


class GoodImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GoodImage._meta.fields] #достает все поля автоматически и выводит в Django admin.
    #exlude = ["email"] с помощью этой записи можно исключить любое поле, а БД - это поле останентся, как и прежде.
    #fields = ["email"] противоположен методу exclude (данные не удалятся из БД)
    class Meta:
        model = GoodImage

admin.site.register(GoodImage, GoodImageAdmin)
