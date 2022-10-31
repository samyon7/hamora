from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/create', views.save, name='product.create'),
    path('product/buy', views.buy, name='product.buy'),
    path('chart', views.chart, name='chart'),
    path('chart/decrement', views.decrement, name='decrement'),
    path('chart/increment', views.incerment, name='increment'),
    path('chart/checkout', views.checkout, name='checkout')
]