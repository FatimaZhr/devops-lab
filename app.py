from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "ssalam 3laikom hiya lewla🙂 Version 2 Déployée automatiquement"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)