from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView, TemplateView
from django.views.generic.edit import CreateView
from contract.models import Contract, Provider
from good.models import Good, Order
from customer.models import Customer
from docxtpl import DocxTemplate
from django.contrib import messages
from io import BytesIO
from contract.forms import ContractForm, SearchContractForm
from customer.forms import CustomerForm
from django.db.models import Q
from datetime import datetime, timedelta
from django.views import generic
from django.utils.safestring import mark_safe
from .models import *
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook

# Create your views here.

class ContractList(ListView):
    model = Contract
    template_name = 'contract/contract_list.html'
    success_url = '/contract/'
    paginate_by = 5


    def get_context_data(self, **kwargs):
        context = super(ContractList, self).get_context_data(**kwargs)
        context['form'] = SearchContractForm()

        contract_list = []
        for contract in Contract.objects.all():
            contract.__setattr__('total_transaction', contract.get_total_transaction())
            contract.__setattr__('debt', contract.get_debt())
            contract_list.append(contract)
        context['contract_list'] = contract_list
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchContractForm(self.request.GET)
        if form.is_valid():
            information = form.cleaned_data['information']
            if information:
                queryset = queryset.filter(
                    Q(id__icontains=information)|
                    Q(order__id__icontains=information)|
                    Q(customer__last_name__icontains=information)|
                    Q(customer__first_name__icontains=information)|
                    Q(customer__patronymic__icontains=information)
                )
        return queryset


class ContractCreateView(CreateView):
    form_class = ContractForm
    template_name = 'contract/contract_form.html'
    success_url = '/contract/'


def docx(request,pk):
    contract = Contract.objects.get(id=pk)
    steam = BytesIO()
    doc = DocxTemplate("Contract/media/word//template_new.docx")
    contract.total_price = contract.get_total_price()
    context = {
                'contract':contract
              }
    doc.render(context)
    doc.save(steam)
    response = HttpResponse(steam.getvalue())
    response['Content-Disposition'] = 'attachment; filename=contract%s.docx' %str(contract.id)
    response['Content-Length'] = steam.tell()
    response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    return response

def excel(request):
    contract = Contract.objects.all()
    steam = BytesIO()
    wb = Workbook()
    ws = wb.active
    ws.title = 'Таблица контрактов'
    ws.append(['Номер договора',
            'Номер заказа',
            'ФИО Клиента',
            'ФИО Заказчика',
            'Тип договора',
            'Дата Создания договора'])
    for i in contract:
        ws.append([i.contract_number,
                 i.order.id,
                 i.customer.last_name,
                 i.provider.last_name,
                 i.type,
                 i.created
         ])
    wb.save(steam)
    response = HttpResponse(steam.getvalue())
    response['Content-Disposition'] = 'attachment; filename=table_of_contracts.xlsx'
    response['Content-Length'] = steam.tell()
    response['Content-Type'] = 'application/vnd.ms-excel'
    return response

def contract(request, pk):
    template_name = 'contract/contract_information.html'
    contract = Contract.objects.get(id=pk)
    goods = Good.objects.filter(order=contract.order.id)
    context = {
        'contract':contract,
        'goods': goods,
    }
    return render(request, 'contract/contract_information.html', context)



def index(request):
    return render(request,'base/home.html')
