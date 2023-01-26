
from django.urls import path, include
from . import views


#  url을 만들어서 view.py의 함수와 매핑하기 
urlpatterns = [
    
    path('test/',views.test), 
    path('cart_list/',views.cart_list), 
    path('cart_view/',views.cart_view), 
]
