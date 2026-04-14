from flask import Flask, request, jsonify, render_template
import os
import requests

# Tells Flask to look in the main folder for your 10/10 pages
app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate():
    niche = request.args.get('niche', 'trending topics')
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return jsonify({"status": "error", "message": "API Key missing"}), 500
    
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "system", "content": "Viral hook generator."},
                     {"role": "user", "content": f"Create a viral hook for {niche}."}]
    }
    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
        return jsonify({"status": "success", "hook": response.json()['choices'][0]['message']['content']})
    except:
        return jsonify({"status": "error", "message": "Connection failed"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)