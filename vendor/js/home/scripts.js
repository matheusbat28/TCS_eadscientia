$(document).ready(function () {

    $('.seta i, .seta').click(function (e) {

        if (e.target.id === 'seta-direta') {
            $('#carrocel-img').children().first().appendTo('#carrocel-img');
        } else if (e.target.id === 'seta-esquerda') {
            $('#carrocel-img').children().last().prependTo('#carrocel-img');
        }
    });
});