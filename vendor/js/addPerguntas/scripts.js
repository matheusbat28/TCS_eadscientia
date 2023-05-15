$('.conteudo-resposta').hide();

$(document).ready(function (e) {
});

$(document).on('click', '#add-pergunta', function (e) {
    let caixa_suspensao_html = `<div class="caixa-suspensa">
    <div class="cabecalho-pergunta">
        <div class="titulo-cabecalho-pergunta">
            <input name="inputNomePergunta" type="text" placeholder="Titulo da Pergunta:">
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
                <input type="radio">
                <input type="text" placeholder="Resposta:">
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
        <input type="radio">
        <input type="text" placeholder="Resposta">
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