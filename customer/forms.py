from django import forms
from customer.models import Customer

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
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'first_name_form'}),
            'last_name': forms.TextInput(attrs={'class':'last_name_form'}),
            'patronymic': forms.TextInput(attrs={'class':'patronymic_form'}),
            'gender':forms.Select(attrs={'class':'gender_form'}),
            'number':forms.TextInput(attrs={'class':'number_form'}),
            'bank_account':forms.TextInput(attrs={'class':'bank_account_form'}),
            'city':forms.TextInput(attrs={'class':'city_form'}),
            'mail_index':forms.TextInput(attrs={'class':'mail_index_form'}),
            'email':forms.EmailInput(attrs={'class':'email_form'}),
         }
