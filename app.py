from flask import Flask, render_template, request, jsonify
from utils.gpt_ai import ask_gpt
from utils.tts_ai import text_to_speech
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question')
    answer = ask_gpt(question)
    audio_url = text_to_speech(answer)
    return jsonify({'answer': answer, 'audio_url': audio_url})

if __name__ == '__main__':
    app.run(debug=True)
