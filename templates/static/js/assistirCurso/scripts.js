var crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
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

    $('.cbx_video').click(function () {

        let id = $(this).parent().children('.titulo-video').children('#id-videoDB').html()
        let status = undefined

        if ($(this).prop('checked')) {
            status = true
        } else {
            status = false
        }

        $.ajax({
            url: window.location.href,
            type: 'POST',
            headers: { 'X-CSRFToken': crf_token },
            data: JSON.stringify({ 'id': id, 'status': status }),
            success: function (data) {
                console.log(data);
            },
            error: function (data) {
                console.log(data);
            }
        })
    })

});
