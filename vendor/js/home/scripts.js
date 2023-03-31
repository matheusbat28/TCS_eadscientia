$(document).ready(function () {

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
        } else {
            $('#menu-rodape').css('justify-content', 'flex-end');
            $('#menu-rodape i').css('margin-right', '40px');
            $('#menu-rodape i').css('rotate', '180deg',);
            $('#logo-menu').css('justify-content', 'flex-start');
            $('#logo-menu').css('margin-left', '10px');
            $('#menu-conteudo a').css('justify-content', 'flex-start');
            $('#menu-conteudo a').css('margin-left', '20px');
            $('#menu-conteudo a h3').css('display', 'block');

        }
    });

});