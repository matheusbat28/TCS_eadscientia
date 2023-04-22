$(document).ready(function () {

    $('.seta i, .seta').click(function (e) {

        if (e.target.id === 'seta-direta') {
            $('#carrocel-img').children().first().appendTo('#carrocel-img');
        } else if (e.target.id === 'seta-esquerda') {
            $('#carrocel-img').children().last().prependTo('#carrocel-img');
        }
    });
});

function slideshow() {
  // pegar a primeira imagem do carrossel
  const primeiraImg = document.querySelector('.carrocel-img:first-child');
  // obter a largura da imagem para calcular o deslocamento
  const imgWidth = primeiraImg.offsetWidth;

  // mover o carrossel para a esquerda
  document.querySelector('#carrocel-img').style.transform = `translateX(-${imgWidth}px)`;

  // mover a primeira imagem para o final do carrossel
  document.querySelector('#carrocel-img').appendChild(primeiraImg);

  // reiniciar a posição do carrossel quando chegar ao final
  const ultimaImg = document.querySelector('.carrocel-img:last-child');
  if (ultimaImg.style.transform == `translateX(-${imgWidth}px)`) {
    document.querySelector('#carrocel-img').style.transform = 'translateX(0)';
  }
}

// chamar a função slideshow a cada 3 segundos
setInterval(slideshow, 3000);




