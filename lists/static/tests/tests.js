var initialize = function () {
    //$('.has-error').show() // the example doesn't have this line
    $('input[name="text"]').on('keypress', function () {
        $('.has-error').hide();
    });
};
