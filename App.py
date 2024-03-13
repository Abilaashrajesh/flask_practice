from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/')
@app.route('/home')
def welcome():
    return "Hi My name is AbilaashRajesh"
@app.route('/submit')
def success():
    return "Registration Success"

@app.route('/name/<name1>')
def name(name1):
    return "Welcome "+str(name1)

@app.route('/pass/<int:score>')
def pas(score):
    return '<h1>You Passed the Exam with {score} marks<h1>'

@app.route('/fail/<int:score>')
def fail(score):
    return '<h1>You Failed the Exam with '+str(score)+' marks<h1>'

@app.route('/result/<int:mark>')
def result(mark):
    res=''
    if mark<50:
        res='fail'
    else:
        res='pas'
    return redirect(url_for(res,score=mark))




if __name__=='__main__':
    app.run(debug=True)