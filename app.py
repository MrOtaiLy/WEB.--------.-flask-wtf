from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/<title>')
@app.route("/index")
def index():
    title = request.args.get("title", "Заглушка")
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


if __name__ == "__main__":
    app.run(debug=True)
