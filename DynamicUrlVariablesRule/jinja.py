## Buildiing URL dynamiclly
## variable rule
## Jinja 2 template engine

"""
{{ }} Expressions to print output in html
{%...%} conditions, for loops
{#...#} this is for comments
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask Tutrial</H1></html>"

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html') 

@app.route("/about")
def about():
    return render_template('about.html') 



# @app.route('/submit',methods=['GET','POST'])
# def submit():
#     if request.method=='POST':
#         name = request.form['name']
#         return f'Hello {name}!'
#     return render_template('form.html')


  #  variable rule
# @app.route('/success/<int:score>')
# def success(score):
#     return "The marks you got is " + str(score)

#variable rule
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    return render_template('result.html', result=res)

@app.route('/successres/<int:score>')
def successres(score):
    res = ""
    if score >= 50:
        res = "PASSED"
    else:
        res = "FAILED"

    exp = {'score':score, 'res':res}

    return render_template('result1.html', result=exp)


# if condition
@app.route('/successif/<int:score>')
def successif(score):

    return render_template('result2.html', result=score)




@app.route('/fail/<int:score>')
def fail(score):

    return render_template('result2.html', result=score)


@app.route("/submit", methods=['GET', 'POST'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        history = float(request.form['history'])
        Data_science = float(request.form['Data_science'])

        total_score = (science + maths + history + Data_science) / 4
    else:
        return render_template('getresults.html')
    return redirect(url_for('successres', score=total_score))


if __name__=="__main__":
    app.run(debug=True)