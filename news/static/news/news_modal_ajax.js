$(document).on('click','.modalStart',function(e) {
    e.stopPropagation(); // 같은 영역에 속해있는 중복 클릭 방지 
    e.preventDefault();  // 이벤트 진행 중지 

	var pk = $(this).attr('name');
	console.log(pk);
    var url = $(this).attr('href');
    var csrf=getCookie("csrftoken");
    $.ajax({
        type: 'post',
        url: url,
        data: {
        	'pk':pk,
        	'csrfmiddlewaretoken': csrf
        },
    	success: function (data, textStatus, jqXHR) {
            $('#post-modal').find('.modal-content').html(data);
            $('#post-modal').modal('show');
        },
    });
});