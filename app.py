from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)

# Use the older, bulletproof initialization for Render
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def home():
    return "ViralForge Engine is Online. Use /generate?niche=money"

@app.route('/generate', methods=['GET'])
def generate():
    niche = request.args.get('niche', 'trending')
    try:
        # Universal call format
        response = openai.chat.completions.create(
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
        return jsonify({
            "status": "error", 
            "message": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))