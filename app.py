from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)

# This version is more stable for Render's environment
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def home():
    return "ViralForge Engine is Online."

@app.route('/generate', methods=['GET'])
def generate():
    niche = request.args.get('niche', 'trending')
    try:
        # Using the older, more stable method for simple deployments
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a viral hook generator."},
                {"role": "user", "content": f"Create a hook for {niche}"}
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