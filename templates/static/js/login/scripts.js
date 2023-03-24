$(document).ready(function () {
    $('#matricula').mask('0000000000');

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

});