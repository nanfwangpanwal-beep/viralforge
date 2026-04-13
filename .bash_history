pkg update && pkg upgrade -y
mkdir viralforge
cd viralforge
nano app.pyfrom flask import Flask, request, jsonify
'termux-change-repo'
nano app.py
<html lang="en">
<head>
</head>
<body>
</body>
</html>nano index.html
nano index.html
python -m http.server 8000
nano index.html
python -m http.server 8000
mkdir viralforge
cd viralforge
nano app.py
git add app.py
git commit -m "Update app.py with generate route"

cd ~/viralforge
git init
git add .
git commit -m "Initial ViralForge commit"
git branch -M main
git remote add origin https://github.com/nanfwangpanwal-beep/viralforge.git
git push -u origin main
git config --global user.name "nanfwangpanwal-beep"
git config --global user.email "your_email@example.com"
git add .
git commit -m "Initial ViralForge commit"
git branch -M main
cd ~/viralforge
git remote add origin https://github.com/nanfwangpanwal-beep/viralforge.git
git branch -M main
git push -u origin main
heroku login
pkg install nodejs
y
pkg install nodejs
y
web: gunicorn app:app
pip install gunicorn
gunicorn app:app
git init
git add .
git commit -m "Prepare ViralForge for deployment"pkg install nodejs
npm install -g heroku
pkg install nodejs
npm install -g heroku
pwd
cd ~/viralforge
pwd
git add .
git commit -m "Prepare ViralForge for deployment"
git init
git branch -m main
git add .
git commit -m "Prepare ViralForge for deployment"
git init
git branch - main
cd ~/viralforge
pwd
git init
git branch -m main
git add .
git commit -m "Prepare ViralForge for deployment"
heroku login
cd ~/viralforge
pwd
git init
git branch -m main
git add .
git commit -m "Prepare ViralForge for deployment"
heroku create viralforge-app
pip install beautifulsoup4 requests
touch scraper.py
nano scraper.py
python scraper.py
nano app.py
python app.py
ls
python scraper.py
nano app.py
nano scraper.py
python app.py
@app.route("/test")
def test():
cd ~/viralforge
git status
git log
curl https://viralforge-app.herokuapp.com/generate
heroku logs --tail
@app.route("/health")
def health():
git add .
git commit -m "Add healthcheck"
git push heroku main
cd ~/viralforge
python app.py
app.py
requirements.txt
Flask
gunicorn
cd ~/viralforge
git init
git branch -m main
git add .
git commit -m "Initial commit for ViralForge"
git remote add origin https://github.com/YOUR_USERNAME/viralforge.git
git push -u origin main
pip install -r requirements.txt
gunicorn app:app
app .py
in
it
pip install -r requirements.txt
gunicorn app:app
app.py
requirements.txt
runtime.txt
python app.py
app.py
pkg install nano -y
nano app.py
nano requirements.txt
web: gunicorn app:app
cd ~/viralforge
git add .
git commit -m "Initialize ViralForge with Flask and Gunicorn"
git push origin main
# 1. Create app.py
cat <<EOF > app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "ViralForge API is running!"

@app.route('/generate', methods=['GET'])
def generate():
    niche = request.args.get('niche', 'general')
    return jsonify({
        "status": "success", 
        "niche": niche,
        "message": "ViralForge is active"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
EOF

# 2. Create requirements.txt
cat <<EOF > requirements.txt
Flask==3.0.3
gunicorn==22.0.0
EOF

# 3. Create Procfile
echo "web: gunicorn app:app" > Procfile
git add app.py requirements.txt Procfile
git commit -m "Files ready for Render"
git push origin main
git remote set-url origin https://nanfwangpanwal-beep:ghp_UtluCVEXaNHOK9mS8HnkMNeOmLr9Vw2qb7GE@github.com/nanfwangpanwal-beep/viralforge.git
git push origin main
pkg install gh -y
gh auth login
git remote set-url origin https://nanfwangpanwal-beep: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@github.com/nanfwangpanwal-beep/viralforge.git
git push origin main
cat <<EOF > app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# We will get the key from Render's environment variables instead
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def home():
    return "ViralForge API is running!"

@app.route('/generate', methods=['GET'])
def generate():
    niche = request.args.get('niche', 'general')
    return jsonify({"status": "success", "niche": niche})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
EOF

rm .env
git add app.py
git commit -m "Remove sensitive keys for security"
git push origin main
app.py
git checkout --orphan latest_branch
git add -A
git commit -am "Initial clean commit"
git branch -D main
git branch -m main
git push -f origin main
curl "https://viralforge-xxxx.onrender.com/generate?niche=business"
https://viralforge-xab9.onrender.com
curl "https://viralforge-xab9.onrender.com"
git commit -am "Update my app"
git push origin main
app.py
echo "openai" >> requirements.txt
echo openai requirements.txt
cat <<EOF > app.py
from flask import Flask, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

# This pulls the key you saved in the Render Environment Dashboard
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/')
def home():
    return "ViralForge AI Engine is Online."

@app.route('/generate', methods=['GET'])
def generate():
    niche = request.args.get('niche', 'trending topics')
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a viral content creator. Generate a high-engagement hook and 3 bullet points for a short video."},
                {"role": "user", "content": f"Create a viral video outline for the {niche} niche."}
            ]
        )
        ai_text = response.choices[0].message.content
        return jsonify({
            "status": "success",
            "niche": niche,
            "content": ai_text
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
EOF

git add app.py requirements.txt
git commit -m "Add OpenAI generation logic"
git push origin main
git add app.py requirements.txt
git commit -m "Add OpenAI generation logic"
git push origin main
cat <<EOF > app.py
from flask import Flask, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

# This pulls the key you saved in the Render Environment Dashboard
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/')
def home():
    return "ViralForge AI Engine is Online."

@app.route('/generate', methods=['GET'])
def generate():
    niche = request.args.get('niche', 'trending topics')
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a viral content creator. Generate a high-engagement hook and 3 bullet points for a short video."},
                {"role": "user", "content": f"Create a viral video outline for the {niche} niche."}
            ]
        )
        ai_text = response.choices[0].message.content
        return jsonify({
            "status": "success",
            "niche": niche,
            "content": ai_text
        })
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
EOF

git add app.py requirements.txt
git commit -m "Add OpenAI generation logic"
git push origin main
requirements.txt
echo "openai" >> requirements.txt
git push origin main
cat <<EOF > requirements.txt
Flask==3.0.3
gunicorn==22.0.0
openai==1.14.3
EOF

git add requirements.txt
git commit -m "Ensure openai library is installed"
git push origin main
opt/render/project/src/.venv/lib/python3.14/site-packages/gunicorn/app/base.py"

git add requirements.txt
git commit -m "Ensure openai library is installed"
git push origin main
cat <<EOF > requirements.txt
Flask==3.0.3
gunicorn==22.0.0
openai==1.14.3
EOF

python app.py
git add requirements.txt
git commit -m "Force update openai dependency"
git push origin main
python app.py
cat <<EOF > app.py
from flask import Flask, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

# This helps us debug in the Render logs
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    print("ERROR: OPENAI_API_KEY environment variable is missing!")

client = OpenAI(api_key=api_key)

@app.route('/')
def home():
    return "ViralForge AI Engine is Online."

@app.route('/generate', methods=['GET'])
def generate():
    niche = request.args.get('niche', 'trending topics')
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a viral content creator."},
                {"role": "user", "content": f"Create a viral hook for {niche}."}
            ]
        )
        return jsonify({"status": "success", "content": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
EOF

git add app.py
git commit -m "Add debug logging for API key"
git push origin main
