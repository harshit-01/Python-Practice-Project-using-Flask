from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    fruits = ["apple","mango","grapes"]
    return render_template('index.html')
@app.route('/about')
def about():
    return "<h1>Hi Guyz</h1>"
@app.route('/quotes')
def quotes():
	 return render_template('quotes.html')
@app.route('/process',methods=['POST'])
def process():
    author = request.form(['author'])
    quote = request.form(['quote'])
    return redirect(url_for('index.html'))
