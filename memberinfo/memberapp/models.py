from django.db import models
from django.db.models.fields import CharField, IntegerField,DateTimeField

class Member(models.Model) :
    mem_id = CharField(primary_key=True, max_length=15, null=False)
    mem_pass = CharField(max_length=15, null=False)
    mem_name = CharField(max_length=10, null=False)
    mem_regno1 = CharField(max_length=6, null=False)
    mem_regno2 = CharField(max_length=7, null=False)
    mem_bir = DateTimeField(null=True)
    mem_zip = CharField(max_length=7, null=False)
    mem_add1 = CharField(max_length=60, null=False)
    mem_add2 = CharField(max_length=50, null=False)
    mem_hometel = CharField(max_length=14, null=False)
    mem_comtel = CharField(max_length=14, null=False)
    mem_hp = CharField(max_length=15, null=True)
    mem_mail = CharField(max_length=40, null=False)
    mem_job = CharField(max_length=40, null=True)
    mem_like = CharField(max_length=40, null=True)
    mem_memorial = CharField(max_length=40, null=True)
    mem_memorialday = DateTimeField(null=True)
    mem_mileage = IntegerField(max_length=10, null=True)
    mem_delete = CharField(max_length=1, null=True)
    
     # DB 속성 정의 : 클래스 이름 및 변수이름 변경 불가 
    class Meta :
        #  사용할 실제 테이블 이름 지정 
        db_table = "member"
        #  현재 model을 사용할 앱 지정 
        app_label = "memberapp"
        #  테이블의 실제 Db에 존재하면 False (보통 False사용)
        managed = False
    
# Create your models here.