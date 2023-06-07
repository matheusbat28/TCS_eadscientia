document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('campo-pesquisa');
    const input = document.getElementById('pesquisar');
    const tabelaCorpo = document.getElementById('tabela-corpo');
    const paginationContainer = document.getElementById('pagination');
    const itensPorPagina = 1; // Defina o número de itens por página
  
    form.addEventListener('submit', function(event) {
      event.preventDefault();
      filtrarResultados();
    });
  
    input.addEventListener('keydown', function(event) {
      if (event.keyCode === 13) { // Código da tecla Enter
        event.preventDefault();
        filtrarResultados();
      }
    });
  
    document.querySelector("button[name='btnlimpar']").addEventListener("click", function(event) {
      event.preventDefault();
      limparPesquisa();
    });
  
    function filtrarResultados(pagina = 1) {
      const filtro = input.value.toLowerCase();
      const linhas = tabelaCorpo.getElementsByTagName('tr');
      const numLinhas = linhas.length;
      const numPaginas = Math.ceil(numLinhas / itensPorPagina);
  
      const inicio = (pagina - 1) * itensPorPagina;
      const fim = inicio + itensPorPagina;
  
      for (let i = 0; i < numLinhas; i++) {
        if (i >= inicio && i < fim) {
          const colunas = linhas[i].getElementsByTagName('td');
          let encontrado = false;
  
          for (let j = 0; j < colunas.length; j++) {
            const texto = colunas[j].textContent.toLowerCase();
  
            if (texto.includes(filtro)) {
              encontrado = true;
              break;
            }
          }
  
          linhas[i].style.display = encontrado ? '' : 'none';
        } else {
          linhas[i].style.display = 'none';
        }
      }
  
      exibirPaginacao(pagina);
    }
  
    function exibirPaginacao(paginaAtual) {
      let paginacaoHTML = '';
  
      for (let i = 1; i <= numPaginas; i++) {
        paginacaoHTML += `<button class="pagina${i === paginaAtual ? ' ativa' : ''}">${i}</button>`;
      }
  
      paginationContainer.innerHTML = paginacaoHTML;
  
      // Adicione o evento de clique para cada botão de página
      paginationContainer.querySelectorAll('button').forEach(function(botao, index) {
        botao.addEventListener('click', function() {
          filtrarResultados(index + 1);
        });
      });
    }
  
    function limparPesquisa() {
      input.value = '';
  
      const linhas = tabelaCorpo.getElementsByTagName('tr');
  
      for (let i = 0; i < linhas.length; i++) {
        linhas[i].style.display = '';
      }
    }
  
    // Inicialize a filtragem e a paginação
    filtrarResultados();
  });
