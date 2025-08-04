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
