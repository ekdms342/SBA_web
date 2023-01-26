"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from firstapp import views

#  url을 만들어서 view.py의 함수와 매핑하기 
urlpatterns = [
    # 브라우저에서 index url로 요청하는 모든 것은 
    # firstapp의 view.py의 index()함수를 자동으로 호출 실행해서 
    #  함수내부의 내용을 리턴(응답)한다 
    
    # 127.0.0.1:8000/first/xxxx 는 모두 firstapp의 urls가 관리
    path('mysql/',include('mysqlapp.urls')),
    path('front/',include('frontapp.urls')),
    path('second/',include('secondapp.urls')),
    path('first/',include('firstapp.urls')),
    path('index2/',views.index2),
    path('index1/',views.index1),
    path('index/',views.index),
    path('',views.index),
    path("admin/", admin.site.urls),
]
