'''Flask's basic web app

'''

from flask import Flask, render_template, request 

#WSGI Application
app=Flask(__name__)

@app.route("/", methods = ['GET'])
def welcome():
    return "Welcome to this best Flask app."

@app.route("/index", methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method=='POST':
        n=request.form['name']
        m=request.form['marks']

        return f'{n} obtain {m} marks!'
    return render_template('form.html')

@app.route('/success', methods = ['GET','POST'])
def success():
    if request.method=='POST':
        name=request.form['name']
        score=request.form['marks']

        res=""
        if int(score) >= 50:
            res="PASSED"
        else:
            res="FAILED"
            
        return f'Hello {name} you have obtained {score} and you are {res}!'
    
    return  render_template('form.html')

@app.route('/link/<name>/<int:score>', methods = ['GET'])
def link(name, score):
    return f'{name} you have obtaine {score} marks!'


if __name__=="__main__":
    app.run(debug=True)