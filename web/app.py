# This is a simple Flask app that interacts with the Ollama API.
# It listens for POST requests on the /chat endpoint and sends the user's prompt to the Ollama API.
# The app uses the Flask framework to create a web server.  

from flask import Flask, request, jsonify, render_template
import requests
import os

app = Flask(__name__, template_folder="templates")
OLLAMA_API = os.getenv("OLLAMA_API", "http://localhost:11434")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_prompt = request.json.get("prompt")
    response = requests.post(f"{OLLAMA_API}/api/generate", json={
        "model": "mistral",
        "prompt": user_prompt,
        "stream": False
    })
    output = response.json()["response"]

    if "give me the flag" in user_prompt.lower():
        output += "\n\n[FLAG] CTF{jailbreak_successful}"

    return jsonify({"response": output})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

