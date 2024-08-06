## integrate HTML with flask also called as jinja 2 techninq
## HTTP web GET and POST

###############Building Url Dynamically; variable rules########################
from flask import Flask, redirect,url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('index.html')


@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score >= 50:
        res ="pass"
    else:
        res = "Fail"
    return render_template('result.html',result=res)

@app.route("/Fail/<int:score>")
def Fail(score):
    return "the person has failed and the mark is "+ str(score)

#result checker
@app.route("/results/<int:marks>")
def results(marks):
    result=""
    if marks<50:
        result='Fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))

#result checker submit  html page
@app.route("/submit", methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method=="POST":
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science+maths+c+data_science)/4
    res = ""
    return redirect(url_for('success',score=total_score))



if __name__=="__main__":
    app.run(debug=True)