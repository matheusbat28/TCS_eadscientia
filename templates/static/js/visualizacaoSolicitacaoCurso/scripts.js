$(document).ready(function () {
    $('#cpf-input').mask('000.000.000-00');
    $('.carregando').hide();

    $('#formulario').submit(function (e) {
        var activeElement = $(document.activeElement);

        if (activeElement.attr('id') === 'btnAprovar' || activeElement.attr('id') === 'btnRecusar') {
            // Desativa todos os botões de aprovar/recusar
            $('#btnAprovar, #btnRecusar').prop('disabled', true);

            // Mostra a animação de carregamento
            if (activeElement.attr('id') === 'btnAprovar') {
                $('#carregando-aprovar').show();
                $('#texto-aprovar').hide();
            } else if (activeElement.attr('id') === 'btnRecusar') {
                $('#carregando-recusar').show();
                $('#texto-recusar').hide();
            }
        }
    });
});



$(window).on('load', function () {
    $('#carregando-aprovar').hide();
    $('#texto-aprovar').show();
    $('#carregando-recusar').hide();
    $('#texto-recusar').show();
});

$(window).on('unload', function () {
    $('#carregando-aprovar').hide();
    $('#texto-aprovar').show();
    $('#carregando-recusar').hide();
    $('#texto-recusar').show();
});