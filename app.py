# This exam result app
from flask import Flask, render_template,request,redirect
# This is push1
app=Flask(__name__)
@app.route('/')
def home():
    return "This is Home page"

@app.route('/success')
def success():
    return "You have passed the exam1"
@app.route('/fail')
def fail():
    return "You have failed"
@app.route('/calculate',methods=['POST','GET'])
def calculate():
     
    if request.method=='GET':
        return render_template('calculate.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        average_marks=(maths+science+history)/3
        result=""
        if average_marks>=50:
            result='success'
        else:
            result='fail'

        return render_template('result.html',results=average_marks)

if __name__=='__main__':
    app.run(debug=True)


