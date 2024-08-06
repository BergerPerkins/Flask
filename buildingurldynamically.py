#################    Building Url Dynamically     ######################
################# variable rules and url building########################
from flask import Flask, redirect,url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Berger"

@app.route("/success/<int:score>")
def success(score):
    return "the person has passesd and the mark is "+ str(score)

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


if __name__=="__main__":
    app.run(debug=True)