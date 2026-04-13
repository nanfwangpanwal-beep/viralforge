from flask import Flask, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

# Initialize client simply
api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

@app.route('/')
def home():
    return "ViralForge AI Engine is Online."

@app.route('/generate', methods=['GET'])
def generate():
    niche = request.args.get('niche', 'trending topics')
    if not api_key:
        return jsonify({"status": "error", "message": "API Key missing on server"}), 500
        
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a viral content creator."},
                {"role": "user", "content": f"Create a viral hook for {niche}."}
            ]
        )
        return jsonify({
            "status": "success", 
            "content": response.choices[0].message.content
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
