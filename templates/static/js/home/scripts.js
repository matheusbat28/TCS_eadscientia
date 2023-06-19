$(document).ready(function () {

    let verStatus = true;

    $("#vermais").click(function () {
        if (verStatus) {
            $('#curso-card').css('height', 'auto')
            verStatus = false;
        } else {
            $('#curso-card').css('height', '500px')
            verStatus = true;
        }
    })

    $.ajax({
        url: '/curso/todoCurso/',
        type: 'GET',
        success: function (data) {
            var cursos = JSON.parse(data.curso);
            $.each(cursos, function (key, value) {
                var option = $('<option></option>').attr('value', value['fields']['nome']);
                $('#pesquisa').append(option);
            })

        }, error: function (data) {
            console.log(data);
        },
    })
});