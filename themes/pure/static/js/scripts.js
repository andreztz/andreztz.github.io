$(document).ready(function(){
      updateContainer();
      $(window).on('resize', function(){

            if ($(window).width() < 767 ){
                $("p.social").css({"margin": "1%", "padding-top": "1%"});
                $(".avatar-profile").css({
                                            "width": "100px",
                                            "border-radius": "100px",
                                            "-webkit-border-radius": "100px",
                                            "-moz-border-radius": "100px"
                                            });

            }
            else if ($(window).width() > 768 ){
                updateContainer();
            }
        });

});

function updateContainer(){
    $("p.social").css({"margin": "1%", "padding-top": "50%"});
}