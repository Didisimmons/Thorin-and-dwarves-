import os
from flask import Flask, render_template


app = Flask(__name__) # this creates an instance and The first argument of the Flask class, is the name of the application's module - our package.This informs Flask  where to look for templates and static files.


@app.route("/")# route decorator tells Flask what URL should trigger the function that follows. The "/" indicates browse the root directory that triggers the inndex function 
def index():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)