from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "Hola Mundo, Soy Eduardo"

if __name__ == '__main__':
    app.run(debug=True)