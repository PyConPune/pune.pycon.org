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
            var ticket_id = id.replace("ticket-row-1-", "");
            $('#id_ticket').val(ticket_id);
            $('html, body').animate({
                scrollTop: $("#ticket-row-2").offset().top - 70
            }, 1000);
        });

        $('input[name=email]').addClass('form-control');

        $('#id_ticket').hide();

        $('.a-ticket select').change(function(event) {
            if ($('#ticket-row-1').find('.ticket-disabled').length == 0) {
                $('html, body').animate({
                    scrollTop: $("#ticket").offset().top
                }, 1000);
                return;
            }

            $this = $(this);
            $this.parent().find('.fa-check').removeClass('hidden');
        });

        $('.a-ticket').click(function(event) {
            if ($('#ticket-row-1').find('.ticket-disabled').length == 0) {
                $('html, body').animate({
                    scrollTop: $("#ticket").offset().top
                }, 1000);
                return;
            }

            $this = $(this);
            var card_type = $this.data('type');

            if($(event.target).is('select')) {
                event.preventDefault();
                return;
            }

            if ($(this).find('.fa-check').hasClass('hidden')) {
                if (card_type == 'dinner') {
                    $this.find('.fa-check').removeClass('hidden');
                };
            } else {
                $this.find('.fa-check').addClass('hidden');
            }
        });
    });