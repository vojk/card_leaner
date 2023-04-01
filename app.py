from flask import Flask, render_template
import db

app = Flask(__name__)

db.init_db()

@app.route('/')
def main_app():
    return render_template('interpter.html', defs=db.get_data_from_db())





if __name__ == '__main__':
    app.run()
