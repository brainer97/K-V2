from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')
@app.route('/home')
def home():
    return render_template('home.html')
@app.route('/chatgpt')
def chatgpt():
    return render_template('chatgpt.html')

if __name__ == '__main__':
    app.run(debug=True)
