import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    secret_is_set = bool(os.getenv("APP_SECRET"))
    return jsonify(
        message="Hello from DevOps project!",
        secret_configured=secret_is_set
    )

@app.get("/products")
def products():
    data = [
        {"id": 1, "name": "Keyboard", "price": 120},
        {"id": 2, "name": "Mouse", "price": 60},
    ]
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
