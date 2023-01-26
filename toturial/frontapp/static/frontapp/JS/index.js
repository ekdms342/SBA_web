function doSumething(){
    // 잘 호출되는지 확인
    // 팝업창 띄우기
    //alert("잘호출 됩니다");
    //input 텍스트 박스의 값 조회(추출)하기
    // document : html 문서 전체를 document라고 한다
    // getElementById : 태그 id 속성의 값이 괄호()안에 있는 값인 것 찾기 
    // value : 텍스트 박스 안의 값(문자 타입으로 받아온다)
    a = document.getElementById("inputA").value;
    b = document.getElementById("inputB").value;
    // alert(a);
    // alert(b);
    //Javascript int : Number
    document.getElementById("valueA").innerHTML = a;
    document.getElementById("valueB").innerHTML = b;
    document.getElementById("valueC").innerHTML = Number(a) + Number(b); 

}
//시간 안내 팝업창 띄우기
function viewTime(){
    // 잘 호출되는지 확인 
    // alert("bb")
    alert(new Date());

}