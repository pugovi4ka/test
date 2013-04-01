$(document).ready(function() {
    // bind 'myForm' and provide a simple callback function
    var form = $('#product-edit-form');
    var inputs = form.find('input, textarea, file');
    form.ajaxForm({
        beforeSubmit: function(){
            inputs.prop('disabled', true);
            form.addClass('loading');
        },
        success: function(response){
            inputs.prop('disabled', false);
            form.removeClass('loading');

            if (response.message) {
                form.html(
                    '<div class="alert alert-success">' + response.message +
                        '<a href="' + response.edit_link + '">Edit product again</a> or ' +
                        '<a href="' + response.product_link + '">show product</a>' +
                    '</div>');
            } else {
                form.html(response);
            }
        }
    });
});