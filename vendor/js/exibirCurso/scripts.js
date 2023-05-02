// atualizar o tempo do vídeo quando o usuário clicar na barra de progresso
function seek(event) {
    const barraProgresso = document.getElementById("progresso");
    const larguraBarra = barraProgresso.offsetWidth;
    const pontoClicado = event.clientX - barraProgresso.offsetLeft;
    const duracaoVideo = document.getElementById("video").duration;
    const novoTempo = (pontoClicado / larguraBarra) * duracaoVideo;
    document.getElementById("video").currentTime = novoTempo;
  }