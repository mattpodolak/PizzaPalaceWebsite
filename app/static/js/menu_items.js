$(function() {

      $(".potato").each(function() {
        $(this).wrap('<figure class="tint"></figure>');
      });

    });
function overlay() {
	el = document.getElementById("overlay");
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
}
function overlay2() {
	el = document.getElementById("overlay2");
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
}
function overlay3() {
	el = document.getElementById("overlay3");
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
}
function overlay4() {
	el = document.getElementById("overlay4");
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
}
function overlay5() {
	el = document.getElementById("overlay5");
	el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
}

//stuff I've added
$(".header2").click(function () {

    $header = $(this);
    //getting the next element
    $content = $header.next();
    //open up the content needed - toggle the slide- if visible, slide up, if not slidedown.
    $content.slideToggle(500, function () {
        //execute this after slideToggle is done
        //change text of header based on visibility of content div
        $header.text(function () {
            //change text based on condition
            return $content.is(":visible") ? "Collapse" : "Click to Order";
        });
    });

});

$(window).scroll(function(){
  $("#cart").stop().animate({"marginTop": ($(window).scrollTop()) + 15 +"px", "marginLeft":($(window).scrollLeft()) + "px"}, "slow" );
});

//stuff I've added
$(".header4").click(function () {

    $header = $(this);
    //getting the next element
    $content = $header.next();
    //open up the content needed - toggle the slide- if visible, slide up, if not slidedown.
    $content.slideToggle(500, function () {
        //execute this after slideToggle is done
        //change text of header based on visibility of content div
    });

});

$(document).ready(function(){
        $('.dropdown-toggle').dropdown()
    });