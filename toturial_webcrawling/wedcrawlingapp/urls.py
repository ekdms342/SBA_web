
from django.urls import path, include
from . import views

urlpatterns = [
    path('webcrawling/',views.wedCrawling), 
    path('',views.melon_list), 

]
