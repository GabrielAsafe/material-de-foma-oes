from app import app
from flask import render_template
# #define a url pro site

@app.route("/index/<name>")
@app.route("/index", defaults={'name' : None})
def main(name):#cria a pg principal chamada index
    return render_template("base.html", name= name)

@app.route("/c")
def c():
    return render_template("child.html")


@app.route("/Hello", defaults={'name' : None})
@app.route("/Hello/<name>")
def Hello(name):
    if name:
        return f"olá {name}"
    
    else:
        return "Sai daqui"