document.addEventListener('DOMContentLoaded', function() {
    const readyBtn = document.getElementById('ready-btn');
    const startSection = document.getElementById('start-section');
    const gameSection = document.getElementById('game-section');
    const questionText = document.getElementById('question-text');
    const answerButtons = document.getElementById('answer-buttons');
    const answerBtnEls = document.querySelectorAll('.answer-btn');

    readyBtn.addEventListener('click', function() {
        startSection.style.display = 'none';
        gameSection.style.display = 'block';
        // Solicita la primera pregunta al backend
        fetch('/start_game')
            .then(res => res.json())
            .then(data => {
                questionText.textContent = data.question;
                answerButtons.style.display = 'block';
            });
    });

    answerBtnEls.forEach(btn => {
        btn.addEventListener('click', function() {
            const answer = btn.getAttribute('data-answer');
            fetch('/answer', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ answer })
            })
            .then(res => res.json())
            .then(data => {
                questionText.textContent = data.next_question;
                // Puedes agregar lógica para terminar el juego si es necesario
            });
        });
    });
});

async function sendQuestion() {
    const question = document.getElementById('question').value;
    const response = await fetch('/ask', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({question})
    });

    const data = await response.json();
    document.getElementById('answer').innerText = data.answer;
    const audio = document.getElementById('audio');
    audio.src = data.audio_url;
    audio.play();
}
