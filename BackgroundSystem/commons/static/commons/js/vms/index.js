var loginForm= new Vue({
    el: '#login-form',
    data:{
        username:'',
        password:'',
    },
    methods:{
        login: function(){
            Vue.http.headers.common['X-CSRFToken'] = Cookies.get('csrftoken');
            Vue.http.post('/api_menus/login_api',this.$data).then(
                                (response)=>{
                                    window.open('/api_menus/queries','_self');
                                    return True;
                                },(response)=>{
                                    alert('错误：没有匹配的注册信息！');
                                    return false;
                                });
                         },
                         },
})

