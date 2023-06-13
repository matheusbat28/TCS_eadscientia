document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("campo-pesquisa");
  const input = document.getElementById("pesquisar");
  const tabelaCorpo = document.getElementById("tabela-corpo");
  const paginaAnterior = document.getElementById("pagina-anterior");
  const paginaProxima = document.getElementById("pagina-proxima");
  const infoPaginas = document.getElementById("info-paginas");
  const limpar = document.getElementById("limpar");
  const itensPorPagina = 20; // Defina o número de itens por página
  let paginaAtual = 1; // Variável para armazenar a página atual
  let numPaginas; // Variável para armazenar o número total de páginas

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    filtrarResultados();
  });

  input.addEventListener("keydown", function (event) {
    if (event.keyCode === 13) {
      // Código da tecla Enter
      event.preventDefault();
      filtrarResultados();
    }
  });

  paginaAnterior.addEventListener("click", function () {
    paginacaoAnterior();
  });

  paginaProxima.addEventListener("click", function () {
    paginacaoProxima();
  });

  function filtrarResultados(pagina = 1) {
    const filtro = input.value.toLowerCase();
    const linhas = tabelaCorpo.getElementsByTagName("tr");
    const numLinhas = linhas.length;
    numPaginas = Math.ceil(numLinhas / itensPorPagina); // Atualiza o número total de páginas

    const resultados = []; // Array para armazenar os índices das linhas que correspondem ao filtro

    for (let i = 0; i < numLinhas; i++) {
      const colunas = linhas[i].getElementsByTagName("td");
      let encontrado = false;

      for (let j = 0; j < colunas.length; j++) {
        const texto = colunas[j].textContent.toLowerCase();

        if (texto.includes(filtro)) {
          encontrado = true;
          break;
        }
      }

      if (encontrado) {
        resultados.push(i); // Adiciona o índice da linha aos resultados
      }
    }

    numPaginas = Math.ceil(resultados.length / itensPorPagina); // Atualiza o número total de páginas com base nos resultados

    const inicio = (pagina - 1) * itensPorPagina;
    const fim = inicio + itensPorPagina;
    const indicesPagina = resultados.slice(inicio, fim); // Obtém os índices das linhas para a página atual

    for (let i = 0; i < numLinhas; i++) {
      if (indicesPagina.includes(i)) {
        linhas[i].style.display = ""; // Exibe as linhas correspondentes à página atual
      } else {
        linhas[i].style.display = "none"; // Oculta as linhas que não estão na página atual
      }
    }

    paginaAtual = pagina;
    exibirPaginacao();
  }

  function exibirPaginacao() {
    infoPaginas.textContent = ` ${paginaAtual} a ${numPaginas}`;

    // Desabilita ou habilita o botão de página anterior
    if (paginaAtual === 1) {
      paginaAnterior.classList.add("desabilitado");
    } else {
      paginaAnterior.classList.remove("desabilitado");
    }

    // Desabilita ou habilita o botão de página próxima
    if (paginaAtual === numPaginas) {
      paginaProxima.classList.add("desabilitado");
    } else {
      paginaProxima.classList.remove("desabilitado");
    }
  }

  function paginacaoAnterior() {
    if (paginaAtual > 1) {
      filtrarResultados(paginaAtual - 1);
    }
  }

  function paginacaoProxima() {
    if (paginaAtual < numPaginas) {
      filtrarResultados(paginaAtual + 1);
    }
  }

  // Inicialize a filtragem e a paginação
  filtrarResultados();
});


limpar.addEventListener("click", function () {
  document.getElementById("pesquisar").value = "";
  document.getElementById("campo-pesquisa").submit();
});
