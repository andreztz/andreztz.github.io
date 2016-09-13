// $.noConflict();
// jQuery.(document).ready(function() {
//
// });


var main = function() {
    $("img").addClass("img-responsive");
    $("pre").css('border-radius', '0');
    $(".btn-burguer").on('click', function() {
        $(this).toggleClass("active");
        $(".dropdown").toggleClass("dropdown-active");
    });
}

$(document).ready(main);
