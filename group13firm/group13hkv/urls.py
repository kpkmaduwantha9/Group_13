from django.urls import path
from . import views

urlpatterns = [
    path('', views.hkvhome , name='hkvhome'),
    
   
]
