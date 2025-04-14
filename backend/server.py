from flask import Flask, request, render_template
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, template_folder='/media/frontend')

DATABASE = {
    'dbname': os.getenv('POSTGRES_DB'),
    'user': os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASSWORD'),
    'host': os.getenv('DB_HOST')
}

def get_db_connection():
    try:
        conn = psycopg2.connect(**DATABASE)
        return conn
    except psycopg2.Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        raise

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')  

@app.route('/submit', methods=['POST'])
def submit():
    action = request.form.get('action')
    message = ""

    try:
        conn = get_db_connection()
        cur = conn.cursor()

        if action == 'Login':
            username = request.form.get('username')
            password = request.form.get('password')

            cur.execute(
                'SELECT * FROM users WHERE username = %s AND password = %s', 
                (username, password)
            )
            user = cur.fetchone()

            message = "Успешный вход!" if user else "Неправильные имя пользователя или пароль!"

        elif action == 'Register':
            new_username = request.form.get('new_username')
            new_password = request.form.get('new_password')

            cur.execute('SELECT * FROM users WHERE username = %s', (new_username,))
            if cur.fetchone():
                message = "Пользователь уже существует!"
            else:
                cur.execute(
                    'INSERT INTO users (username, password) VALUES (%s, %s)', 
                    (new_username, new_password)
                )
                conn.commit()
                message = "Успешная регистрация!"

        else:
            message = "Неизвестное действие"

    except psycopg2.Error as e:
        conn.rollback()
        message = f"Ошибка базы данных: {e}"
    finally:
        if 'cur' in locals():
            cur.close()
        if 'conn' in locals():
            conn.close()

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)