$('.carregando').hide();
$('#fundo_modal').css('display', 'none')

let modalStatus = false;

$(document).ready(function () {
    $('#matricula').mask('0000000000');


    $("#olho-senha").mousedown(function () {
        $("#senha").attr("type", "text");
    });

    $("#olho-senha").mouseup(function () {
        $("#senha").attr("type", "password");
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

$(document).on('click', '#esqueci-senha label, #modal-x', function () {
    $('#fundo_modal').toggleClass('fundo_modal-estilo');
});
