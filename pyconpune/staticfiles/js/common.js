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

    /* Show Buy Tickets button in header when header overlaps
    Buy Tickets button in hero-container in desktops and tablets (Start) */
	var menuBuyTickets = $('.nav-menu .buy-tickets-btn').parent();
    if(mobileMenuBtn.is(':visible')) {
		// Always show Buy Tickets button in mobile sidebar
		menuBuyTickets.removeClass('hide');
    } else {
		$(window).on('scroll', function() {
		    if($(this).scrollTop() >= $('.hero-container .buy-tickets-btn').offset().top){
		        menuBuyTickets.removeClass('hide');
		    } else {
				menuBuyTickets.addClass('hide');
		    }
		});
    }
    /* Show Buy Tickets button in header when header overlaps
    Buy Tickets button in hero-container in desktops and tablets (End) */
});