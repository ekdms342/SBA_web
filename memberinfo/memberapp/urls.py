from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("member_list/", views.member_list),
    path("member_view/", views.member_view),
    path("member_insert_form/", views.member_insert_form),
    path("member_insert/", views.member_insert),
    path("member_update_view/", views.member_update_view),
    path("member_update/", views.member_update),
    
]
