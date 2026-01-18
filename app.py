
from flask import Flask, render_template, request, jsonify
from letters import generate_art
import os

app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    text = data.get('name', '')
    if not text:
        return jsonify({'art': ''})
    
    art = generate_art(text)
    return jsonify({'art': art})

if __name__ == '__main__':
    app.run(debug=True)
