from django.shortcuts import render
from django.http import HttpResponse

def hello(request) :
    return HttpResponse('<u>Hello FrontApp</u>')

# Create your views here.

# templates의 sample.html 파일 호출하기 
def sample(request) :
    # render 함수 인지 설명 
    ## 첫번째 값  요청으로 들어온 모든 값 넘기기 
    ## 두번째 값 : 응답할 html 파일의 정의
    ### url 규칙 : 앱이름 작성 -> templates 호출 
    ## 세번쨰 값 : html 에 넣을 데이터들 -> 딕셔너리 (키-밸류) 형태 
    return render(request,
                  "frontapp/01_sample.html",
                  {})

def index (request) :
    return render(request,
                  'frontapp/index.html',
                  {})
    
def about_me (request) :
    return render(request,
                  'frontapp/about_me.html',
                  {})
    
def blog (request) :
    return render(request,
                  'frontapp/blog.html',
                  {})

def index_css (request) :
    return render(request,
                  'frontapp/index_css.html',
                  {})
    
def index_css2 (request) :
    return render(request,
                  'frontapp/index_css2.html',
                  {})
    
def index_css3 (request) :
    return render(request,
                  'frontapp/index_css3.html',
                  {})
    
def index_javascript1 (request) :
    return render(request,
                  'frontapp/index_javascript1.html',
                  {})
    
def index_javascript2 (request) :
    return render(request,
                  'frontapp/index_javascript2.html',
                  {})

def index_bootstrap1 (request) :
    return render(request,
                  'frontapp/index_bootstrap1.html',
                  {})