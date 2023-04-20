
from django.urls import path, include
from . import views


#  url을 만들어서 view.py의 함수와 매핑하기 
urlpatterns = [
    # 브라우저에서 index url로 요청하는 모든 것은 
    # firstapp의 view.py의 index()함수를 자동으로 호출 실행해서 
    #  함수내부의 내용을 리턴(응답)한다 
    
    # 127.0.0.1:8000/first/xxxx 는 모두 firstapp의 urls가 관리
    path('sample/',views.sample),
    path('main/',views.main),
    path('login_form/',views.login_form),
    path('login_form_check/',views.login_form_check),
    path('iprod_list/',views.iprod_list),
    
]
