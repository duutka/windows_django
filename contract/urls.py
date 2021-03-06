from django.contrib import admin
from django.urls import re_path, path, include
from django.conf import settings
from contract.views import ContractList, ContractCreateView
from . import views

urlpatterns = [
    path('', ContractList.as_view()),
    re_path(r'^(?P<pk>\d+)/word', views.docx, name='docx'),
    re_path(r'^(?P<pk>\d+)', views.contract, name='contract'),
    re_path(r'newtransaction/(?P<pk>\d+)/', views.contract_transaction_new, name='contract_transaction_new'),
    path('newcontract/', ContractCreateView.as_view(), name='ContractCreateView'),
    path('excel/', views.excel, name='excel'),

]
