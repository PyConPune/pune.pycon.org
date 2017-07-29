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
        $('#id_auxiliary_ticket_id').hide();

        $('.a-ticket select').change(function(event) {
            if ($('#ticket-row-1').find('.ticket-disabled').length == 0) {
                $('html, body').animate({
                    scrollTop: $("#ticket").offset().top
                }, 1000);
                return;
            }

            $this = $(this);
            var card_type = $this.parent().parent().data('type');
            var id = $this.parent().parent().attr('id').replace("ticket-row-2-", "");
            $this.parent().find('.fa-check').removeClass('hidden');
            if (card_type == 'tshirt') {
                var tshirt_arr_id = "#tshirt-arr-" + (id - 1);
                var tshirt_id = $this.val();
                $(tshirt_arr_id).val(tshirt_id);
            }
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
            var id = $this.attr('id').replace("ticket-row-2-", "");

            if($(event.target).is('select')) {
                event.preventDefault();
                return;
            }

            if ($(this).find('.fa-check').hasClass('hidden')) {
                if (card_type == 'dinner') {
                    $this.find('.fa-check').removeClass('hidden');
                    var auxiliary_ticket_id = id;
                    $('#id_auxiliary_ticket_id').val(auxiliary_ticket_id);
                };
            } else {
                $this.find('.fa-check').addClass('hidden');
                $('#id_auxiliary_ticket_id').val(0);
            }
        });

        $('#ticket-register-form').submit(function(event){
            console.log($(this).serialize());
        });
    });