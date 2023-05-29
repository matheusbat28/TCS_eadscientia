document.getElementById('certificado-form').addEventListener('submit', function(event) {
  event.preventDefault(); // Impede o envio do formulário padrão

  // Recupera os valores dos campos do formulário
  var nome = document.getElementById('nome').value;
  var curso = document.getElementById('curso').value;

  // Obtém a data atual
  var dataAtual = new Date();
  var dia = dataAtual.getDate();
  var mes = dataAtual.toLocaleString('default', { month: 'long' });
  var ano = dataAtual.getFullYear();

  // Monta o HTML do certificado gerado
  var certificateHTML = `
  <div class="header">
    <img src="logo.png" alt="Logo da Instituição" class="logo">
    <h2>Certificado de Conclusão</h2>
  </div>
  <div class="content">
    <p>Este certificado é concedido a:</p>
    <h3 class="nome-aluno">${nome}</h3>
    <p>Pela conclusão do curso:</p>
    <h4 class="nome-curso">${curso}</h4>
    <p>Data: ${dia} de ${mes} de ${ano}</p>
  </div>
  <div class="footer">
    <div class="assinaturas">
      <div class="assinatura">
        <img src="assinatura1.png" alt="Assinatura do Diretor" class="assinatura-img">
      </div>
      <div class="assinatura">
        <img src="assinatura2.png" alt="Assinatura do Instrutor" class="assinatura-img">
      </div>
    </div>
  </div>
`;

  // Exibe o certificado gerado no contêiner
  document.getElementById('certificado-container').innerHTML = certificateHTML;
});


  // -------------------------------gerar certificado--------------------------------------

  window.onload = function() {
    document.getElementById('btn-gerar-pdf').addEventListener('click', function() {
      var certificateContainer = document.getElementById('certificado-container');
  
      // Opções de configuração para o html2pdf
      var options = {
        filename: 'certificado.pdf',
        image: { type: 'jpeg', quality: 0.98 }, // Configurações opcionais para imagens
        html2canvas: { scale: 2 }, // Configurações opcionais para html2canvas
        jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' } // Configurações opcionais para jsPDF
      };
  
      setTimeout(function() {
        // Gerar o PDF a partir do conteúdo HTML
        html2pdf().from(certificateContainer).set(options).save();
      }, 1000);
  });
  }
  
  


  