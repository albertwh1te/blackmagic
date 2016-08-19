
  $(document).ready(function() {
var signUpForm = new Vue({
    el: '#signup-form',
    data: {
        formData:{ 
            userType:'',
            nickName:'',
            gender:'',
            headIcon:'',
            major:'',
            interests:'',
            email:'',
            password:'',
            passwordAgain:'',
        },
        errors:{    
            userType:'',
            nickName:'',
            gender:'',
            headIcon:'',
            major:'',
            interests:'',
            email:'',
            password:'',
            passwordAgain:'',
        }
    },
    methods:{
        schoolEmailCheck:function(){
            this.errors.email='';
            this.formData.email=this.formData.email.toLocaleLowerCase();
            if (this.formData.userType=='S'){
                var errMsg='请使用学校的官方邮箱（.edu）!';
                var patt=/.+@.+\.edu(?!\w).*/g;
                var result=patt.test(this.formData.email);
            }else{
                var errMsg='请使用有效的邮箱(避免使用gmail和QQ邮箱)!';
                var patt=/.+@.+\..*/g;
                var result=patt.test(this.formData.email);
                if (result){
                patt=/.+@(gmail||qq).com/g;
                result=! patt.test(this.formData.email);
                };
            };
            if (result){
                this.errors.email=this.errors.email.replace(RegExp(errMsg,'g'),'');
            }else{
                if (! this.errors.email.match(errMsg)){
                    this.errors.email+=errMsg;
                };
            };
            return false;
        },
        emptyCheck:function(){
            var errMsg="此处不能为空！";
            for (x in this.formData){
                if ((! this.formData[x]) && (! this.errors[x].match(errMsg)) ){
                    this.errors[x]+=errMsg;
                }else{
                    this.errors[x]=this.errors[x].replace(RegExp(errMsg,'g'),'');
                };
            };
            return false;
        },
        equalCheck:function(){
            var errMsg="两次输入密码不一致！"
            if (this.formData.password != this.formData.passwordAgain){
                if (! this.errors.passwordAgain.match(errMsg)){
                    this.errors.passwordAgain+=errMsg; 
                }
                return false;
            }else{
                this.errors.passwordAgain=this.errors.passwordAgain.replace(RegExp(errMsg,'g'),'');
                return true;
            }
        },
        signUp:function(){
            this.schoolEmailCheck();
            this.emptyCheck();
            var verified=true;
            for (err in this.errors){
                if (this.errors[err]){
                    verified=false;
                    break;
                }
            }
            if (verified){
                window.location.href="/users/signup-success.html"; 
                return false;
            }
            return false;
        },
    },
});


      function equalCheck (formData, jqForm, options){
            var errMsg="两次输入密码不一致！"
            var form=jqForm[0];
            if (form.password.value != form.passwordAgain.value){
                    signUpForm.$data.errors.passwordAgain=errMsg; 
                return false;
            }
        }

       
            var options={
                //data: signUpForm.$data.formData,
                beforeSubmit:equalCheck,
                success: function(data) { // data 保存提交后返回的数据，一般为 json 数据
                    // 此处可对 data 作相关处理
                    signUpForm.$data.errors=data;
                    if (data['success']==true){
                        window.open('/users/signup-success.html','_self')
                    }
                }
            };
            // bind 'myForm' and provide a simple callback function 
            $('#signup-form').ajaxForm(options); 
        }); 

                // inside event callbacks 'this' is the DOM element so we first 
                // wrap it in a jQuery object and then invoke ajaxSubmit 


            function getFileUrl(sourceId) {  
                var url;  
                if (navigator.userAgent.indexOf("MSIE")>=1) { // IE  
                    url = document.getElementById(sourceId).value;  
                } else if(navigator.userAgent.indexOf("Firefox")>0) { // Firefox  
                    url = window.URL.createObjectURL(document.getElementById(sourceId).files.item(0));  
                } else if(navigator.userAgent.indexOf("Chrome")>0) { // Chrome  
                    url = window.URL.createObjectURL(document.getElementById(sourceId).files.item(0));  
                }  
                return url;  
            }  
            function preImg(sourceId, targetId) {   
                var url = getFileUrl(sourceId);   
                var imgPre = document.getElementById(targetId);   
                imgPre.src = url;   
            }   