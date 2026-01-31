from docutils.nodes import image
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/abc")
def abc():
    return render_template('abc.html')

@app.route("/<name>")
def name(name):
    image="203845197.jpg"
    return render_template('name.html', name=name, image=image)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
