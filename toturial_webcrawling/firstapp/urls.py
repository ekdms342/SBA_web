
from django.urls import path
from . import views

#  url을 만들어서 view.py의 함수와 매핑하기 
urlpatterns = [
    # 브라우저에서 index url로 요청하는 모든 것은 
    # firstapp의 view.py의 index()함수를 자동으로 호출 실행해서 
    #  함수내부의 내용을 리턴(응답)한다 
    # 127.0.0.1:8000/first/main 
    path('index3/',views.index3), 
    path('main/',views.index2),
    path('index1/',views.index1),
    path('index/',views.index),
]
