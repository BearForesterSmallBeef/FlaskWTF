from flask import Flask, url_for, render_template


app = Flask(__name__)


@app.route('/')
def main_menu():
    return \
        f'''
        <h1>Миссия Колонизация Марса</h1>
        <ol>
        <li><a href="http:\\index\\123">Index</a>
        <li><a href="http:\\training\\Главный инженер">Training</a>
        <li><a href="http:\\list_prof\\ol">List of profs</a>
        <li><a href="http:\\answer">Ответ</a>
        </ol>
        '''


@app.route('/index/<title>')
def index(title):
    param = {
        'title': title
    }
    return render_template('index.html', **param)


@app.route('/training/<prof>')
def profs(prof):
    if "инженер" in prof or "строитель" in prof:
        param = {
            "img_url": url_for('static', filename='/img/engineer.png'),
            "training_name": "Инженерный тренажер"
        }
    else:
        param = {
            "img_url": url_for('static', filename='/img/scientist.png'),
            "training_name": "Научный симулятор"
        }
    return render_template('profs.html', **param)


@app.route('/list_prof/<mod>')
def list_profs(mod):
    prof = "инженер-исследователь, пилот, строитель, экзобиолог, врач," \
           " инженер по терраформированию, климатолог, специалист по радиационной защите," \
           " астрогеолог, гляциолог, инженер жизнеобеспечения, метеоролог, оператор марсохода," \
           " киберинженер, штурман"
    param = {
        "professions": [i.strip() for i in prof.split(",")],
        "mod": mod
    }
    return render_template('profs_list.html', **param)


@app.route('/answer')
@app.route('/auto_answer')
def answering():
    points = {
        'surname': 'Фамилия',
        'name': 'Имя',
        'education': 'Образование',
        'profession': 'Профессия',
        'sex': 'Пол',
        'motivation': 'Мотивация',
        'ready': 'Готовы остаться на Марсе?'
    }
    answers = {
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на марсе',
        'ready': 'True'
    }
    param = {
        "points": points,
        "answers": answers
    }
    return render_template('param.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
