var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');

$('.conteudo-resposta, .carregamento, #mensagem').hide();

function separarDado() {
    var perguntas = [];

    $('.caixa-suspensa').each(function () {
        var pergunta = {
            'pergunta': $(this).children('.cabecalho-pergunta').children('.titulo-cabecalho-pergunta').children('input').val(),
            'opcoes': []
        };

        $(this).find('.conteudo-resposta').children().each(function () {
            var opcao = {
                'status': $(this).children('.cabecalho-resposta').children('input[type="checkbox"]').is(':checked'),
                'pergunta': $(this).children('.cabecalho-resposta').children('input[type="text"]').val()
            };

            pergunta['opcoes'].push(opcao);
        });

        perguntas.push(pergunta);
    });
    console.log(perguntas)

    return JSON.stringify(perguntas);
}

$(document).ready(function (e) {
    $('#formulario-curso').submit(function (e) {
        e.preventDefault();
        $('#mensagem, #btn-criar i').hide();
        $('.carregamento').show();
        $.ajax({
            url: window.location.href,
            type: $(this).attr('method'),
            headers: { 'X-CSRFToken': crf_token },
            data: separarDado(),
            success: function (data) {
                if (data.status == 200) {
                    // window.location.reload()
                    $('#mensagem').show();
                    $('#mensagem').html(data.message).addClass('alert-success').removeClass('alert-danger');
                } else if (data.status == 404) {
                    $('#mensagem').show();
                    $('#mensagem').html(data.message).addClass('alert-danger').removeClass('alert-success');
                }

                $('.carregamento').hide();
                $('#btn-criar i').show();
                $('#mensagem').delay(10000).fadeOut('slow');
            },
            error: function (data) {
                console.log(data);
            }
        });
    });
});


$(document).on('click', '#add-pergunta', function (e) {
    let caixa_suspensao_html = `<div class="caixa-suspensa">
    <div class="cabecalho-pergunta">
        <div class="titulo-cabecalho-pergunta">
            <input required name="inputNomePergunta" type="text" placeholder="Titulo da Pergunta:">
        </div>
        <div class="operacao-cabecalho-resposta">
            <i title="Expandir resposta" class="fa-solid fa-caret-down expandir-resposta"></i>
            <i title="Adicionar resposta" class="fa-solid fa-plus add-resposta"></i>
            <i title="Deletar pergunta" class="fa-solid fa-trash deletar-pergunta"></i>
        </div>
    </div>
    <div class="conteudo-resposta">
        <div class="resposta-pergunta">
            <div class="cabecalho-resposta">
                <input type="checkbox">
                <input required type="text" placeholder="Resposta:">
            </div>
            <div class="deletar-resposta">
                <i title="Deletar Resposta" class="fa-solid fa-trash deletar-resposta"></i>
            </div>
        </div>
    </div>
</div>`;
    $('#conteudo-pergunta').append(caixa_suspensao_html);
});

$(document).on('click', '.expandir-resposta', function (e) {
    var caixaSuspensa = $(this).parent().parent().parent().find('.conteudo-resposta');
    if (caixaSuspensa.is(':visible')) {
        caixaSuspensa.hide();
        $(this).css('transform', 'rotate(0deg)');
    } else {
        caixaSuspensa.show();
        $(this).css('transform', 'rotate(180deg)');
    }

});

$(document).on('click', '.deletar-pergunta', function (e) {
    var caixaSuspensa = $(this).parent().parent().parent().find('.conteudo-resposta');
    caixaSuspensa.hide();
    $(this).parent().parent().parent().remove();
});

$(document).on('click', '.add-resposta', function (e) {
    html_img = `<div class="resposta-pergunta">
    <div class="cabecalho-resposta">
        <input type="checkbox">
        <input required type="text" placeholder="Resposta">
    </div>
    <div class="deletar-resposta">
        <i title="Deletar Resposta" class="fa-solid fa-trash deletar-resposta"></i>
    </div>
</div>`;
    var caixaSuspensa = $(this).parent().parent().parent().find('.conteudo-resposta');
    caixaSuspensa.show();

    $(this).parent().parent().parent().find('.conteudo-resposta').append(html_img);
});

$(document).on('click', '.deletar-resposta', function (e) {
    var caixa

    $(this).parent().parent().remove();
});