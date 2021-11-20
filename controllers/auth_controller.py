from email import message
from configdb import get_connection
from werkzeug.security import generate_password_hash as genph
from werkzeug.security import check_password_hash as checkph
from pymysql.err import IntegrityError

def register_user(name, email, password, photo):
    try:
        cnn = get_connection()
        with cnn.cursor() as cursor:
            cursor.execute("INSERT INTO user (name, email, password, photo) VALUES (%s, %s, %s, %s)",(name, email, get_password(password), photo))
        cnn.commit()
        cnn.close()
        return 'OK',True
    except IntegrityError as e:
        code, mesg = e.args
        return f'el {mesg.split(" ")[-1]} es invalido intentalo de nuevo',False

def get_password(password):
    return genph(password)

def checkPassword(email,password):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("SELECT password FROM user where email=%s",(email))
        userHash = cursor.fetchall()[0]
    cnn.close()
    return checkph(userHash[0], password)