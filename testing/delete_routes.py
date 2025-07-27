from flask import render_template, request, redirect, url_for, session, jsonify, Blueprint
from flask_login import login_required, current_user
import requests
import os

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    if request.method == 'POST':
        data = request.get_json()
        user_input = data.get("prompt", "").strip()

        if not user_input:
            return jsonify({"error": "Prompt cannot be empty."}), 400
        

        try:
            response = requests.post(
                'http://localhost:11434/api/generate', 
                json={
                    "model": "llama3", 
                    "prompt": user_input, 
                    "stream": False
                }
            )

        except requests.exceptions.ConnectionError:
            return jsonify({"error": "Could not connect to local AI model"}), 500
        
        if response.status_code != 200:
            return jsonify({"error": "AI model failed", "details": response.text}), 500
        

        data = response.json()
        return jsonify({"response": data.get("response", "")})

    return render_template('chat.html', user=current_user)