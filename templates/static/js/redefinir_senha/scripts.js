$(document).ready(function () {
    $('.carregando').hide();

    $('#btn-cad-vef-senha').click(function () {
        $('#carregando-vef').show();
        $('#texto-vef').hide();
    }
    );
});

$(window).on('load', function () {
    $('#carregando-vef').hide();
    $('#texto-vef').show();
});

$(window).on('unload', function () {
    $('#carregando-vef').hide();
    $('#texto-vef').show();
});