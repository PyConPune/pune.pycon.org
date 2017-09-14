$(document).ready(function () {
    var mobileMenuBtn = $('.mobile-menu-btn');
    /* Mobile menu sidebar hide/show (Start) */
    var bodyObject = $('body');
    if(mobileMenuBtn.is(':visible')) {
        function toggleMobileSidebar() {
            mobileMenuBtn.toggleClass('close-icon');
            bodyObject.toggleClass('slide-right').toggleClass('no-scroll');
        }
        mobileMenuBtn.on('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            toggleMobileSidebar();
        });
    }
    /* Mobile menu sidebar hide/show (End) */

    // handle links with @href started with '#' only
    $(document).on('click', 'a', function(e) {
        // target element id
        var href = $(this).attr('href');
        var split_array = href.split('/');
        if (!split_array[split_array.length - 1].startsWith('#')) {
            return;
        }
        var id = split_array[split_array.length - 1];

        console.log(id);
        // target element
        var $id = $(id);
        if ($id.length === 0) {
            return;
        }

        // prevent standard hash navigation (avoid blinking in IE)
        e.preventDefault();

        // top position relative to the document
        var pos = $id.offset().top;

        // animated top scrolling
        $('body, html').animate({scrollTop: pos});
    });

    /* Show Buy Tickets button in header when header overlaps
    Buy Tickets button in hero-container in desktops and tablets (Start) */
//	var menuBuyTickets = $('.nav-menu .buy-tickets-btn').parent();
//    if(mobileMenuBtn.is(':visible')) {
//		// Always show Buy Tickets button in mobile sidebar
//		// Commented till ticket registration starts
//		// menuBuyTickets.removeClass('hide');
//    } else {
//		$(window).on('scroll', function() {
//		    if($(this).scrollTop() >= $('.hero-container .buy-tickets-btn').offset().top){
//		        menuBuyTickets.removeClass('hide');
//		    } else {
//				menuBuyTickets.addClass('hide');
//		    }
//		});
//    }
    /* Show Buy Tickets button in header when header overlaps
    Buy Tickets button in hero-container in desktops and tablets (End) */
});