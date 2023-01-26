from django.shortcuts import render
from django.http import HttpResponse

def main(request) :
    return HttpResponse('<u>Main</u>')

def sample(request) :
    return render(request,
                  'secondapp/02_sample.html',
                  {})
    
def login_form(request) :
    return render(request,
                  'secondapp/form/form.html',
                  {})
    
def login_form_check(request) :
    
    if request.method == " GET" :
        mem_id = request.GET["mem_id"]
        mem_pass = request.Get["mem_pass"]
        
    elif request.method == "POST" :
        mem_id = request.POST['mem_id']
        mem_pass = request.POST["mem_pass"]
    
    return render(request,
                  'secondapp/form/form_check.html',
                  {"mem_id" : mem_id,
                   "mem_pass" : mem_pass})

# Create your views here.
