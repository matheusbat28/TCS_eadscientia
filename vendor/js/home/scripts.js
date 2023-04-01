$(document).ready(function () {

    function horario() {
        var data = new Date();
        var hora = data.getHours();
        var minuto = data.getMinutes();

        if (hora < 10) {
            hora = "0" + hora;
        }
        if (minuto < 10) {
            minuto = "0" + minuto;
        }

        var horario = hora + ":" + minuto
        $("time").html(horario);
    }

    horario();
    setInterval(horario, 1000);
});