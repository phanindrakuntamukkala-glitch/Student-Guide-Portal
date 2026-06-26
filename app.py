from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email == "phani@gmail.com" and password == "1234":
            return redirect("/dashboard")
        else:
            return "Invalid Email or Password"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/timetable")
def timetable():
    return render_template("timetable.html")

@app.route("/fees")
def fees():
    return render_template("fees.html")

@app.route("/assignments")
def assignments():
    return render_template("assignments.html")

@app.route("/study-materials")
def study_materials():
    return render_template("study_materials.html")

@app.route("/results")
def results():
    return render_template("results.html")

@app.route("/attendance")
def attendance():
    return render_template("attendance.html")

@app.route("/cgpa")
def cgpa():
    return render_template("cgpa.html")

@app.route("/exam-apply")
def exam_apply():
    return render_template("exam_apply.html")

@app.route("/admit-card")
def admit_card():
    return render_template("admit_card.html")

@app.route("/library")
def library():
    return render_template("library.html")

@app.route("/academic-calendar")
def academic_calendar():
    return render_template("academic_calendar.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")


@app.route("/ai-assistant", methods=["GET", "POST"])
def ai_assistant():

    answer = ""

    if request.method == "POST":

        question = request.form["question"].lower()

        if "ai" in question:
            answer = "Artificial Intelligence is the simulation of human intelligence by machines."

        elif "dbms" in question:
            answer = "DBMS is software used to store, retrieve and manage databases."

        elif "os" in question or "operating system" in question:
            answer = "An Operating System manages computer hardware and software resources."

        elif "python" in question:
            answer = "Python is a high-level programming language used in AI, web development and automation."

        else:
            answer = "I don't know this answer yet. Connect me with Gemini or OpenAI API for smarter responses."

    return render_template("ai_assistant.html", answer=answer)

import os

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )