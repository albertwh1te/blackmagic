var loginForm= new Vue({
    el: '#login-form',
    data:{
        email:'',
        password:'',
    },
    methods:{
        login: function(){
            Vue.http.headers.common['X-CSRFToken'] = Cookies.get('csrftoken');
            Vue.http.post('/api/users/users/login/',this.$data).then(
                                (response)=>{
                                    window.open('/houses/home-rent.html','_self');
                                    return false;
                                },(response)=>{
                                    alert('错误：没有匹配的注册信息！');
                                    return false;
                                });
                         },
                         },
})

