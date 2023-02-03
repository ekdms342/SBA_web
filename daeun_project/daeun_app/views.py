from django.shortcuts import render
from django.http import HttpResponse
from .models import Prod

def login_logout(request) :
    return render(
        request,
        'daeun_app/login.html'
    )
 

def prod_list (request) :
    
    try : 
        if request.method == "GET" :
            login_check = request.GET["login_check"]
        elif request.method == "POST" :
            login_check = request.POST["login_check"]
        
        if login_check == "login" :
            
            prod_list = Prod.objects.all()
            return render(
                request,
                "daeun_app/prod/prod_list.html",
                {"prod_list" : prod_list, "chkID" : "login"}
            )
        else :
            return render(
                request,
                "daeun_app/login.html"
            )
    except :
        url = "/daeun_app/login/"
        msg = """
            <script>
                alert("정상적인 접근이 아닙니다");
                location.href = "{}";
            </script>
        """.format(url)
        return HttpResponse(msg)
        
# Create your views here.
