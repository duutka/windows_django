from django import forms
from django.forms import widgets
from contract.models import Contract, Transaction

class SearchContractForm(forms.Form):
    information = forms.CharField(label="", widget=forms.TextInput(attrs={
     'placeholder': 'Поиск...',
     'class':'search_form'
     }),
      required=False
    )


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['contract_number','order', 'avance', 'garanty', 'provider','type','date_provider']
        widgets = {
            'contract_number': forms.TextInput(attrs={'class':'contract_number_form'}),
            'order': forms.Select(attrs={'class':'order_form'}),
            'avance': forms.TextInput(attrs={'class':'avance_form'}),
            'garanty': forms.TextInput(attrs={'class':'garanty_form'}),
            'provider': forms.Select(attrs={'class':'provider_form'}),
            'type': forms.Select(attrs={'class':'type_form'}),
            'date_provider': forms.DateTimeInput(attrs={'class':'date_provider_form', 'data-target':'#datetimepicker1'})
             }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
