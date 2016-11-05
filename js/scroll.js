
jQuery(document).ready(function(){

var navOffset = $(topNav);
    if (!navOffset.length) {
        return;
    }
    offSet = navOffset.offset().top;

//console.log(offSet);

	$(topNav).wrap('<div class="navpalceholder"></div>');
	$(".navpalceholder").height($(topNav).outerHeight());

	$(topNav).wrapInner('<div class="navinner"></div>');


jQuery(window).scroll(function(){

	var scrollpos = jQuery(window).scrollTop();

	//console.log(scrollpos);

	if (scrollpos >= offSet) {
		$(topNav).addClass("fixed");
		} else{
		$(topNav).removeClass("fixed");

		}
});

});

