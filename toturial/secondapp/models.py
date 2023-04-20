from django.db import models
from django.db.models.fields import CharField, IntegerField

class Iprod(models.Model) :
    # 실제 DB와 동일하게 지정 
    lprod_id = IntegerField( max_length=10, null=False)
    lprod_gu = CharField(primary_key=True, max_length=4, null=False)
    lprod_nm = CharField(max_length=40, null=False)
    
    # DB 속성 정의 : 클래스 이름 및 변수이름 변경 불가 
    class Meta :
        #  사용할 실제 테이블 이름 지정 
        db_table = "lprod"
        #  현재 model을 사용할 앱 지정 
        app_label = "secondapp"
        #  테이블의 실제 Db에 존재하면 False (보통 False사용)
        managed = False

# Create your models here.
