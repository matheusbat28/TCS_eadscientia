$(document).ready(function () {
    $('#matricula').mask('0000000000');
    $('.carregando').hide();


    $("#olho-senha").mousedown(function () {
        $("#senha").attr("type", "text");
    });

    $("#olho-senha").mouseup(function () {
        $("#senha").attr("type", "password");
    });

    $('#esqueci-senha').click(function () {
        if ($('#cbx_modal').is(':checked')) {
            $('#modal').removeClass('modal-mostrar');
            $('#modal').addClass('modal-sair');
        } else {
            $('#modal').removeClass('modal-sair');
            $('#modal').addClass('modal-mostrar');
        }
    });

    $('#modal-x label').click(function () {
        $('#modal').removeClass('modal-mostrar');
        $('#modal').addClass('modal-sair');
    });

    $('#btn-entrar').click(function (e) {
        $('#texto-log').hide();
        $('#carregando-log').show();

    });

    $('#btn-recuperar-senha').click(function (e) {
        $('#btn-recuperar-senha i').hide();
        $('#carregando-senha').show();

    });

});

$(window).on('load', function () {
    $('#texto-log').show();
    $('#carregando-log').hide();
    $('#btn-recuperar-senha i').show();
    $('#carregando-senha').hide();
});

$(window).on('unload', function () {
    $('#texto-log').show();
    $('#carregando-log').hide();
    $('#btn-recuperar-senha i').show();
    $('#carregando-senha').hide();
});
