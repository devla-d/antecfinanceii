'use strict';
(function($) {


    $(document).ready(
        function() {




            $('.set-bg').each(function() {
                var img = $(this).data('bg');
                $(this).css('background-image', `url(${img})`)
            })


            /* ----------------------------------------------------------- */
            /* Header Scroll
            /* ----------------------------------------------------------- */
            $(window).scroll(function() {
                if ($(this).scrollTop() > 100) {
                    $('.topbar-two').addClass("scroll"), 1000;
                    $('#topbar nav').addClass("scroll"), 1000;
                } else {
                    $('.topbar-two').removeClass("scroll"), 1000;
                    $('#topbar nav').removeClass("scroll"), 1000;
                }
            });

            var is_sidebar_open = false
            $('.hamburger').on('click', function() {

                is_sidebar_open = true
                $('.dismiss').addClass('active');
                $('.sidebar').addClass('active');

            })

            $('.dismiss').on('click', function() {

                is_sidebar_open = false
                $('.dismiss').removeClass('active');
                $('.sidebar').removeClass('active');

            })







        }
    )







})(jQuery);