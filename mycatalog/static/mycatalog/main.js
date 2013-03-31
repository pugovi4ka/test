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
                form.html(response.form);

                form.find('.alert').remove();
                form.find('input[type="submit"]').parent()
                    .after('<div class="alert alert-success">' + response.message + '</div>');
            } else {
                form.html(response);
            }
        }
    });
});