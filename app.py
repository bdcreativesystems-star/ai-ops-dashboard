from flask import Flask, render_template, request, redirect
from automations.file_organizer import organize_files
from automations.system_report import generate_report

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/run-organizer", methods=["POST"])
def run_organizer():
    folder = request.form["folder"]
    organize_files(folder)
    return redirect("/")

@app.route("/system-report")
def system_report():
    report = generate_report()
    return report

if __name__ == "__main__":
    app.run(debug=True)
