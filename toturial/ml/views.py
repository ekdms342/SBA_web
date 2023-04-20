from django.shortcuts import render
from django.http import HttpResponse

# 판다스 
import pandas as Pd 

# 앤스콤 폴더
from ml.dataset.csv import dataset_csv as dc
# import ml.dataset.csv as dc

#RNN 폴더
from ml.rnn import rnn as rn

def sample(request) :
    return HttpResponse("안녕하세요")

# 앤스콤 데이터 조회하기 (샘플)
def getAnscomData(request) :
    df = dc.Dataset_csv()
    
    df_ans = df.getAnscombeData()
    return HttpResponse(df_ans)
# Create your views here.

# HTML 
def getAns_List(request) :
    df = dc.Dataset_csv()
    # 컬럼명, 데이터리스트 조회 
    columns, df_list = df.getAColumn_List()
    
    #엔스콤 시각화 이미지 저장하기 
    df.initVisualization()
    
    return render(request,
                  "ml/anscom_list.html",
                  {"columns" : columns,
                   "df_list" : df_list})
    
def getModel(request) :
    dr = rn.RNN()
    df_rnn = dr.getModel()
    return HttpResponse(df_rnn)

def predict_insert_form(request) :
    # 글쓰기 페이지 html : cart_insert_form.html
    return render(request,
                  'ml/rnn.html',
                  {})


def Predict(request) :
    
    if request.method == "GET" :
        current_word = request.GET['current_word']
        n = request.GET["n"]
        n = int(n)
    elif request.method == "POST" :
        current_word = request.POST['current_word']
        n = request.POST["n"]
        n = int(n)
        
    dr = rn.RNN()
    df_rnn = dr.sentence_generation(current_word,n)
    return HttpResponse(df_rnn)
        
    