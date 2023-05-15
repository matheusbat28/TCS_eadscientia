$('.conteudo-caixa-suspensa, #mensagem, .carregamento').hide();
$('#btn-criar i').show();

var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');

$("#mensagem").hide();

function separadorDadoJson(dataForm) {
    let = capitulo = [];

    for (let i = 2; i < dataForm.length; i++) {
        if (dataForm[i].name == 'inputNomeCapitulo') {
            let nomeCapitulo = dataForm[i].value;
            let video = [];
            capitulo.push({ 'nomeCapitulo': nomeCapitulo, 'video': video });
        }
        if (dataForm[i].name == 'inputNomeVideo') {
            let nomeVideo = dataForm[i].value;
            let urlVideo = dataForm[i + 1].value;
            capitulo[capitulo.length - 1].video.push({ 'nomeVideo': nomeVideo, 'urlVideo': urlVideo });
        }
    }



    let dados = {
        'nomeCurso': dataForm[1].value,
        'capitulos': capitulo
    };

    return JSON.stringify(dados);
};


$(document).ready(function (e) {

    $('#inuptFotoCurso').attr('accept', 'image/*');

    $('#formulario-curso').submit(function (e) {
        e.preventDefault();
        $('#mensagem, #btn-criar i').hide();
        $('.carregamento').show();

        let dataForm = $(this).serializeArray();
        $.ajax({
            url: '/curso/adicionarCurso/',
            type: 'POST',
            headers: { 'X-CSRFToken': crf_token },
            contentType: 'application/json; charset=utf-8',
            data: separadorDadoJson(dataForm),
            success: function (data) {
                if (data.status == 'successo') {
                    $('#mensagem').show();
                    $('#mensagem').html(data.message).addClass('alert-success').removeClass('alert-danger');
                } else {
                    $('#mensagem').show();
                    $('#mensagem').html(data.message).addClass('alert-danger').removeClass('alert-success');
                }
                $('.carregamento').hide();
                $('#btn-criar i').show();

                $('#mensagem').delay(10000).fadeOut('slow');
            },
            error: function (data) {
                console.log(data);
            },

        });
    });

});

$(document).on('click', '#add-foto-fundo, .fechar-modal-foto', function (e) {
    $('#modal-foto').toggle();
    if ($('#modal-foto').is(':visible')) {
        $('#modal-foto').css('display', 'flex');
    }

});

$(document).on('click', '#add-capitulo', function (e) {
    let caixa_suspensao_html = `<div class="caixa-suspensa">
    <div class="cabecalho-caixa-suspensa">
        <div class="titulo-cabecalho-caixa-suspensa">
            <input required name="inputNomeCapitulo" type="text" placeholder="Titulo do capítulo:">
        </div>
        <div class="operacao-cabecalho-caixa-suspensa">
            <i title="Expandir capítulo" class="fa-solid fa-caret-down expandir-capitulo"></i>
            <i title="Adicionar video" class="fa-solid fa-plus add-video"></i>
            <i title="Deletar capitulo" class="fa-solid fa-trash deletar-capitulo"></i>
        </div>
    </div>
    <div class="conteudo-caixa-suspensa">
        <div class="video-capitulo-curso">
            <div class="cabecalho-video-capitulo-curso">
                <input required type="text" name="inputNomeVideo" placeholder="Titulo do video:">
            </div>
            <div class="operacao-video-capitulo-curso">
                <input required type="text" name="inputUrlVideo" placeholder="Url do video:">
                <i title="Deletar capitulo" class="fa-solid fa-trash deletar-video"></i>
            </div>
        </div>
    </div>
</div>`;
    $('#conteudo-curso').append(caixa_suspensao_html);
});

$(document).on('click', '.expandir-capitulo', function (e) {
    var caixaSuspensa = $(this).parent().parent().parent().find('.conteudo-caixa-suspensa');
    if (caixaSuspensa.is(':visible')) {
        caixaSuspensa.hide();
        $(this).css('transform', 'rotate(0deg)');
    } else {
        caixaSuspensa.show();
        $(this).css('transform', 'rotate(180deg)');
    }

});

$(document).on('click', '.deletar-capitulo', function (e) {
    var caixaSuspensa = $(this).parent().parent().parent().find('.conteudo-caixa-suspensa');
    caixaSuspensa.hide();
    $(this).parent().parent().parent().remove();
});

$(document).on('click', '.add-video', function (e) {
    html_img = `<div class="video-capitulo-curso">
        <div class="cabecalho-video-capitulo-curso">
            <input required type="text" name="inputNomeVideo" placeholder="Titulo do video:">
        </div>
        <div class="operacao-video-capitulo-curso">
            <input required type="text" name="inputUrlVideo" placeholder="Url do video:">
            <i title="Deletar capitulo" class="fa-solid fa-trash deletar-video"></i>
        </div>
    </div>`;
    var caixaSuspensa = $(this).parent().parent().parent().find('.conteudo-caixa-suspensa');
    caixaSuspensa.show();

    $(this).parent().parent().parent().find('.conteudo-caixa-suspensa').append(html_img);
});

$(document).on('click', '.deletar-video', function (e) {
    var caixa

    $(this).parent().parent().remove();
});


$(document).on('change', '#inuptFotoCurso', function (e) {
    var file = $(this)[0].files[0];
    var reader = new FileReader();
    reader.onloadend = function () {
        $('#img-conteudo-modal-foto').attr('src', reader.result);
    }
    reader.readAsDataURL(file);
});