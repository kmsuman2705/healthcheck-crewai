from flask import Flask, render_template, request
from generate_report import generate_system_report

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        result = generate_system_report()  # Call function to generate the report
    return render_template("index.html", result=result)
