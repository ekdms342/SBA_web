from django.shortcuts import render
from django.http import HttpResponse

def main(request) :
    return HttpResponse('<u>Main</u>')

def sample(request) :
    return render(request,
                  'secondapp/02_sample.html',
                  {})

# Create your views here.
