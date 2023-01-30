from django.shortcuts import render
from django.http import HttpResponse
from .models import Member

def member_list (request) :
    member_list = Member.objects.all()
    
    return render(
        request,
        "memberapp/member/member_list.html",
        {"member_list" : member_list}
    )
    
def member_view (request) :
    try :
        if request.method == "GET" :
            mem_id = request.GET["mem_id"]
            
        elif request.method == "POST" :
            mem_id = request.POST["mem_id"]
        
        # member 상세정보 1건 가지고 오기 
        member_view = Member.objects.get(mem_id = mem_id)
        
        return render(
            request,
            "memberapp/member/member_view.html",
            {"member_view" : member_view}
        )
    except :
        url = "/member/member_list/"
        msg = """
            <script>
                alert("정상적인 접근이 아닙니다");
                location.href = "{}";
            </script>
        """.format(url)
        return HttpResponse(msg)
    
def member_insert_form (request) :
    return render(request,
                  "memberapp/member/member_insert_form.html",
                  {})

def member_insert (request) :
    if request.method == "GET" :
        mem_id = request.GET["mem_id"]
        mem_pass = request.GET["mem_pass"]
        mem_name = request.GET["mem_name"]
        mem_regno1 = request.GET["mem_regno1"]
        mem_regno2 = request.GET["mem_regno2"]
        mem_bir = request.GET["mem_bir"]
        mem_zip = request.GET["mem_zip"]
        mem_add1 = request.GET["mem_add1"]
        mem_add2 = request.GET["mem_add2"]
        mem_hometel = request.GET["mem_hometel"]
        mem_comtel = request.GET["mem_comtel"]
        mem_hp = request.GET["mem_hp"]
        mem_mail = request.GET["mem_mail"]
        mem_job = request.GET["mem_job"]
        mem_like = request.GET["mem_like"]
        mem_memorial = request.GET["mem_memorial"]
        mem_memorialday = request.GET["mem_memorialday"]
        mem_mileage = request.GET["mem_mileage"]
        mem_delete = request.GET["mem_delete"]
    elif request.method == "POST" :
        mem_id = request.POST["mem_id"]
        mem_pass = request.POST["mem_pass"]
        mem_name = request.POST["mem_name"]
        mem_regno1 = request.POST["mem_regno1"]
        mem_regno2 = request.POST["mem_regno2"]
        mem_bir = request.POST["mem_bir"]
        mem_zip = request.POST["mem_zip"]
        mem_add1 = request.POST["mem_add1"]
        mem_add2 = request.POST["mem_add2"]
        mem_hometel = request.POST["mem_hometel"]
        mem_comtel = request.POST["mem_comtel"]
        mem_hp = request.POST["mem_hp"]
        mem_mail = request.POST["mem_mail"]
        mem_job = request.POST["mem_job"]
        mem_like = request.POST["mem_like"]
        mem_memorial = request.POST["mem_memorial"]
        mem_memorialday = request.POST["mem_memorialday"]
        mem_mileage = request.POST["mem_mileage"]
        mem_delete = request.POST["mem_delete"]    
    
    Member(mem_id = mem_id, mem_pass = mem_pass,
            mem_name = mem_name, mem_regno1 = mem_regno1,
            mem_regno2 = mem_regno2, mem_bir = mem_bir,
            mem_zip = mem_zip, mem_add1 = mem_add1, 
            mem_add2 = mem_add2, mem_hometel = mem_hometel,
            mem_comtel = mem_comtel, mem_hp = mem_hp,
            mem_mail = mem_mail, mem_job = mem_job,
            mem_like =mem_like, mem_memorial = mem_memorial,
            mem_memorialday = mem_memorialday, mem_mileage = mem_mileage,
            mem_delete = mem_delete).save()
    
    url = "/member/member_list/"
    msg = """
        <script>
            alert("정상적으로 저장 됨");
            location.href = "{}";
        </script>    
    """.format(url)
    return HttpResponse(msg)

def member_update_view(request) :
    try :
        if request.method == "GET" :
            mem_id = request.GET["mem_id"]
            
        elif request.method == "POST" :
            mem_id = request.POST["mem_id"]
        
        # member 상세정보 1건 가지고 오기 
        member_view = Member.objects.get(mem_id = mem_id)
        
        return render(
            request,
            "memberapp/member/member_update_view.html",
            {"member_view" : member_view}
        )
    except :
        url = "/member/member_list/"
        msg = """
            <script>
                alert("정상적인 접근이 아닙니다");
                location.href = "{}";
            </script>
        """.format(url)
        return HttpResponse(msg)

def member_update (request) :
    if request.method == "GET" :
        mem_id = request.GET["mem_id"]
        mem_pass = request.GET["mem_pass"]
        mem_name = request.GET["mem_name"]
        mem_regno1 = request.GET["mem_regno1"]
        mem_regno2 = request.GET["mem_regno2"]
        mem_bir = request.GET["mem_bir"]
        mem_zip = request.GET["mem_zip"]
        mem_add1 = request.GET["mem_add1"]
        mem_add2 = request.GET["mem_add2"]
        mem_hometel = request.GET["mem_hometel"]
        mem_comtel = request.GET["mem_comtel"]
        mem_hp = request.GET["mem_hp"]
        mem_mail = request.GET["mem_mail"]
        mem_job = request.GET["mem_job"]
        mem_like = request.GET["mem_like"]
        mem_memorial = request.GET["mem_memorial"]
        mem_memorialday = request.GET["mem_memorialday"]
        mem_mileage = request.GET["mem_mileage"]
        mem_delete = request.GET["mem_delete"]
    elif request.method == "POST" :
        mem_pass = request.POST["mem_pass"]
        mem_name = request.POST["mem_name"]
        mem_regno1 = request.POST["mem_regno1"]
        mem_regno2 = request.POST["mem_regno2"]
        mem_bir = request.POST["mem_bir"]
        mem_zip = request.POST["mem_zip"]
        mem_add1 = request.POST["mem_add1"]
        mem_add2 = request.POST["mem_add2"]
        mem_hometel = request.POST["mem_hometel"]
        mem_comtel = request.POST["mem_comtel"]
        mem_hp = request.POST["mem_hp"]
        mem_mail = request.POST["mem_mail"]
        mem_job = request.POST["mem_job"]
        mem_like = request.POST["mem_like"]
        mem_memorial = request.POST["mem_memorial"]
        mem_memorialday = request.POST["mem_memorialday"]
        mem_mileage = request.POST["mem_mileage"]
        mem_delete = request.POST["mem_delete"]    
    
    Member(mem_id = mem_id).update( mem_pass = mem_pass,
            mem_name = mem_name, mem_regno1 = mem_regno1,
            mem_regno2 = mem_regno2, mem_bir = mem_bir,
            mem_zip = mem_zip, mem_add1 = mem_add1, 
            mem_add2 = mem_add2, mem_hometel = mem_hometel,
            mem_comtel = mem_comtel, mem_hp = mem_hp,
            mem_mail = mem_mail, mem_job = mem_job,
            mem_like =mem_like, mem_memorial = mem_memorial,
            mem_memorialday = mem_memorialday, mem_mileage = mem_mileage,
            mem_delete = mem_delete)
    
    url = "/member/member_list/"
    msg = """
        <script>
            alert("정상적으로 저장 됨");
            location.href = "{}";
        </script>    
    """.format(url)
    return HttpResponse(msg)



# Create your views here.
