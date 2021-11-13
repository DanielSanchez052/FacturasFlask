from configdb import get_connection

   
def validateEmail(email):
    cnn = get_connection()
    users = []
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id FROM user where email=%s",(email))
        users = cursor.fetchall()
    cnn.close()
    return users == ()
