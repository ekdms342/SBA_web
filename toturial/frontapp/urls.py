
from django.urls import path, include
from . import views


#  url을 만들어서 view.py의 함수와 매핑하기 
urlpatterns = [
    
     # 127.0.0.1:8000/front/sample
    path('sample/',views.sample), 
     # 127.0.0.1:8000/front/hello
    path('hello/',views.hello), 
    # 127.0.0.1:8000/front
    path('index',views.index), 
    # 127.0.0.1:8000/front
    path('',views.index), 
    path('blog/',views.blog), 
    path('about_me/',views.about_me), 
    path('index_css/',views.index_css),
    path('index_css2/',views.index_css2),
    path('index_css3/',views.index_css3),
    path('index_javascript1/',views.index_javascript1),
    path('index_javascript2/',views.index_javascript2),
    path('index_bootstrap1/',views.index_bootstrap1),
]
