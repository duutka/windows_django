from django import forms
from django.forms import widgets
from good.models import Good, Order
from contract.models import Montage
from customer.models import Customer
from django.forms import ModelForm

class SearchOrderForm(forms.Form):
    information = forms.CharField(label="", widget=forms.TextInput(attrs={
     'placeholder': 'Поиск...',
     'class':'search_form'
     }),
      required=False
    )

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
        'first_name',
        'last_name',
        'patronymic',
        'gender',
        'number',
        'bank_account',
        'mail_index',
        'city',
        'email']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'gender':'Пол',
            'patronymic': 'Отчество',
            'number': 'Телефон',
            'bank_account': 'Банковский счет',
            'city': 'Город',
            'mail_index':'Индекс',
            'email': 'Почта'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Имя'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Фамилия'}),
            'patronymic': forms.TextInput(attrs={'class':'form-control','placeholder':'Отчество'}),
            'gender':forms.Select(attrs={'class':'form-control','placeholder':'Пол'}),
            'number':forms.TextInput(attrs={'class':'form-control','placeholder':'Номер телефона'}),
            'bank_account':forms.TextInput(attrs={'class':'form-control','placeholder':'Банковские данные'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'Город'}),
            'mail_index':forms.TextInput(attrs={'class':'form-control','placeholder':'Индекс'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
         }

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=[
        'customer',
        'payment',
        'file']

    widgets = {
    'customer': forms.Select(attrs={'class':'form-control','placeholder':'Клиент'}),
    'payment': forms.Select(attrs={'class':'form-control','placeholder':'Оплачено:'}),
    'file': forms.TextInput(attrs={'class':'form-control','placeholder':'Файл:'})
    }

class GoodForm(forms.ModelForm):
    class Meta:
        model=Good
        fields=[
        'order',
        'profile',
        'fittings',
        'type_of_product',
        'filling',
        'image',
        'seal_color',
        'micro_ventilation',
        'decor_color',
        'handle_color',
        'toning',
        'product_color',
        'time_of_production',
        'number_of',
        'square',
        'price_per_item',
        'sale',
        'status'
        ]
        labels={
            'order': 'Заказ',
            'profile': 'Профиль',
            'fittings': 'Фурнитура',
            'type_of_product': 'Тип продукта',
            'filling': 'Заполнение',
            'seal_color': 'Цвет уплотнения',
            'micro_ventilation': 'Микропроветривание',
            'decor_color': 'Цвет декора',
            'handle_color': 'Цвет ручки',
            'toning': 'Тонировка',
            'product_color': 'Цвет изделия',
            'time_of_production': 'Время изготовления',
            'number_of': 'Количество',
            'square': 'Площадь',
            'price_per_item': 'Цена за 1шт.',
            'sale': 'Скидка',
            'status':'Статус',
            }

        widgets = {
            'order': forms.Select(attrs={'class':'form-control','placeholder':'Заказ'}),
            'profile': forms.Select(attrs={'class':'form-control','placeholder':'Профиль'}),
            'fittings': forms.TextInput(attrs={'class':'form-control','placeholder':'Фурнитура'}),
            'type_of_product': forms.TextInput(attrs={'class':'form-control','placeholder':'Вид изделия'}),
            'filling':forms.TextInput(attrs={'class':'form-control','placeholder':'Заполнение'}),
            'seal_color':forms.Select(attrs={'class':'form-control','placeholder':'Цвет уплотнения'}),
            'micro_ventilation':forms.Select(attrs={'class':'form-control','placeholder':'Микропроветривание'}),
            'decor_color':forms.Select(attrs={'class':'form-control','placeholder':'Цвет декорации'}),
            'handle_color':forms.Select(attrs={'class':'form-control','placeholder':'Цвет ручки'}),
            'toning':forms.Select(attrs={'class':'form-control','placeholder':'Тонировка'}),
            'product_color':forms.Select(attrs={'class':'form-control','placeholder':'Цвет изделия'}),
            'time_of_production':forms.TextInput(attrs={'class':'form-control','placeholder':'Время изготовления'}),
            'number_of':forms.TextInput(attrs={'class':'form-control','placeholder':'Количество'}),
            'square':forms.TextInput(attrs={'class':'form-control','placeholder':'Площадь'}),
            'price_per_item':forms.TextInput(attrs={'class':'form-control','placeholder':'Цена за 1 шт.'}),
            'sale':forms.TextInput(attrs={'class':'form-control','placeholder':'Скидка'}),
            'status': forms.Select(attrs={'class':'form-control','placeholder':'Статус'}),
         }

class MontageForm(forms.ModelForm):
    class Meta:
        model = Montage
        fields = [
        'date',
        'address',
        'customer',
        'description']

        labels = {
            'date': 'Дата',
            'address': 'Адрес',
            'customer': 'Клиент',
            'description': 'Описание',
            }

        widgets = {
            'date': forms.TextInput(attrs={'class':'form-control','placeholder':'Дата'}),
            'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Адрес'}),
            'customer': forms.Select(attrs={'class':'form-control','placeholder':'Клиент'}),
            'description': forms.TextInput(attrs={'class':'form-control','placeholder':'Описание'}),
    }
# class OrderForm(ModelForm):
#     class Meta:
#         model=Good
