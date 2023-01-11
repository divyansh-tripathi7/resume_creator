from flask import Flask



app = Flask(__name__)




@app.route("/")
def index():
    with open("tex_files/resume.tex", "r") as f_in:
        data = f_in.read()
    print(data)
    data = data
    return f'{data}'