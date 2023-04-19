$(document).ready(function () {

    $('.seta').click(function (e) {


        if (e.target.children[0].id === 'seta-direta') {
            $('#carrocel-img').children().first().appendTo('#carrocel-img');
        } else if (e.target.children[0].id === 'seta-esquerda') {
            $('#carrocel-img').children().last().prependTo('#carrocel-img');
            console.log($('#carrocel-img').children().last());
        }
    });
});