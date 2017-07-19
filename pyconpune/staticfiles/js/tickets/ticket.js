    $(document).ready( function() {
        $('.p-ticket').click(function() {
            $this = $(this);
            var id = $this.attr('id');
            var children = $this.parent().children()
            children.each( function (i) {
                if ($(this).attr('id') != id) {
                    $(this).addClass('ticket-disabled');
                    $(this).find('.fa-check').addClass('hidden');
                }
                if ($(this).attr('id') === id) {
                    if ($(this).hasClass('ticket-disabled')) {
                        $(this).removeClass('ticket-disabled');
                    }
                    $(this).find('.fa-check').removeClass('hidden');
                }
            });
            $('html, body').animate({
                scrollTop: $("#ticket-row-2").offset().top - 70
            }, 1000);
        });

        $('.a-ticket').click(function() {
            $this = $(this);
            if ($(this).find('.fa-check').hasClass('hidden')) {
                $this.find('.fa-check').removeClass('hidden');
            } else {
                $this.find('.fa-check').addClass('hidden');
            }
        })
    });