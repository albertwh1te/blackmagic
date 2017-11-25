top250url = "https://api.douban.com/v2/movie/top250"

Vue.component('todo-item', {
    props: ['todo'],
    template: '<h2>{{ todo.title }}</h2>',
  })

var recentMovies ={
  template: '<el-tabel data:></el-tabel>'
}

var app = new Vue({
    el: '#app',
//     data: {
//       groceryList: [
//         { id: 0, text: 'Vegetables' },
//         { id: 1, text: 'Cheese' },
//         { id: 2, text: 'Whatever else humans are supposed to eat' }
//       ]
//     }
    data:{
      movies:[],
      visible: false
    },
    created(){
      $.ajax({
       // The URL for the request
       url: top250url,
    
       // The data to send (will be converted to a query string)
       data: {
           count:20
       },
    
       // Whether this is a POST or GET request
       type: "GET",
       // The type of data we expect back
       dataType : "jsonp",
       jsonp: "callback",

   })
     // Code to run if the request succeeds (is done);
     // The response is passed to the function
     .done(json  => { 
       console.log(json);
       console.log(this);
       this.movies = json.subjects;
        // $( "<div class=\"content\">").html( json.html ).appendTo( "body" );
     })
     // Code to run if the request fails; the raw request and
     // status codes are passed to the function
     .fail(function( xhr, status, errorThrown ) {
       console.log( "Error: " + errorThrown );
       console.log( "Status: " + status );
       console.dir( xhr );
     })
     // Code to run regardless of success or failure;
     .always(function( xhr, status ) {
      //  alert( "The request is complete!" );
    })
  }
})