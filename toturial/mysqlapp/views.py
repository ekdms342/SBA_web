from django.shortcuts import render
from django.http import HttpResponse
from .models import Cart
# Create your views here.

def test(request) :
    return HttpResponse('<u>mysqlapp</u>')

def cart_list (request) :
    # cart 전체 정보 가지고 오기 
    cart_list = Cart.objects.all()
    
    return render(
        request,
        "mysqlapp/cart/cart_list.html",
        {"cart_list" : cart_list}
    )
    
# 주문정보 상세보기 
def cart_view (request) :
    if request.method == "GET" :
        cart_no = request.GET["cart_no"]
        cart_prod = request.GET["cart_prod"]
        
    elif request.method == "POST" :
        cart_no = request.POST["cart_no"]
        cart_prod = request.POST["cart_prod"]
    
    # cart 상세정보 1건 가지고 오기 
    cart_view = Cart.objects.get(cart_no = cart_no,
                                 cart_prod = cart_prod)
    
    return render(
        request,
        "mysqlapp/cart/cart_view.html",
        {"cart_view" : cart_view}
    )

