from django.conf.urls import url, include
from django.contrib import admin
from . import views
from good.models import Good
from django.conf.urls import url
from django.urls import re_path, path, include
from good.views import OrderList, DescriptionList, OrderCreateView, GraphList
from django.views.generic import DetailView

urlpatterns = [
path('', OrderList.as_view()),
path('description/',DescriptionList.as_view()),
url(r'^description/(?P<pk>\d+)$', views.information, name="information"),
path('neworder/', OrderCreateView.as_view(), name='OrderCreateView'),
path('graphs/', GraphList.as_view(), name = 'graphs'),
]
