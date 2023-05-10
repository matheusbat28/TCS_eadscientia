$('.conteudo-caixa-suspensa').hide();

$(document).ready(function (e) {
});

$(document).on('click', '#add-capitulo', function (e) {
    let caixa_suspensao_html = `<div class="caixa-suspensa">
    <div class="cabecalho-caixa-suspensa">
        <div class="titulo-cabecalho-caixa-suspensa">
            <input name="inputNomeCapitulo" type="text" placeholder="Titulo do capítulo:">
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
                <input type="text" name="inputNomeVideo" placeholder="Titulo do video:">
            </div>
            <div class="operacao-video-capitulo-curso">
                <input type="file" name="inputArquivo" id="">
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
            <input type="text" placeholder="Titulo do video:">
        </div>
        <div class="operacao-video-capitulo-curso">
            <input type="file" name="inputArquivo" id="">
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