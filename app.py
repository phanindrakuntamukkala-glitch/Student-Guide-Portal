from flask import Flask, render_template, request, redirect

app = Flask(__name__)
students = {

    "phani@gmail.com": {
        "password": "1234",
        "name": "KUNTAMUKKALA PHANINDRA CHOWDARY",
        "father": "Kuntamukkala Srinivasa Rao",
        "mother": "Kuntamukkala Narmada",
        "dob": "29/10/2005",
        "course": "B.Tech",
        "department": "Artificial Intelligence & Machine Learning",
        "branch": "Computer Science & Engineering",
        "section": "CSE-VII",
        "semester": "6",
        "roll": "74",
        "university_roll": "2301010386",
        "email": "phani@gmail.com",
        "phone": "7569462957",
        "cgpa": "8.75",
        "attendance": "92%",
        "credits": "132",
        "backlogs": "0",
        "photo": "students/phani.jpg"
    },

    "madhu@gmail.com": {
        "password": "1234",
        "name": "MADHU SANGEETHA KOLETI",
        "father": "Koleti Upendar Rao",
        "mother": "Koleti Anitha",
        "dob": "16/05/2005",
        "course": "B.Tech",
        "department": "Computer Science",
        "branch": "Computer Science & Engineering",
        "section": "CSE-VII",
        "semester": "6",
        "roll": "75",
        "university_roll": "2301010387",
        "email": "madhu@gmail.com",
        "phone": "9573379009",
        "cgpa": "8.20",
        "attendance": "89%",
        "credits": "130",
        "backlogs": "0",
        "photo": "students/madhu.jpg"
    },

    "himaja@gmail.com": {
        "password": "1234",
        "name": "KUNTAMUKKALA HIMAJASRI",
        "father": "Kuntamukkala Srinivasarao",
        "mother": "Kuntamukkala Narmada",
        "dob": "18/06/2007",
        "course": "B.Tech",
        "department": "Information Technology",
        "branch": "Information Technology",
        "section": "IT-VI",
        "semester": "6",
        "roll": "76",
        "university_roll": "2301010388",
        "email": "himaja@gmail.com",
        "phone": "7815850791",
        "cgpa": "9.10",
        "attendance": "95%",
        "credits": "132",
        "backlogs": "0",
        "photo": "students/himaja.jpg"
    },

    "laharika@gmail.com": {
        "password": "1234",
        "name": "MEDHARAMETLA LAHARIKA",
        "father": "Medharametla Nageswara Rao",
        "mother": "Medharametla Padma",
        "dob": "29/10/2005",
        "course": "B.Tech",
        "department": "Artificial Intelligence & Machine Learning",
        "branch": "Computer Science & Engineering",
        "section": "AIML-VI",
        "semester": "6",
        "roll": "77",
        "university_roll": "2301010389",
        "email": "laharika@gmail.com",
        "phone": "9346028543",
        "cgpa": "8.45",
        "attendance": "91%",
        "credits": "131",
        "backlogs": "0",
        "photo": "students/laharika.jpg"
    },

    "niharika@gmail.com": {
        "password": "1234",
        "name": "MEDHARAMETLA  NIHARIKA",
        "father": "MEDHARAMETLA Nageswara Rao",
        "mother": "MEDHARAMETLA Padma",
        "dob": "18/01/2005",
        "course": "B.Tech",
        "department": "Electronics & Communication",
        "branch": "ECE",
        "section": "ECE-VI",
        "semester": "6",
        "roll": "78",
        "university_roll": "2301010390",
        "email": "niharika@gmail.com",
        "phone": "8074308340",
        "cgpa": "8.95",
        "attendance": "94%",
        "credits": "132",
        "backlogs": "0",
        "photo": "students/niharika.jpg"
    },

   

}
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"].strip().lower()
        password = request.form["password"]

        print("Email:", email)
        print("Students:", students.keys())

        if email in students and students[email]["password"] == password:
            return render_template(
                "dashboard.html",
                student=students[email]
            )
        else:
            return "Invalid Email or Password"

    return render_template("login.html")



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