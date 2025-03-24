from flask import Flask
import os

app = Flask(__name__)
version = os.getenv("APP_VERSION", "blue")

@app.route("/")
def home():
    return f"<h1 style='text-align:center'>This is the {version.upper()} version</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
