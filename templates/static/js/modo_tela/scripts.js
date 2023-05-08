if (localStorage.getItem('modo_tela') == 'false') {
    $('body').removeClass('modo-claro');
    $('body').addClass('modo-escuro');
} else {
    $('body').removeClass('modo-escuro');
    $('body').addClass('modo-claro');
}

$(document).on('click', '#modo_tela', function (e) {
    if ($('body').hasClass('modo-claro')) {
        $('body').removeClass('modo-claro');
        $('body').addClass('modo-escuro');
        $(this).parent().find('#modo_tela i').removeClass('fa-cloud-moon');
        $(this).parent().find('#modo_tela i').addClass('fa-cloud-sun');
        localStorage.setItem('modo_tela', 'false');
    } else {
        $('body').removeClass('modo-escuro');
        $('body').addClass('modo-claro');
        $(this).parent().find('#modo_tela i').removeClass('fa-cloud-sun');
        $(this).parent().find('#modo_tela i').addClass('fa-cloud-moon');
        localStorage.setItem('modo_tela', 'true');
    }


});
