from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h3>Hello, Render! Flask deployment successful 🚀</h3>"

if __name__ == '__main__':
    app.run(debug=True)