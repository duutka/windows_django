from django.shortcuts import render, redirect
from good.models import Good, Order
from django.views.generic import ListView, DetailView, FormView, TemplateView
from good.forms import SearchOrderForm
from django.db.models import Q
from good.forms import CustomerForm, OrderForm, GoodForm
from datetime import datetime, timedelta
from .models import *

class OrderList(ListView):
    model = Good
    template_name = 'good/good.html'
    paginate_by = 10
    queryset = Good.objects.all().order_by("-completed")

    def get_context_data(self, **kwargs):
        context = super(OrderList, self).get_context_data(**kwargs)
        context['form'] = SearchOrderForm()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        form = SearchOrderForm(self.request.GET)
        if form.is_valid():
            information = form.cleaned_data['information']
            if information:
                queryset = queryset.filter(
                    Q(order__id__icontains=information)|
                    Q(order__customer__last_name__icontains=information)|
                    Q(order__customer__first_name__icontains=information)|
                    Q(order__customer__patronymic__icontains=information)
                )
        return queryset

class OrderCreateView(TemplateView):
    template_name = 'good/good_form.html'
    success_url = '/order/'

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data(**kwargs)
        context['form_customer'] = CustomerForm(self.request.POST)
        context['form_order'] = OrderForm(self.request.POST)
        context['form_good'] = GoodForm(self.request.POST)
        return context

    def post(self, request, *args, **kwargs):
        error=''
        context = self.get_context_data(**kwargs)
        if context['form_customer'].is_valid():
            instance_customer = context['form_customer'].save()
        if context['form_order'].is_valid():
            instance_order = context['form_order'].save()
        if context['form_good'].is_valid():
            instance_good = context['form_good'].save()
        return self.render_to_response(context)



class DescriptionList(ListView):
    model=Good
    template_name='good/description_product.html'

def information(request, pk):
    template_name='good/description_product.html'
    order = Order.objects.get(id=pk)
    goods = Good.objects.filter(order=order.id)
    context={
    'order':order,
    'goods':goods
    }
    return render(request, 'good/description_product.html', context)

class GraphList(ListView):
    model = Good
    hour = 8
    template_name = 'good/graph_list.html'
    good_list=[]

    def get_context_data(self, **kwargs):
        context = super(GraphList, self).get_context_data(**kwargs)
        today = datetime.today().replace(hour=8,minute=0)
        day_list = [{'date':today +timedelta(days=x) ,'goods':[]}for x in range(4)]
        for day in day_list:
            start = day['date']
            end = start + timedelta(hours=1)
            for x in range(10):
                day['goods'].append(
                    {'date':start.strftime('%H:%M'),
                     'data':Good.objects.filter(created__range=[start,end])
                     })
                start+=timedelta(hours=1)
                end+=timedelta(hours=1)
        context['hour'] = range(8)
        context['day_list'] = day_list
        return context
