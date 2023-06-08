$(document).ready(function () {


    $('.itens-subconteudo, .seta-baixo, #matricula').hide();

    $('#menu-rodape, #menu-icon').click(function () {

        if ($('#cbx-menu').is(':checked')) {
            $('#menu-rodape').css('justify-content', 'center');
            $('#menu-rodape i').css('margin-right', '0');
            $('#menu-rodape i').css('rotate', '0deg');
            $('#logo-menu').css('justify-content', 'center');
            $('#logo-menu').css('margin-left', '0');
            $('#menu-conteudo a').css('justify-content', 'center');
            $('#menu-conteudo a').css('margin-left', '0');
            $('#menu-conteudo a h3').css('display', 'none');
            $('.itens-subconteudo').hide();
            $('.seta-baixo').hide();
            $('.seta-baixo').css('transform', 'rotate(0deg)');
            $('#matricula').hide();
        } else {
            $('#menu-rodape').css('justify-content', 'flex-end');
            $('#menu-rodape i').css('margin-right', '40px');
            $('#menu-rodape i').css('rotate', '180deg',);
            $('#logo-menu').css('justify-content', 'flex-start');
            $('#logo-menu').css('margin-left', '10px');
            $('#menu-conteudo a').css('justify-content', 'flex-start');
            $('#menu-conteudo a').css('margin-left', '20px');
            $('#menu-conteudo a h3').css('display', 'block');
            $('.seta-baixo').show();
            $('#matricula').show();
        }
    });

    $('.seta').click(function (e) {

        if ((this).id === 'seta-esqueda') {
            $('#card-carrocel').children().last().prependTo('#card-carrocel')

        } else if ((this).id === 'seta-direita') {
            $('#card-carrocel').children().first().appendTo('#card-carrocel')
        }
    });

    function carrocelAnimacao() {
        $('#card-carrocel').children().first().appendTo('#card-carrocel')
    }

    setInterval(carrocelAnimacao, 10000)

});

$(document).on('click', '.itens-conteudo', function (e) {
    var sub_conteudo = $(this).next('.itens-subconteudo');
    if (sub_conteudo.is(':visible')) {
        sub_conteudo.hide();
        $(this).find('.seta-baixo').css('transform', 'rotate(0deg)');
    } else {
        sub_conteudo.show();
        $(this).find('.seta-baixo').css('transform', 'rotate(180deg)');
    }
});