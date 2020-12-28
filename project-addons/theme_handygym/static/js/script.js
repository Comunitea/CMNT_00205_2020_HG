$(document).ready(function(){
    $(".s_website_form").validate({
        rules: {
            email_from: {
            required: true,
            email: true
            },
            phone: {
                required: true,
            }
        },
        messages: {
            email_from: {
                required: 'Este campo es obligatorio',
                email: 'Por favor, introduce una dirección de correo electrónico válida'
            },
            phone: {
                required: 'Este campo es obligatorio'
            }
        }
    });

    /* Scroll to revi widget on product rating stars click */
    $('.wp_stars_product_page').on('click', function(){
        var to_scroll = $('.wp_revi_widget_product').offset().top
        $('html, body').animate({ scrollTop: to_scroll - 150}, 700);
    });
});
