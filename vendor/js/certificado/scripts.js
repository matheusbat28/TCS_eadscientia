document.getElementById('certificado-form').addEventListener('submit', function(event) {
    event.preventDefault(); 
  
    var nome = document.getElementById('nome').value;
    var curso = document.getElementById('curso').value;
  
    var certificateHTML = '<h2>Certificado</h2>' +
                          '<p>Nome: ' + nome + '</p>' +
                          '<p>Curso: ' + curso + '</p>';
  
    document.getElementById('certificado-container').innerHTML = certificateHTML;
  });
  