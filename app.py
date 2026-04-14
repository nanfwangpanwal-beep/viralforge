from flask import Flask, request, jsonify, render_template
import os
import requests

# CRITICAL FIX: Tell Flask to look in the main folder ('.') for HTML files
app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    # Now looks for index.html in your main directory
    return render_template('index.html')

@app.route('/login.html')
def login_page():
    # Explicitly serves the login page from the main directory
    return render_template('login.html')

@app.route('/generate', methods=['GET'])
def generate():
    niche = request.args.get('niche', 'trending topics')
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        return jsonify({"status": "error", "message": "API Key missing in Render settings"}), 500

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a viral hook generator for social media."},
            {"role": "user", "content": f"Create one high-energy viral hook for the {niche} niche."}
        ]
    }

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=10
        )
        result = response.json()
        
        if response.status_code != 200:
            return jsonify({
                "status": "error", 
                "message": result.get("error", {}).get("message", "OpenAI Account Issue")
            }), response.status_code

        return jsonify({
            "status": "success",
            "hook": result['choices'][0]['message']['content']
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)