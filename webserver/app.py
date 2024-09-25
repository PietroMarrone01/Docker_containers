import os
import psycopg2 # type: ignore
from flask import Flask # type: ignore

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'webapp')
DB_USER = os.getenv('DB_USER', 'webapp_user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'securepassword')

def get_name_from_db():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM users LIMIT 1;")
        name = cursor.fetchone()[0]
        return name
    except (psycopg2.DatabaseError, TypeError, IndexError) as e:
        app.logger.error(f"Database error: {e}")
        return "Guest"
    finally:
        conn.close()

@app.route('/')
def hello():
    name = get_name_from_db()
    return f"Hello world, {name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)


    