from django.urls import path
from . import views

urlpatterns = [
    path('', views.hkvhome , name='hkvhome'),
    path('funding/', views.funding_view, name='funding'), 
    
]