// 获取 csrftoken
jQuery(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});

$('#signup_submit').click(function() {
    url = '/user/signup/';
    userType = $('input[name=userType]:checked').val();
    nickname = $('input[id=nickname]').val();
    gender = $('input[name=gender]:checked').val();

    major = $('input[id=major]').val();
    introduction = $('input[id=introduction]').val();
    email = $('input[id=email]').val();
    password = $('input[id=password]').val();
    password_verify = $('input[id=password-verify]').val();

    $.ajax({
        url: url,
        method: 'POST',
        dataType:'json',
        data: {
            'userType': userType,
            'nickname': nickname,
            'gender': gender,
            'major': major,
            'introduction': introduction,
            'email': email,
            'password': password,
            'password_verify': password_verify,
        },
        success: function (data) {
            if(data['fail']){
                if ('complete' == data['type']){
                    alert('請填寫完整信息')
                }else if ('match' == data['type']){
                    alert('密碼不一致')
                }else if ('exist' == data['type']){
                    alert('該郵箱已經註冊')
                }
            }else {
                window.location.href = '/user/signup_success/';
                // window.location.href = '/';
            }
        }
    });
});
