from flask import Flask, render_template, request, jsonify
from utils import google_ai

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game')
def start_game():
    question = google_ai.get_first_question()
    return jsonify({'question': question})

@app.route('/answer', methods=['POST'])
def answer():
    data = request.get_json()
    answer = data.get('answer')
    # Puedes mantener un contexto de juego si lo deseas
    next_question = google_ai.get_next_question(answer, context={})
    return jsonify({'next_question': next_question})

if __name__ == '__main__':
    app.run(debug=True)
