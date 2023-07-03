var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');

$(document).ready(function () {
    var tempoRestante = 3600;

    var intervalo = setInterval(function () {
        var horas = Math.floor(tempoRestante / 3600);
        var minutos = Math.floor((tempoRestante % 3600) / 60);
        var segundos = tempoRestante % 60;

        horas = horas.toString().padStart(2, '0');
        minutos = minutos.toString().padStart(2, '0');
        segundos = segundos.toString().padStart(2, '0');

        $('#temporizador').text(horas + ':' + minutos + ':' + segundos);

        var porcentagem = (tempoRestante / 3600) * 100;
        $('#barra').css('width', porcentagem.toFixed(2) + '%');

        tempoRestante--;

        if (tempoRestante < 0) {
            clearInterval(intervalo);
        }
    }, 1000);

    function separarDado(form) {
        var questoes = [];
        $.each(form.children('.questao'), function (key, value) {
            var questao = {
                'id_questao': $(value).children('.id_questao').html(),
                'id_alternativa': [] // Inicializa como um array vazio
            };

            $.each($(value).children('.alternativas'), function (key, value) {
                var isChecked = $(value).children('#box_questao').prop('checked');
                var id_alternativa = $(value).children('.id_alternativa').html();

                if (isChecked) {
                    questao['id_alternativa'].push(id_alternativa); // Adiciona o ID da alternativa ao array
                }
            });
            questoes.push(questao);
        });
        return JSON.stringify(questoes);
    }



    $('#formulario_avaliacao').submit(function (e) {
        e.preventDefault();
        $.ajax({
            url: window.location.href,
            type: 'POST',
            headers: { 'X-CSRFToken': crf_token },
            data: separarDado($(this)),
            success: function (data) {
                console.log(data);
            },
            error: function (data) {
                console.log(data);
            },

        })
    })
});
