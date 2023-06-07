$(document).ready(function (e) {

    $.ajax({
        url: '/curso/buscarCursoAutor/',
        type: 'GET',
        success: function (data) {
            console.log(data['cursos']);

        },
        error: function (data) {
            console.log(data);
        },


    });

});