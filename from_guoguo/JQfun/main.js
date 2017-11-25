window.onload = function () { $("a").addClass("test");
    $("a").click(function (event) {
        var elm = $(this)
        alert("Thanks for visiting!");
        elm.removeClass("test");
    })
};
$("b").click(function (event) {
    event.preventDefault()
    $(this).hide("slow")
})
$( document ).ready(function() {
    console.log( "document loaded" );
});
$( window ).on( "load", function() {
    console.log( "window loading" );
});
$("c").attr({
    "href":"https://www.zhihu.com/",
    "title":"sdd"
}
).html("<h1>this is good</h1>")
var myNewElement = $( "<p>New element</p>" );
myNewElement.insertAfter( "c" ); // This will remove the p from #content!
var myItems = [];
var myList = $( "#myList" );
 
for ( var i = 0; i < 15; i++ ) {
    myItems.push( "<li>item " + i + "</li>" );
}
myList.append( myItems.join( "" ) );
$("li").eq(1).addClass("demo")
var tt = $.trim( "    <div>lots of extra whitespace</div>    " );
$( "div.surrogateParent1" ).siblings().html(tt).css("color","green").width("20px");
$.each([ "foo", "bar", "baz" ], function( idx, val ) {
    document.writeln( "element " + idx + " is " + val );
});
 
$.each({ foo: "bar", baz: "bim" }, function( k, v ) {
    document.writeln( k + " : " + v );
});
$( "div" ).on({
    mouseenter: function() {
        console.log( "hovered over a div" );
    },
    mouseleave: function() {
        console.log( "mouse left a div" );
    }
    // ,click: function() {
        // console.log( "clicked on a div" );
    // }
});
$( "div" ).on( "click", {
    foo:"bar"
},function( event ) {
    console.log( "event object:" );
    console.dir( event );
    console.log( event.data.foo );
})

$( "p" ).on( "click", {
    foo: "bar"
}, function( event ) {
    console.log( "event data: " + event.data.foo + " (should be 'bar')" );
});
$("p").off("click",{
    foo: "bar"
}, function( event ) {
    console.log( "event data: " + event.data.foo + " (should be 'bar')" );
});

api_url = "http://baike.baidu.com/api/openapi/BaikeLemmaCardApi?scope=103&format=json&appid=379020&bk_key=tom"
base_url = "http://baike.baidu.com/api/openapi/BaikeLemmaCardApi?scope=103&format=json&appid=379020&"
var getInfo =function(keyword){
    url = base_url + keyword
    console.log(url)
    $.ajax({
    
       // The URL for the request
       url: url,
    
       // The data to send (will be converted to a query string)
       data: {
           id: 123
       },
    
       // Whether this is a POST or GET request
       type: "GET",
       // The type of data we expect back
       dataType : "jsonp",
       jsonp: "callback",

   })
     // Code to run if the request succeeds (is done);
     // The response is passed to the function
     .done(function( json ) {
        $( "<h1>" ).text( json.title ).appendTo( "body" );
        // $( "<div class=\"content\">").html( json.html ).appendTo( "body" );
     })
     // Code to run if the request fails; the raw request and
     // status codes are passed to the function
     .fail(function( xhr, status, errorThrown ) {
       alert( "Sorry, there was a problem!" );
       console.log( "Error: " + errorThrown );
       console.log( "Status: " + status );
       console.dir( xhr );
     })
     // Code to run regardless of success or failure;
     .always(function( xhr, status ) {
       alert( "The request is complete!" );
     });

}
// Using the core $.ajax() method
$.ajax({
    
       // The URL for the request
       url: api_url,
    
       // The data to send (will be converted to a query string)
       data: {
           id: 123
       },
    
       // Whether this is a POST or GET request
       type: "GET",
       // The type of data we expect back
       dataType : "jsonp",
       jsonp: "callback",

   })
     // Code to run if the request succeeds (is done);
     // The response is passed to the function
     .done(function( json ) {
         console.log(json.abstract)
        $( "<h1>" ).text( json.title ).appendTo( "body" );
        $( "<h2>" ).text( json.abstract ).appendTo( "body" );
        // $( "<div class=\"content\">").html( json.html ).appendTo( "body" );
     })
     // Code to run if the request fails; the raw request and
     // status codes are passed to the function
     .fail(function( xhr, status, errorThrown ) {
       alert( "Sorry, there was a problem!" );
       console.log( "Error: " + errorThrown );
       console.log( "Status: " + status );
       console.dir( xhr );
     })
     // Code to run regardless of success or failure;
     .always(function( xhr, status ) {
       alert( "The request is complete!" );
     });

$("#myForm").submit(function(event){
    event.preventDefault();
    var info = $( "#myForm" ).serialize();
    console.log(info)
    getInfo(info)
}
)