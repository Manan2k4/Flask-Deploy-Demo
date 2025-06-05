from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify(message="Hello from Flask on Vercel! 🚀")

# Required Vercel entrypoint
def handler(request, response):
    return app(request.environ, response.start_response)
