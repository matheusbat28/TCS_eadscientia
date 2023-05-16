const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
  event.preventDefault();

  // get selected answers
  const q1 = document.querySelector('input[name="q1"]:checked');
  const q2 = document.querySelector('input[name="q2"]:checked');

  // check if answers are selected
  if (!q1 || !q2) {
    alert('Por favor, responda todas as perguntas.');
    return;
  }

  // check answers
  const respostasCorretas = ['a', 'b'];
  const respostasUsuario = [q1.value, q2.value];
  let score = 0;
  for (let i = 0; i < respostasCorretas.length; i++) {
    if (respostasUsuario[i] === respostasCorretas[i]) {
      score++;
    }
  }

  // show score
  const totalQuestoes = respostasCorretas.length;
  const porcentagem = Math.round((score / totalQuestoes) * 100);
  alert(`Você acertou ${score} de ${totalQuestoes} questões (${porcentagem}%).`);

  // check if user is approved
  const radios = document.querySelectorAll('input[type="radio"]:checked');
  const numCorreto = Array.from(radios).reduce(function(acc, radio) {
    const questao = radio.getAttribute('name').slice(-1);
    return acc + (radio.value === respostasCorretas[questao-1] ? 1 : 0);
  }, 0);
  const percentCorreto = numCorreto / totalQuestoes * 100;
  const message = percentCorreto >= 70 ? 'Parabéns, você foi aprovado!' : 'Infelizmente, você não foi aprovado.';
  alert(`Você acertou ${numCorreto} de ${totalQuestoes} questões (${percentCorreto.toFixed(2)}%). ${message}`);
});

// ---------------------------------------------------------------------------------------------

const timerElement = document.getElementById('tempo');

const timeLimit = 30; // 30 segundos

let remainingTime = timeLimit;

function updateTimer() {
  const minutos = Math.floor(remainingTime / 60);
  const segundos = remainingTime % 60;

  const formattedTime = `${minutos.toString().padStart(2, '0')}:${segundos.toString().padStart(2, '0')}`;

  timerElement.textContent = formattedTime;

  remainingTime--;

  if (remainingTime < 0) {
    form.submit();
  }
}

updateTimer();

const timerInterval = setInterval(updateTimer, 1000);

form.addEventListener('submit', function (event) {
  event.preventDefault(); 


  clearInterval(timerInterval);

  form.submit();
});



  