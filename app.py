'''Flask's basic web app

'''

from flask import Flask, render_template, request 

#WSGI Application
app=Flask(__name__)

@app.route("/", methods = ['GET'])
def welcome():
    return "Welcome to this best Flask app."

@app.route("/first-page", methods = ['GET'])
def index():
    return render_template('index.html')

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')



if __name__=="__main__":
    app.run(debug=True)