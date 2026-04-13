from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "ViralForge Engine is LIVE. Use /generate?niche=money"

@app.route('/generate', methods=['GET'])
def generate():
    niche = request.args.get('niche', 'trending topics')
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        return jsonify({"error": "API Key missing in Render settings"}), 500

    # The "Direct Bypass" - This ignores all proxy and library bugs
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a viral hook generator."},
            {"role": "user", "content": f"Create a viral hook for {niche}"}
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
            return jsonify({"status": "error", "message": result.get("error", {}).get("message", "OpenAI Error")}), response.status_code

        return jsonify({
            "status": "success",
            "hook": result['choices'][0]['message']['content']
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))