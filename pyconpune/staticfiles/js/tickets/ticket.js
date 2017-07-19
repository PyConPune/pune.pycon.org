    $(document).ready( function() {
        $('.ticket').click(function() {
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
            })
        })
    });