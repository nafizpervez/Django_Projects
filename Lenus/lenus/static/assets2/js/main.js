(function ($) {
    "use strict";
    
    new WOW().init();  
    
    
    /*---background image---*/
	function dataBackgroundImage() {
		$('[data-bgimg]').each(function () {
			var bgImgUrl = $(this).data('bgimg');
			$(this).css({
				'background-image': 'url(' + bgImgUrl + ')', // + meaning concat
			});
		});
    }
    
    
    $(window).on('load', function () {
        dataBackgroundImage();
    });
    

    /*swiper container activation*/
    var swiper = new Swiper('.works_swiper', {
        slidesPerView: 2,
        clickable: true,
        spaceBetween: 75,
        breakpoints: {
            1366: {
                spaceBetween: 75,
                
              },
            1200: {
                spaceBetween: 50,
                
            },
            992: {
                spaceBetween: 30,
                
            },
            768: {
              slidesPerView: 2,
              spaceBetween: 30,
              
            },
            576: {
              slidesPerView: 2,
              spaceBetween: 30,
            },
            320: {
                slidesPerView: 1,
              },
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
    });
    
    /*swiper container activation*/
    $(document).ready(function() {
        var $slider = $('.portfolio_slick_slider');
        var $progressBar = $('.progress');
        var $progressBarLabel = $( '.slider__label' );
        
        $slider.on('beforeChange', function(event, slick, currentSlide, nextSlide) {   
          var calc = ( (nextSlide) / (slick.slideCount-1) ) * 100;
          $progressBar
            .css('background-size', calc + '% 100%')
            .attr('aria-valuenow', calc );
          
          $progressBarLabel.text( calc + '% completed' );
        });
        
        $slider.slick({
          slidesToShow: 1,
          slidesToScroll: 1,
          centerMode: true,
          speed: 400
          
        });  
    });




   //Search Box addClass removeClass
   $('.header_search_btn > a').on('click', function(){
    $('.page_search_box').addClass('active')
    });
    $('.search_close > i').on('click', function(){
        $('.page_search_box').removeClass('active')
    });




    /*--- Magnific Popup Video---*/
    $('.video_popup').magnificPopup({
        type: 'iframe',
        gallery: {
            enabled: true
        }
    });

    $('.img_popup').magnificPopup({
        type: 'image',
        gallery: {
            enabled: true
        }
    });


    /*--- counterup activation ---*/
    $('.counterup').counterUp({
        delay: 20,
        time: 1000
    });
    
    
    $('.select_option').niceSelect();
 
    
      /*---  ScrollUp Active ---*/
      $.scrollUp({
        scrollText: '<i class="ion-android-arrow-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    });
    
    
       /*----------  Scroll to top  ----------*/
       function scrollToTop() {
        var $scrollUp = $('#scroll-top'),
            $lastScrollTop = 0,
            $window = $(window);

        $window.on('scroll', function () {
            var st = $(this).scrollTop();
           
            $lastScrollTop = st;
        });

        $scrollUp.on('click', function (evt) {
            $('html, body').animate({scrollTop: 0}, 600);
            evt.preventDefault();
        });
    }
    scrollToTop();

    

    /*---canvas menu activation---*/
    $('.canvas_open').on('click', function(){
        $('.offcanvas_menu_wrapper,.body_overlay').addClass('active')
    });
    
    $('.canvas_close,.body_overlay').on('click', function(){
        $('.offcanvas_menu_wrapper,.body_overlay').removeClass('active')
    });
    /*---Off Canvas Menu---*/
    var $offcanvasNav = $('.offcanvas_main_menu'),
        $offcanvasNavSubMenu = $offcanvasNav.find('.sub-menu');
    $offcanvasNavSubMenu.parent().prepend('<span class="menu-expand"><i class="fa fa-angle-down"></i></span>');
    
    $offcanvasNavSubMenu.slideUp();
    
    $offcanvasNav.on('click', 'li a, li .menu-expand', function(e) {
        var $this = $(this);
        if ( ($this.parent().attr('class').match(/\b(menu-item-has-children|has-children|has-sub-menu)\b/)) && ($this.attr('href') === '#' || $this.hasClass('menu-expand')) ) {
            e.preventDefault();
            if ($this.siblings('ul:visible').length){
                $this.siblings('ul').slideUp('slow');
            }else {
                $this.closest('li').siblings('li').find('ul:visible').slideUp('slow');
                $this.siblings('ul').slideDown('slow');
            }
        }
        if( $this.is('a') || $this.is('span') || $this.attr('clas').match(/\b(menu-expand)\b/) ){
        	$this.parent().toggleClass('menu-open');
        }else if( $this.is('li') && $this.attr('class').match(/\b('menu-item-has-children')\b/) ){
        	$this.toggleClass('menu-open');
        }
    });

   
  /*blog Isotope activation*/
  $('.portfolio_page_gallery').imagesLoaded( function() {
    // init Isotope
    var $grid = $('.portfolio_page_gallery').isotope({
       itemSelector: '.gird_item',
        percentPosition: true,
        masonry: {
            columnWidth: '.gird_item'
        }
    });
        
    // filter items on button click
    $('.portfolio_messonry_button').on( 'click', 'button', function() {
       var filterValue = $(this).attr('data-filter');
       $grid.isotope({ filter: filterValue });
        
       $(this).siblings('.active').removeClass('active');
       $(this).addClass('active');
    });
   
});


    
    
    /*---MailChimp---*/
    $('#mc-form').ajaxChimp({
        language: 'en',
        callback: mailChimpResponse,
        // ADD YOUR MAILCHIMP URL BELOW HERE!
        url: 'http://devitems.us11.list-manage.com/subscribe/post?u=6bbb9b6f5827bd842d9640c82&amp;id=05d85f18ef'

    });
    function mailChimpResponse(resp) {

        if (resp.result === 'success') {
            $('.mailchimp-success').addClass('active')
            $('.mailchimp-success').html('' + resp.msg).fadeIn(900);
            $('.mailchimp-error').fadeOut(400);

        } else if(resp.result === 'error') {
            $('.mailchimp-error').html('' + resp.msg).fadeIn(900);
        }  
    }
 
  
    
    
})(jQuery);	
