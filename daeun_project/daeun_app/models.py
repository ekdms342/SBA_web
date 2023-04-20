from django.db import models
from django.db.models.fields import CharField, IntegerField,TextField

class Prod (models.Model) :
    prod_id = CharField(primary_key=True, max_length=30, null=False) #tkdvnazhem
    prod_name = CharField(max_length=40, null=False) # 상품명
    prod_lgu = CharField(max_length=4, null=False) # 상품분류
    prod_buyer = CharField(max_length=6, null=False) # 공급업체 
    prod_sale = IntegerField(max_length=10, null=False) # 판매가
    prod_outline = CharField(max_length=50, null=False) # 상품개략설명
    prod_detail = TextField(null=True) #상품 상세 설명 
    prod_img = CharField(max_length=40, null=False) # 상품이미지
    prod_size = CharField(max_length=20, null=True) # 크기
    prod_color = CharField(max_length=20, null=True) # 색상
    prod_delivery = CharField(max_length=255, null=True) # 배달 특이사항
    prod_mileage = IntegerField(max_length=10, null= True) # 개당 마일리지 점수 
    
    # DB 속성 정의 : 클래스 이름 및 변수이름 변경 불가 
    class Meta :
        #  사용할 실제 테이블 이름 지정 
        db_table = "prod"
        #  현재 model을 사용할 앱 지정 
        app_label = "daeun_app"
        #  테이블의 실제 Db에 존재하면 False (보통 False사용)
        managed = False
    
    
# Create your models here.
