from django.urls import path
from rates import views

urlpatterns = [
    path('parser', views.run_parser, name='run_parser'),
    path('rates', views.rates_list, name='rates'),
    path('clear_rates', views.clear_results, name='clear_results'),
    path('waiting', views.waiting_for_pasring, name='rates_wait')
]
