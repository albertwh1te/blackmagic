//house VM
var placeHolderImg="";//'/static/commons/images/placeholder.png'
var houseAddForm = new Vue({
    el: '#house-add-form',
    data: {
            address:'',
            startDate:'',
            houseType:'',
            rent:'',
            deposit:'',
            furniture:'',
            pet:'',
            laundry:'',
            parking:'',
            utilities:'',
            photos:'/static/commons/images/placeholder.png',
            distanceToSupermarket:'',
            distanceToCampus:[$.extend(true, {}, {
                campus:'',
                distance:'',
            }
                                      )],
    },
    methods:{
        addDistance:function(){
            this.distanceToCampus.push($.extend(true, {}, {
    campus:'',
    distance:'',
}));
        },
        delDistance:function(){
            if (this.distanceToCampus.length>1){
                this.distanceToCampus.pop();
            }
        }
    }
})

var houseSummary = new Vue({
    el:'#house-summary',
    data:{
        photos:'/static/commons/images/placeholder.png',
    },
    methods:{
    
}
})

var roomAddForm= new Vue({
    el: '#room-add-form',
    data:{
        roomType:'',
        startDate:'',
        rent:'',
        deposit:'',
        bathType:'',
        furniture:'',
        capacity:'',
        vacancy:'',
        gender:'',
        leaseTerm:'',
        photos:'/static/commons/images/placeholder.png',
    },
    methods:{
        
    }
})

var roomItem= new Vue({
    el: '#room-item',
    data:{
        rent:600,
        photos:'/static/commons/images/placeholder.png',
        roomType:'主卧',
        nApplicants:'4',
        capacity:'1',
        status:'N'
    },
    methods:{
        stateChange:function(){
            if (this.status!='Y'){
                this.status="Y"
            }else{
                this.status="N";
            }
        },
    }
})
