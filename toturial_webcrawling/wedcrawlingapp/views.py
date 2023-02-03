from django.shortcuts import render
from django.http import HttpResponse
from wedcrawlingapp.web.webcrawling import WebCrawling
from .models import Melon

# 웹 크롤링 및 저장 
def wedCrawling(request) :
    wc = WebCrawling("http://www.melon.com/chart/index.htm")
    # 웹 크롤링 데이터 조회하기 
    model_list = wc.getData()
    #웨드라이버 종료하기 
    wc.webdriver_quit()
    
    # DB에 저장하기 
    # melon 테이블에는 10개의 데이터만 유지 
    # 데이터가 없으면 insert, 있으면 update
    melon_cnt = Melon.objects.count()
    
    if melon_cnt > 0 :
        # 데이터가 있으면 수행 
        for data in model_list :
            Melon.objects.filter(no = data["no"]).update(no = data['no'], 
                                                        title = data['title'],
                                                        singer= data['singer'] ) 
            
    else : 
        # 데이터가 없으면 수행 
        for data in model_list :
            Melon(no = data['no'], 
                  title = data['title'],
                  singer= data['singer'] ).save() 
    
    msg  = """
        <script>
            alert('웹크롤링 및 DB 입력/수정 성공!!')
            location.href = '/crawling'
        </script>
    """
    return HttpResponse(msg)
    # return render(request,
    #               "wedcrawlingapp/webcrawling.html",
    #               {"melon_list" : model_list}
    #               )

def melon_list(request) :
    melon_list = Melon.objects.all()
    
    return render(
        request,
        "wedcrawlingapp/webcrawling.html",
        {"melon_list" : melon_list}
    )
# Create your views here.
