
from django.urls import path, include
from . import views


#  url을 만들어서 view.py의 함수와 매핑하기 
urlpatterns = [
    # 장바구니
    path('test/',views.test), 
    path('cart_list/',views.cart_list), 
    path('cart_view/',views.cart_view), 
    path('cart_insert_form/',views.cart_insert_form), 
    path('cart_insert/',views.cart_insert), 
    path('cart_update_view/',views.cart_update_view), 
    path('cart_update/',views.cart_update), 
    path('cart_delete/',views.cart_delete), 
    
    
    # 로그임 
    path('login_form/',views.login_form), 
    path('login/',views.login), 
    path('logout/',views.logout), 
]
