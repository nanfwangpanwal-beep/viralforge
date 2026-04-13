from flask import Flask, request, jsonify, render_template
import os
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # This tells Flask to look for index.html in the /templates folder
    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate():
    niche = request.args.get('niche', 'trending topics')
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if not api_key:
        return jsonify({"status": "error", "message": "API Key missing in Render settings"}), 500

    # Headers for direct API communication
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    # Data structure for the AI request
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a viral hook generator for social media."},
            {"role": "user", "content": f"Create one high-energy viral hook for the {niche} niche."}
        ]
    }

    try:
        # Direct POST request to bypass library/proxy bugs
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
    # Render provides the PORT environment variable automatically
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)