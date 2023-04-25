$(document).ready(function () {
    $('#cpf-input').mask('000.000.000-00');
    $('.carregando').hide();

    $('#formulario').submit(function (e) {
        $('#carregando-formulario').show();
        $('#texto-formulario ').hide();

    });


});

$(window).on('load', function () {
    $('#carregando-formulario').hide();
    $('#texto-formulario ').show();
});

$(window).on('unload', function () {
    $('#carregando-formulario').hide();
    $('#texto-formulario ').show();
});