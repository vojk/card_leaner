from flask import Flask, render_template, request
import db

app = Flask(__name__)

db.init_db()


@app.route('/cards/<string:card_set_id>')
def cards(card_set_id):
    _card_set_id = card_set_id
    return render_template('windows/card_wind.html', defs=db.get_data_from_db(_card_set_id))


@app.route('/')
def main_app():
    conn = db.connection_for_db()
    records = conn.execute("SELECT * FROM card_sets").fetchall()
    conn.close()
    return render_template('interpter.html', defs=records)


@app.route('/cards/overview')
def card_overview():
    conn = db.connection_for_db()
    records = conn.execute("SELECT * FROM card_sets").fetchall()
    conn.close()
    return render_template('card_overview.html', defs=records)


@app.route('/cards/add/', methods=["POST", "GET"])
def add_cards():
    if request.method == "POST":
        name = request.form['_name_form']
        question = request.form['_question_form']
        answer = request.form['_answer_form']
        conn = db.connection_for_db()
        check_for_card_set = conn.execute("SELECT * FROM card_sets WHERE name = ?", (name,)).fetchone()
        if not check_for_card_set:
            conn.execute("INSERT INTO card_sets (name) VALUES (?)", (name,))
            conn.commit()
        _id = conn.execute("SELECT id FROM card_sets WHERE name = ?", (name,)).fetchall()
        conn.execute("INSERT INTO quizes (questions, answers, card_set) VALUES (?,?,?)", (question, answer, _id[0][0],))
        conn.commit()
        conn.close()
        return "Done"
    return render_template('windows/create_wind.html')


if __name__ == '__main__':
    app.run()
