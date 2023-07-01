$('.conteudo-caixa-suspensa, #mensagem, .carregamento').hide();
$('#btn-criar i').show();

var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');

$("#mensagem").hide();

function separarDados(dataForm) {
    let capitulos = [];

    $('.caixa-suspensa').each(function () {

        let tituloCapitulo = $(this).find('.cabecalho-caixa-suspensa').find('#inputNomeCapitulo').val();
        var capitulo = {
            'nome-capitulo': tituloCapitulo,
            'videos': []
        }


        $(this).find('.conteudo-caixa-suspensa').each(function () {
            let = video = {};
            $(this).find('.video-capitulo-curso').children().each(function () {
                if ($(this).hasClass('cabecalho-video-capitulo-curso')) {
                    video['nome'] = $(this).children().val()
                } else if ($(this).hasClass('operacao-video-capitulo-curso')) {
                    video['url'] = $(this).children().val()
                    capitulo['videos'].push(video)
                };
            });
        })
        capitulos.push(capitulo)
    });

    dataForm.append('nome-curso', $('#inputTituloCurso').val());
    dataForm.append('capitulos', JSON.stringify(capitulos));
    return dataForm;

}


$(document).ready(function (e) {

    $('#inuptFotoCurso').attr('accept', 'image/*');

    $('#formulario-curso').submit(function (e) {
        e.preventDefault();
        $('#mensagem, #btn-criar i').hide();
        $('.carregamento').show();

        $.ajax({
            url: curso/adicionarCurso/,
            type: $(this).attr('method'),
            headers: { 'X-CSRFToken': crf_token },
            processData: false,
            contentType: false,
            data: separarDados(new FormData(this)),
            success: function (data) {
                if (data.status == 200) {
                    window.location.reload()
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
                $('.carregamento').hide();
                $('#btn-criar i').show();
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
            <input required id="inputNomeCapitulo" name="inputNomeCapitulo" type="text" placeholder="Titulo do capítulo:">
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
                <input required type="text" id="inputNomeVideo" name="inputNomeVideo" placeholder="Titulo do video:">
            </div>
            <div class="operacao-video-capitulo-curso">
                <input required type="text" id="inputUrlVideo" name="inputUrlVideo" placeholder="Url do video:">
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
            <input required type="text" id="inputNomeVideo" name="inputNomeVideo" placeholder="Titulo do video:">
        </div>
        <div class="operacao-video-capitulo-curso">
            <input required type="text" id="inputUrlVideo" name="inputUrlVideo" placeholder="Url do video:">
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