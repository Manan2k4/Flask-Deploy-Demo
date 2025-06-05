from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return jsonify(message="Hello from Flask on Vercel! 🚀")

# Vercel expects this exact function name
def __vercel__handler(request, response):
    return app(request.environ, response.start_response)