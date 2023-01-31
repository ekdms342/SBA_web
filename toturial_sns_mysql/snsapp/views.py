from django.shortcuts import render

def login_logout(request) :
    return render(
        request,
        'snsapp/login.html'
    )

# Create your views here.
