// basic demo

// $(document).ready(function(){
$(function(){
    // document.append("Hello, World!");
    $('p').click(function(){
        // alert('heello');
        console.log('this is a test');
        // document.write("hi");
        $(this).hide();
    });
});

// event on bind demo with css manipulations
$(function(){
    $('a').on('mouseenter',function(){
        $('a').css('color','red');
    });
    $('a').on('mouseleave',function(){
        $('a').css('color','green');
    });
});

// animate test
$(function(){
    $(".animate_test").on('click',function(){
        $('div').animate(
            {left:'249px',
            opacity: '0.5',
            height: '150px',
            width: '150px'
           }
        );
    });
});
// test callback
$(function(){
    $(".callback_test").on('click',function(){
        $("#hide_test").hide("slow",function(){
            alert('the sentence is gone !');
        });
    });
});



