from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__)

# @app.route('/')
# def welcome():
#     return render_template('index.html')
# @app.route('/submit')
# def success():
#     return "Registration Success"

# @app.route('/name/<name1>')
# def name(name1):
#     return "Welcome "+str(name1)

@app.route('/pass/<int:score>')
def pas(score):
    return render_template('pass.html',result=score)

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

@app.route('/submit',methods=['POST','GET'])
def submit():
    total=0
    if request.method=='POST':
        science=float(request.form.get('science'))
        maths=float(request.form.get('maths'))
        c=float(request.form.get('c'))
        ds=float(request.form.get('ds'))
        total=(science+c+ds+maths)/4
    if total<50:
        res='fail'
    else:
        res='pas'
    print('Total mark ',total)
    return redirect(url_for(res,score=total))

if __name__=='__main__':
    app.run(debug=True)