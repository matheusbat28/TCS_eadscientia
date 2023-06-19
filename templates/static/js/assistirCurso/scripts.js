$(document).ready(function (e) {

    $('#menu-video').click(function () {
        $('#progresso-curso').toggle()
    })

    $('.titulo-topico').click(function () {
        let sub_conteudo = $(this).parent().parent().children('.corpo-topico');
        sub_conteudo.toggle()
    })

    $('.titulo-video').click(function () {
        let id = $(this).children('#id-video').html()
        $('#corpo-curso embed').attr('src', `https://www.youtube.com/embed/${id}`)
    })

});
