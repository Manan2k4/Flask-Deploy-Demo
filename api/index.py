from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return jsonify(message="Hello from Flask on Vercel! 🚀")

@app.route("/hello")
def hello_user():
    return jsonify(greet="Hey Manan! This route works too! 🎯")

# Vercel expects this exact function name
def __vercel__handler(request, response):
    return app(request.environ, response.start_response)