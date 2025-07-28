from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from OpenShift with Python!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # OpenShift uses 8080 by default
    app.run(host="0.0.0.0", port=port)
