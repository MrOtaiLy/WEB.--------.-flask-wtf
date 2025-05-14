from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
import json
import random

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "static/uploads"
app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg"}


@app.route("/index")
@app.route("/<title>")
def index(title="Заглушка"):
    return render_template("base.html", title=title)


@app.route("/training/<prof>")
def training(prof):
    return render_template("training.html", prof=prof)


@app.route("/list_prof/<list_type>")
def list_prof(list_type):
    professions = [
        "инженер-исследователь",
        "пилот",
        "строитель",
        "экзобиолог",
        "врач",
        "инженер по терраформированию",
        "климатолог",
        "специалист по радиационной защите",
        "астрогеолог",
        "гляциолог",
        "инженер жизнеобеспечения",
    ]
    return render_template(
        "list_prof.html", list_type=list_type, professions=professions
    )


@app.route("/answer", methods=["GET", "POST"])
def answer():
    if request.method == "GET":
        return render_template("answer_form.html")
    else:
        data = {}
        data["title"] = request.form["title"]
        data["surname"] = request.form["surname"]
        data["name"] = request.form["name"]
        data["education"] = request.form["education"]
        data["profession"] = request.form["profession"]
        data["sex"] = request.form["sex"]
        data["motivation"] = request.form["motivation"]
        data["ready"] = request.form["ready"]
        return render_template("auto_answer.html", data=data)


@app.route("/auto_answer")
def auto_answer():
    data = {
        "title": "Анкета",
        "surname": "Watny",
        "name": "Mark",
        "education": "Высшее",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": "True",
    }
    return render_template("auto_answer.html", data=data)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        astronaut_id = request.form.get("astronaut_id")
        astronaut_password = request.form.get("astronaut_password")
        captain_id = request.form.get("captain_id")
        captain_token = request.form.get("captain_token")
        return render_template("login_result.html")
    return render_template("mars_access.html")


@app.route("/distribution")
def distribution():
    astronauts = [
        "Ридли Скотт",
        "Энди Уир",
        "Марк Уотни",
        "Венката Капур",
        "Тедди Сандерс",
        "Шон Бин",
    ]
    return render_template("distribution.html", astronauts=astronauts)


@app.route("/table")
def table():
    sex = request.args.get("sex", "male").lower()
    age = request.args.get("age", "0")
    try:
        age = int(age)
    except ValueError:
        age = 0
    return render_template("table.html", sex=sex, age=age)


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
    )


@app.route("/gallery", methods=["GET", "POST"])
def gallery():
    if request.method == "POST":
        file = request.files["file"]
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return redirect(url_for("gallery"))
    images = os.listdir(app.config["UPLOAD_FOLDER"])
    return render_template("gallery.html", images=images)


@app.route("/member")
def member():
    with open("templates/crew.json", "r", encoding="utf-8") as f:
        crew = json.load(f)
    member = random.choice(crew)
    member["professions"] = sorted(member["professions"])
    return render_template("member.html", member=member)


if __name__ == "__main__":
    app.run(debug=True)
