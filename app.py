from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    title = request.args.get('title', 'Заглушка')
    return render_template('base.html', title=title)

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof)

@app.route('/list_prof/<list_type>')
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
        "инженер жизнеобеспечения"
    ]
    return render_template('list_prof.html', list_type=list_type, professions=professions)


if __name__ == '__main__':
    app.run(debug=True)
