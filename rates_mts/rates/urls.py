from django.urls import path
from rates import views

urlpatterns = [
    path('parser', views.run_parser),
]
