$(function () {

   $(document).ready(function() {
   $('.slider').slick({
      arrows: true,
      dots: true,
      slidesToShow: 3,
      slidesToScroll: 1,
      speed: 1200,
      autoplay: true,
      autoplaySpeed:2000

   });
})

if ($(document).width() <= 425) {
    $('.slider').slick({
        arrows: false,
        dots: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        speed: 1200,
        autoplay: true,
        autoplaySpeed:1700
    })
} else {
     $('.slider').slick({
        arrows: true,
        dots: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        speed: 1200,
        autoplay: true,
        autoplaySpeed:2000
    })
}


$(".up-btn").on("click", function () {
   $("html, body").animate({
      scrollTop: 0,
   }, "slow");
})

AOS.init({
   disable: false, // accepts following values: 'phone', 'tablet', 'mobile', boolean, expression or function
   startEvent: 'DOMContentLoaded', // name of the event dispatched on the document, that AOS should initialize on
   initClassName: 'aos-init', // class applied after initialization
   animatedClassName: 'aos-animate', // class applied on animation
   useClassNames: false, // if true, will add content of `data-aos` as classes on scroll
   disableMutationObserver: false, // disables automatic mutations' detections (advanced)
   debounceDelay: 50, // the delay on debounce used while resizing window (advanced)
   throttleDelay: 99, // the delay on throttle used while scrolling the page (advanced)


   // Settings that can be overridden on per-element basis, by `data-aos-*` attributes:
   offset: 100, // offset (in px) from the original trigger point
   delay: 0, // values from 0 to 3000, with step 50ms
   duration: 800, // values from 0 to 3000, with step 50ms
   easing: 'ease', // default easing for AOS animations
   once: false, // whether animation should happen only once - while scrolling down
   mirror: false, // whether elements should animate out while scrolling past them
   anchorPlacement: 'top-bottom', // defines which position of the element regarding to window should trigger the animation
});

    var header = $('#header'),
        innerH = $('#intro').innerHeight(),
        scrollOfset = $(window).scrollTop();

    //Header

    checkScroll(scrollOfset)

    $(window).on('scroll', function () {

        scrollOfset = $(this).scrollTop();

        checkScroll(scrollOfset)


    })

    function checkScroll(scrollOfset) {

        if( scrollOfset >= innerH ) {
            header.addClass('header-fixed');
        } else {
            header.removeClass('header-fixed');
        }

    }

    //Smooth Scroll

    $('[data-scroll]').on('click', function(event) {
        event.preventDefault();

        var blockId = $(this).data('scroll'),
            blockOffset =  $(blockId).offset().top;

        $('html, body').animate({
            scrollTop: blockOffset
        }, 500);
    });







    //Menu nav toggle


    $('#nav_toggle').on('click', function (event) {
        event.preventDefault();


        $(this).toggleClass('active')
        $('#nav').toggleClass('active')
        $('#header').toggleClass('active')
    })


});
