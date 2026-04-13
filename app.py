from flask import Flask, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

# This setup forces the client to ignore Render's internal proxy settings
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://api.openai.com/v1"
)

@app.route('/')
def home():
    return "ViralForge Engine is Online. Use /generate?niche=money"

@app.route('/generate', methods=['GET'])
def generate():
    niche = request.args.get('niche', 'trending topics')
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a viral hook generator."},
                {"role": "user", "content": f"Create a viral hook for {niche}"}
            ]
        )
        return jsonify({
            "status": "success",
            "hook": response.choices[0].message.content
        })
    except Exception as e:
        # This will show the actual error on your screen if it fails
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))