from configdb import get_connection
from werkzeug.security import generate_password_hash as genph
from werkzeug.security import check_password_hash as checkph

def register_user(name, email, password, photo):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("INSERT INTO user (name, email, password, photo) VALUES (%s, %s, %s, %s)",(name, email, get_password(password), photo))
    cnn.commit()
    cnn.close()

def get_password(password):
    return genph(password)