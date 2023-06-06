document.getElementById("campo-pesquisa").addEventListener("submit", function(event) {
    event.preventDefault();

    var input = document.getElementById("pesquisar");
    var filter = input.value.toUpperCase();

    var select = document.getElementById("status");
    var statusFilter = select.value;

    var table = document.getElementById("tabela");
    var rows = table.getElementsByTagName("tr");

    for (var i = 0; i < rows.length; i++) {
      var cursoCell = rows[i].getElementsByTagName("td")[0];
      var statusCell = rows[i].getElementsByTagName("td")[1];

      if (cursoCell || statusCell) {
        var cursoText = cursoCell.textContent || cursoCell.innerText;
        var statusText = statusCell.textContent || statusCell.innerText;

        var cursoMatch = cursoText.toUpperCase().indexOf(filter) > -1;
        var statusMatch = statusText.toUpperCase().indexOf(statusFilter.toUpperCase()) > -1;

        if (cursoMatch && statusMatch) {
          rows[i].style.display = "";
        } else {
          rows[i].style.display = "none";
        }
      }
    }
  });
  
  document.querySelector("button[name='btnlimpar']").addEventListener("click", function(event) {
    event.preventDefault(); 
  
    var input = document.getElementById("pesquisar");
    var select = document.getElementById("status");
  
    input.value = ""; 
    select.value = ""; 
  
    document.getElementById("campo-pesquisa").dispatchEvent(new Event("submit"));
  });