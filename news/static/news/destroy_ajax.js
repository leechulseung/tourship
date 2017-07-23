$('.destroy').unbind().bind("click", addAnswer);

        function addAnswer(e){
        e.submit
        e.stopPropagation(); // 같은 영역에 속해있는 중복 클릭 방지 
        e.preventDefault();  // 이벤트 진행 중지 
        
        var pk = $(this).attr('name'); //선택된 요소의 부모의 name속성 캐치

        var url = "/newspeed/destroy/";
        var csrf = getCookie("csrftoken");
        
        var destroy = confirm('정말로 삭제하시겠 습니까?')

        if(destroy){
          $.ajax({
               type : 'post', // post방식으로 전송
               url : url, // 서버로 보낼 url 주소
               data : {  // 서버로 보낼 데이터들 dict형식 
                'pk':pk,
                'csrfmiddlewaretoken': csrf,
                },
                // 서버에서 리턴받아올 데이터 형식
               dataType : 'html',  

               //서버에서 무사히 html을 리턴하였다면 실행 
               success : function(data, textStatus, jqXHR){
                location.reload(); 
                alert("삭제 되었습니다.")
                //append(data);
               },

               //서버에서 html을 리턴해주지 못했다면 
               error : function(data, textStatus, jqXHR){
                alert("실패 하였다.");
               },
               
           });
        }else{
          
        }
        
       }
