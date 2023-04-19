
from django.urls import path, include
from . import views


#  url을 만들어서 view.py의 함수와 매핑하기 
urlpatterns = [
    # 장바구니
    path('sample/',views.sample), 
    path('anscom/',views.getAnscomData), 
    path('ans_list/',views.getAns_List), 
    path('model/',views.getModel), 
    path('predict_insert_form/',views.predict_insert_form), 
    path('predict/',views.Predict), 
]
