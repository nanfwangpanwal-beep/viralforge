from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key="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")

@app.route('/')
def home():
    return "ViralForge API is running 🚀"

@app.route('/generate')
def generate():
    niche = request.args.get('niche', 'business')

    prompt = f"""
    Generate a viral short-form video idea in the {niche} niche.

    Include:
    - Hook (very attention grabbing)
    - Content idea
    - Caption
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return jsonify({
        "result": response.choices[0].message.content
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
