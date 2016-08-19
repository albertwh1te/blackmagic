
var userInfo= new Vue({
    el: '#user-info',
    data:{
            id: "",
            username: "",
            first_name: "",
            last_name: "",
            userType: "",
            nickName: "",
            gender: "",
            headIcon: "/static/commons/images/head_portrait.jpg",
            major: "",
            interests: "",
            email: "",
            credits: 0,
            verified: "",
            status: 1,
    },
    methods:{
    }
});

userInfo.$http.get('/api/users/profiles/get_current/').then(
                                (response)=>{
                                    userInfo.$data=response.json();
                                    return false;
                                },(response)=>{
                                    alert('您尚未登录，请先登录！');
                                    window.open('/','_self');
                                    return false;
                                });