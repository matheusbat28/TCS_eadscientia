$(document).ready(function () {
    $('#certificado').click(function () {
        let curso = $(this).parent().parent().parent().parent().children('.info-curso').children('h3').html()
        console.log(curso)
    })
});