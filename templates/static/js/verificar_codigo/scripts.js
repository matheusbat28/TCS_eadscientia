$(document).ready(function () {
    $('.codigo').mask('0');
    $('.carregando').hide();

    localStorage.setItem('status', true);
    localStorage.setItem('tempo', 60);

    $('time').hide();


    if (sessionStorage.getItem('status') == 'false') {
        $('time').show();
        $('#btn-reenviar-codigo').hide();
        tempo();
        setInterval(tempo, 1000);


    }

    function tempo() {
        var tempo = localStorage.getItem('tempo');
        if (tempo <= 0) {
            localStorage.setItem('tempo', 0);
            $('time').text('00:00');
            $('#btn-reenviar-codigo').show();
            $('time').hide();
            sessionStorage.setItem('status', true);
        }
        else {
            tempo--;
            localStorage.setItem('tempo', tempo);
            tempo = tempo < 10 ? '0' + tempo : tempo;
            tempo = '00:' + tempo;
            $('time').text(tempo);
        }
    }


    $('#btn-verificar-codigo').click(function () {
        $('#carregando-verificar').show();
        $('#texto-verificar').hide();
    });


    $('#btn-reenviar-codigo').click(function () {
        sessionStorage.setItem('status', false);
        localStorage.setItem('tempo', 60);
    });
});
