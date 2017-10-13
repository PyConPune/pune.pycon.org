$(document).ready( function() {
    $('.p-ticket').click(function() {
        $this = $(this);
        var id = $this.attr('id');
        var children = $this.parent().children()
        children.each( function (i) {
            if ($(this).attr('id') != id) {
                $(this).addClass('ticket-disabled');
                $(this).find('.ticket-inner').removeClass('active');
            }
            if ($(this).attr('id') === id) {
                if ($(this).hasClass('ticket-disabled')) {
                    $(this).removeClass('ticket-disabled');
                }
                $(this).find('.ticket-inner').addClass('active');
            }
        });
        if (!$('#ticket-row-2').hasClass('show')) {
            $('#ticket-row-2').addClass('show');
        }
        if (!$('#ticket-row-3').hasClass('show')) {
            $('#ticket-row-3').addClass('show');
        }
        var ticket_id = id.replace("ticket-row-1-", "");
        $('#id_ticket').val(ticket_id);
        $('html, body').animate({
            scrollTop: $("#ticket-row-2").offset().top - 70
        }, 1000);
        var ticket_title = $this.find('.ticket-title').html();
        var ticket_price = $this.find('.ticket-price').html();
        var sum = 0;
        $('.payment-breakup-row#conference-ticket .item').html(ticket_title);
        $('.payment-breakup-row#conference-ticket .price').html(ticket_price);
        $('.price').each(function(){
            var price = parseFloat($(this).text().replace('₹','').replace('','0'));
            sum = sum + price;
        });
        var tax = (0.18 * sum);
        var final_sum = (sum + tax);
        $('.payment-breakup-row#total-without-tax .total-price').html('₹' + sum.toFixed(2));
        $('.payment-breakup-row#total-with-tax .total-price').html('₹' + final_sum.toFixed(2));
        $('.payment-breakup-row#tax .tax-price').html('₹' + tax.toFixed(2));
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
        $this.parent().find('.ticket-inner').addClass('active');
        if (card_type == 'tshirt') {
            var tshirt_arr_id = "#tshirt-arr-" + (id - 1);
            var tshirt_id = $this.val();
            $(tshirt_arr_id).val(tshirt_id);
            var ticket_title = 'Tshirt ' + $this.find(':selected').html();
            var ticket_price = $this.parent().find('.ticket-price').html();
            var sum = 0;
            $('.payment-breakup-row#tshirt-ticket-' + (id - 1) + ' .item').html(ticket_title);
            $('.payment-breakup-row#tshirt-ticket-' + (id - 1) + ' .price').html(ticket_price);
            $('.price').each(function(){
                var price = parseFloat($(this).text().replace('₹','').replace('','0'));
                sum = sum + price;
            });
            var tax = (0.18 * sum);
            var final_sum = (sum + tax);
            $('.payment-breakup-row#total-without-tax .total-price').html('₹' + sum.toFixed(2));
            $('.payment-breakup-row#total-with-tax .total-price').html('₹' + final_sum.toFixed(2));
            $('.payment-breakup-row#tax .tax-price').html('₹' + tax.toFixed(2));
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

        if (!$(this).find('.ticket-inner').hasClass('active')) {
            if (card_type == 'dinner') {
                $this.find('.ticket-inner').addClass('active');
                var auxiliary_ticket_id = id;
                $('#id_auxiliary_ticket_id').val(auxiliary_ticket_id);
                var ticket_title = $this.find('.ticket-title').html();
                var ticket_price = $this.find('.ticket-price').html();
                var sum = 0
                $('.payment-breakup-row#auxiliary-ticket .item').html(ticket_title);
                $('.payment-breakup-row#auxiliary-ticket .price').html(ticket_price);
                $('.price').each(function(){
                    var price = parseFloat($(this).text().replace('₹','').replace('','0'));
                    sum = sum + price;
                });
                var tax = (0.18 * sum);
                var final_sum = (sum + tax);
                $('.payment-breakup-row#total-without-tax .total-price').html('₹' + sum.toFixed(2));
                $('.payment-breakup-row#total-with-tax .total-price').html('₹' + final_sum.toFixed(2));
                $('.payment-breakup-row#tax .tax-price').html('₹' + tax.toFixed(2));
            };
        } else {
            $this.find('.ticket-inner').removeClass('active');
            $('#id_auxiliary_ticket_id').val(0);
            $('.payment-breakup-row#auxiliary-ticket .item').html('');
            $('.payment-breakup-row#auxiliary-ticket .price').html('');
            var sum = 0;
            $('.price').each(function(){
                var price = parseFloat($(this).text().replace('₹','').replace('','0'));
                sum = sum + price;
            });
            var tax = (0.18 * sum);
            var final_sum = (sum + tax);
            $('.payment-breakup-row#total-without-tax .total-price').html('₹' + sum.toFixed(2));
            $('.payment-breakup-row#total-with-tax .total-price').html('₹' + final_sum.toFixed(2));
            $('.payment-breakup-row#tax .tax-price').html('₹' + tax.toFixed(2));
        }

        if (!$('#ticket-row-3').hasClass('show')) {
            $('#ticket-row-3').addClass('show');
        }
    });

    if (!$('#ticket-row-1').hasClass('show')) {
        $('#ticket-row-1').addClass('show');
    }

    $('.form-group button[type=submit]').click(function(event){
        event.preventDefault();
        $('#form-invalid').addClass('hidden')
        if (isValidForms()) {
            $('#ticket-register-form').submit();
        }
    });
});

function isValidForms() {
    if ($('#id_ticket option:selected').val() == "") {
        $('#form-invalid').removeClass('hidden').html("You must select a ticket");
        return false;
    }

    if ($('#id_first_name').val() == "") {
        $('#form-invalid').removeClass('hidden').html("You must enter all necessary fields");
        return false;
    }

    if ($('#id_last_name').val() == "") {
        $('#form-invalid').removeClass('hidden').html("You must enter all necessary fields");
        return false;
    }

    if ($('#id_email').val() == "") {
        $('#form-invalid').removeClass('hidden').html("You must enter all necessary fields");
        return false;
    }

    if ($('#id_contact').val() == "") {
        $('#form-invalid').removeClass('hidden').html("You must enter all necessary fields");
        return false;
    }

    if ($('#id_age_group option:selected').val() == "0") {
        $('#form-invalid').removeClass('hidden').html("You must enter all necessary fields");
        return false;
    }

    if ($('#id_occupation option:selected').val() == "Z") {
        $('#form-invalid').removeClass('hidden').html("You must enter all necessary fields");
        return false;
    }

    return true;
}
