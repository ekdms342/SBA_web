from django.shortcuts import render
from django.http import HttpResponse
from .models import Cart, Member
# Create your views here.

def test(request) :
    return HttpResponse('<u>mysqlapp</u>')

def cart_list (request) :
    # cart 전체 정보 가지고 오기 
    cart_list = Cart.objects.all()
    
    return render(
        request,
        "mysqlapp/cart/cart_list.html",
        {"cart_list" : cart_list}
    )
    
# 주문정보 상세보기 
def cart_view (request) :
    try :
        if request.method == "GET" :
            cart_no = request.GET["cart_no"]
            cart_prod = request.GET["cart_prod"]
            
        elif request.method == "POST" :
            cart_no = request.POST["cart_no"]
            cart_prod = request.POST["cart_prod"]
        # cart 상세정보 1건 가지고 오기 
        cart_view = Cart.objects.get(cart_no = cart_no,
                                    cart_prod = cart_prod)
        
        return render(
            request,
            "mysqlapp/cart/cart_view.html",
            {"cart_view" : cart_view}
        )
    except :
        url = "/mysql/cart_list/"
        msg = """
            <script>
                alert("정상적인 접근이 아닙니다");
                location.href = "{}";
            </script>
        """.format(url)
    
    return HttpResponse(msg)
    

# 글쓰기 페이지 처리 
def cart_insert_form(request) :
    # 글쓰기 페이지 html : cart_insert_form.html
    return render(request,
                  'mysqlapp/cart/cart_insert_form.html',
                  {})
    
# 글쓰기 저장하기 
def cart_insert(request) :
    
    try : 
        if request.method == "GET" :
            cart_no = request.GET['cart_no']
            cart_prod = request.GET["cart_prod"]
            cart_member = request.GET["cart_member"]
            cart_qty = request.GET["cart_qty"]
        elif request.method == "POST" :
            cart_no = request.POST['cart_no']
            cart_prod = request.POST["cart_prod"]
            cart_member = request.POST["cart_member"]
            cart_qty = request.POST["cart_qty"]
        
        # DB에 저장하기 
        Cart(cart_no = cart_no, 
            cart_prod = cart_prod,
            cart_member = cart_member,
            cart_qty = cart_qty).save() 
        
        url = "/mysql/cart_list/"
        msg = """
            <script>
                alert("정상적으로 저장 됨");
                location.href = "{}";
            </script>
        """.format(url)
        
        return HttpResponse(msg)
    except :
        url = "/mysql/cart_list/"
        msg = """
            <script>
                alert("정상적인 접근이 아닙니다");
                location.href = "{}";
            </script>
        """.format(url)

    return HttpResponse(msg)
    
    # return render(
    #     request,
    #     "mysqlapp/cart/cart_list.html",
    #     {}
    # )
    
# 수정할 내용 보이기    
def cart_update_view (request) :
    try : 
        if request.method == "GET" :
            cart_no = request.GET["cart_no"]
            cart_prod = request.GET["cart_prod"]
            
        elif request.method == "POST" :
            cart_no = request.POST["cart_no"]
            cart_prod = request.POST["cart_prod"]
        
        # cart 상세정보 1건 가지고 오기 
        cart_view = Cart.objects.get(cart_no = cart_no,
                                    cart_prod = cart_prod)
        
        return render(
            request,
            "mysqlapp/cart/cart_update_view.html",
            {"cart_view" : cart_view}
        )
    except :
        url = "/mysql/cart_list/"
        msg = """
            <script>
                alert("정상적인 접근이 아닙니다");
                location.href = "{}";
            </script>
        """.format(url)
    
    return HttpResponse(msg)

#수정 내용 저장하기
def cart_update(request) :
    try :
        
        if request.method == "GET" :
            cart_no = request.GET['cart_no']
            cart_prod = request.GET["cart_prod"]
            cart_qty = request.GET["cart_qty"]
        elif request.method == "POST" :
            cart_no = request.POST['cart_no']
            cart_prod = request.POST["cart_prod"]
            cart_qty = request.POST["cart_qty"]
        
        # DB에 저장하기 
        Cart.objects.filter(cart_no= cart_no, 
                            cart_prod = cart_prod).update(cart_qty = cart_qty)
        
        url = "/mysql/cart_view/"
        url = url + "?cart_no=" + cart_no +"&cart_prod=" + cart_prod
        msg = """
            <script>
                alert("정상적으로 수정 됨");
                location.href = "{}";
            </script>
        """.format(url)
        
        return HttpResponse(msg) 
    except :
        url = "/mysql/cart_list/"
        msg = """
            <script>
                alert("정상적인 접근이 아닙니다");
                location.href = "{}";
            </script>
        """.format(url)
        return HttpResponse(msg)

# 삭제하기 
def cart_delete(request) :
    try : 
        if request.method == "GET" :
            cart_no = request.GET['cart_no']
            cart_prod = request.GET["cart_prod"]
        elif request.method == "POST" :
            cart_no = request.POST['cart_no']
            cart_prod = request.POST["cart_prod"]
        
        # DB에 저장하기 
        Cart.objects.filter(cart_no= cart_no, 
                            cart_prod = cart_prod).delete()
        
        url = "/mysql/cart_list/"
        msg = """
            <script>
                alert("정상적으로 삭제 됨");
                location.href = "{}";
            </script>
        """.format(url)
        
        return HttpResponse(msg) 
    except :
        url = "/mysql/cart_list/"
        msg = """
            <script>
                alert("정상적인 접근이 아닙니다");
                location.href = "{}";
            </script>
        """.format(url)
    
        return HttpResponse(msg)

# 로그임 화면 페이지 
def login_form(request) :
    return render (
        request,
        "mysqlapp/login/login_logout.html",
        {"chkID" : "login"}
    )
    
def login (request) :
    try : 
        # 파라미터 받아오기 
        if request.method == "GET" :
            mem_id = request.GET["mem_id"]
            mem_pass = request.GET["mem_pass"]
        elif request.method == "POST" :
            mem_id = request.POST["mem_id"]
            mem_pass = request.POST["mem_pass"]
        
        try:   
            # 아이디와 패스워드로 데이터 조회하기 
            mem_info = Member.objects.get(mem_id = mem_id,
                                        mem_pass = mem_pass)
            #  세션 (session) 처리하기 
            # - 회원아이디와 이름을 세션 객체에 저장하기 
            # - 세션 객체는 브라우저가 저속되어 있는 한 유지 시키기 위한 객체
            request.session["sMem_id"] = mem_info.mem_id
            request.session["sMem_name"] = mem_info.mem_name
            
        except :
            msg = """
                <script>
                    alert('아이디 또는 패스워드를 확인해 주세요');
                    location.href = '/mysql/login_form';
                </script>
            """
            return HttpResponse(msg)
    except :
        msg = """
            <script>
                alert('잘못된 접근입니다');
                location.href = '/mysql/login_form';
            </script>
        """
        return HttpResponse(msg)
    
    return render(request,
                  "mysqlapp/login/login_logout.html",
                  {
                        "sMem_id" : request.session.get("sMem_id"),
                        "sMem_name" : request.session.get("sMem_name"),
                        # "mem_info" : mem_info,
                        "chkID" : "logout"
                        }
                  )
    
def logout(request) :
    # 로그인 상태 확인하기 : 세션에 id 값이 있는지 확인 
    if request.session.get("sMem_id") :
        # 세션 정조가 있다면, 로그아웃 처리하기 
        request.session.flush()  
        msg = """
            <script>
                alert('로그아웃 되었습니다');
                location.href = '/mysql/login_form/';
            </script>
        """
        return HttpResponse(msg)
    else :
        msg = """
            <script>
                alert('잘못된 접근입니다, 로그인 페이지로 이동합니다');
                location.href = '/mysql/login_form/';
            </script>
        """
        return HttpResponse(msg)
    
    
    
    # return render(request,
    #               "mysqlapp/login/login_logout.html",
    #               {"chkID" : "login"})