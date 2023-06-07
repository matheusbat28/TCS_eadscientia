$(document).ready(function () {
    $('#dado-perfil button p').show();
    $('.carregamento').hide();

    $('#idarquivo').on('change', function () {
        let inputArquivo = $(this)[0].files[0];

        if (inputArquivo) {
            $('#img-perfil img').attr('src', URL.createObjectURL(inputArquivo));
        };
    });

    $('#dado-perfil button').click(function () {
        $('#dado-perfil button p').hide();
        $('.carregamento').show();
    })
});
