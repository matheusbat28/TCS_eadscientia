$(document).ready(function() {
  $('#btn-gerar-pdf').click(function() {
    var certificateContainer = $('#certificado-container');

    // Opções de configuração para o html2pdf
    var options = {
      filename: 'certificado.pdf',
      image: { type: 'jpeg', quality: 0.98 }, // Configurações opcionais para imagens
      html2canvas: { scale: 2 }, // Configurações opcionais para html2canvas
      jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' } // Configurações opcionais para jsPDF
    };

    setTimeout(function() {
      // Gerar o PDF a partir do conteúdo HTML
      html2pdf().from(certificateContainer.get(0)).set(options).save();
    }, 1000);
  });
});