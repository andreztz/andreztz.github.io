// $.noConflict();
// jQuery.(document).ready(function() {
//
// });


var main = function() {
    $("img").addClass("img-responsive");
    $("div[class='youtube']").addClass('embed-responsive embed-responsive-16by9');
    $('iframe').addClass("embed-responsive-item");
    $("pre").css('border-radius', '0');
    $(".btn-burguer").on('click', function() {
        $(this).toggleClass("active");
        $(".dropdown").toggleClass("dropdown-active");
    });
}

$(document).ready(main);
