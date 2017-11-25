var base_url = "http://baike.baidu.com/api/openapi/BaikeLemmaCardApi?scope=103&format=json&appid=379020&" 
var getInfo =function(keyword){
    url = base_url + keyword
    $.ajax({
       url: url,
       type: "GET",
       dataType : "jsonp",
       jsonp: "callback",
   })
     .done(function( json ) {
        $("#info").empty()
        $( "<h1 class='text-center'>" ).text( json.title ).appendTo( "#info" );
        $( "<h3>" ).text( json.abstract ).appendTo( "#info" );
     })
     .fail(function( xhr, status, errorThrown ) {
       alert( "Sorry, there was a problem!" );
       console.log( "Error: " + errorThrown );
       console.log( "Status: " + status );
       console.dir( xhr );
     })
     .always(function( xhr, status ) {
       console.log( "The request is complete!" );
     });

}
$( document ).ready(function() {
    $("#searchForm").submit(function(event){
        event.preventDefault();
        var query = $( "#searchForm" ).serialize();
        console.log(query)
        getInfo(query)
    }
    )
});

