"""Dеб приложение, которое позволяет зарегистрировать посетителя.
Данные посетителя заносятся в базу данных MySQL, и могут быть выведены по ссылке /log """
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db_config = {'database': 'log_of_residents',
             'host': '127.0.0.1',
             'user': 'reception',
             'password': 'password', }


def log_request(req: 'flask request'):
    """Добавление данных в базу данных"""
    conn = mysql.connector.connect(**db_config)
    client = conn.cursor()
    sql = """insert into log
                   (name, sex, age, room, phone)
                   values
                   (%s, %s, %s, %s, %s)"""
    client.execute(sql, (req.form['name'],
                         req.form['sex'],
                         req.form['age'],
                         req.form['room'],
                         req.form['phone'],))
    conn.commit()
    client.close()
    conn.close()


@app.route('/')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='REGISTRATION')


@app.route('/registration', methods=['POST'])
def reg_page() -> 'html':
    log_request(request)
    return render_template('reg.html',
                           the_title='REGISTRATION',
                           the_name=request.form['name'],
                           the_sex=request.form['sex'],
                           the_age=request.form['age'],
                           the_room=request.form['room'],
                           the_phone=request.form['phone'],)


@app.route('/log')
def view_log():
    """Отображение содержимого из таблицы log"""
    contents = list()
    conn = mysql.connector.connect(**db_config)
    client = conn.cursor()
    sql = """select name, sex, age, room, phone from log"""
    client.execute(sql)
    log = client.fetchall()
    for line in log:
        contents.append([])
        for item in line:
            contents[-1].append(item)
    title = ('name', 'sex', 'age', 'room', 'phone')
    conn.commit()
    client.close()
    conn.close()
    return render_template('viewlog.html',
                           the_title='Log',
                           the_row_titles=title,
                           the_data=contents)


if __name__ == '__main__':
    app.run(debug=True)
