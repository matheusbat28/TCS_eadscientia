$(document).ready(function () {

    let admStatus = true;
    let rhStatus = true;
    let gestaoStatus = true;

    $('.itens-subconteudo, .seta-baixo').hide();

    $('#menu-rodape').click(function () {

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
        }
    });

    $('#Administracao').click(function () {
        if (admStatus && $('#cbx-menu').is(':checked')) {
            $('#administracao-conteudo').show();
            $('#seta-adm').css('transform', 'rotate(180deg)');
            admStatus = false;
        } else {
            $('#administracao-conteudo').hide();
            $('#seta-adm').css('transform', 'rotate(0deg)');
            admStatus = true;
        }
    });

    $('#rh').click(function () {
        if (rhStatus && $('#cbx-menu').is(':checked')) {
            $('#rh-conteudo').show();
            $('#seta-rh').css('transform', 'rotate(180deg)');
            rhStatus = false;
        } else {
            $('#rh-conteudo').hide();
            $('#seta-rh').css('transform', 'rotate(0deg)');
            rhStatus = true;
        }
    });

    $('#gestao').click(function () {
        if (gestaoStatus && $('#cbx-menu').is(':checked')) {
            $('#gestao-conteudo').show();
            $('#seta-gestao').css('transform', 'rotate(180deg)');
            gestaoStatus = false;
        } else {
            $('#gestao-conteudo').hide();
            $('#seta-gestao').css('transform', 'rotate(0deg)');
            gestaoStatus = true;
        }
    });

});