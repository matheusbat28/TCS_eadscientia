$(document).ready(function () {
    $('#matricula').mask('0000000000');

    $("#olho-senha").mousedown(function () {
        $("#senha").attr("type", "text");
    });

    $("#olho-senha").mouseup(function () {
        $("#senha").attr("type", "password");
    });

});