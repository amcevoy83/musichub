$(document).ready(function(){
$(function(){
    $("#register-form").submit(function(){
        var form = this;

        //collect form details and store them in this card variable
        var card = {
            number:     $("#id_credit_card_number").val(),
            expMonth:   $("#id_expiry_month").val(),
            expYear:    $("#id_expiry_year").val(),
            cvc:        $('#id_cvv').val()
        };

    //disable the button so that it isn't triggered again whilst waiting for Stripe to assign us our token'
    $("#validate_card_btn").attr("disabled",true);

    Stripe.createToken(card,function(status, response){
        //200 means the status is successful
        $("#div_id_credit_card_number label").text('Credit card number');

        if (status === 200){
            console.log(status, response);
            //hide any previous errors that may have been shown
            $("credit-card-errors").hide();
            //add the stripe token to the stripe_id field so that it can be posted back tot he server(and stored in our models class
            $("#id_stripe_id").val(response.id);


            form.submit();
        }
        else {
            $("#stripe-error-message").text(response.error.message);
            if (response.error.message == "Your card's security code is invalid.") {
                $("#div_id_cvv label").text(response.error.message);
            }
            if (response.error.message == "Your card number is incorrect.") {
                $("#div_id_credit_card_number label").text(response.error.message);
            }
            $("#credit-card-errors").show();
            $("#validate_card_btn").attr("disabled", false);
            }
        });
        return false;

    });

});

});