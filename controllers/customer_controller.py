# importar el archivo de la conexión a la BD
from configdb import get_connection

def add_user(id,name,mobile):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("INSERT INTO customer (id,name, mobile) VALUES (%s,%s,%s)",(id,name,mobile))
    cnn.commit()
    cnn.close()

def update_user(name,mobile,active,id):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("UPDATE customer SET name = %s, mobile = %s, status = %s WHERE id = %s",(name,mobile,active,id))
    cnn.commit()
    cnn.close()

def delete_user(id):
    cnn = get_connection()
    user_bills = get_user_bill(id)
    if(user_bills[1] == 0):
        with cnn.cursor() as cursor:
            cursor.execute("DELETE FROM customer WHERE id = %s",(id))
        cnn.commit()
        cnn.close()
        return {"message": 'Se elimina correctamente', "code":True}
    else:
        return {"message": 'Este usuario ya tiene Facturas Registradas', "code":False}
        
def get_users():
    cnn = get_connection()
    users = []
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, mobile, status,(select count(*) from invoice.invoice where id_customer=US.id) invoices FROM customer as US")
        users = cursor.fetchall()
    cnn.close()
    return users

def get_user_id(id):
    cnn = get_connection()
    user = None
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, mobile, status FROM customer WHERE id = %s",(id))
        user = cursor.fetchone()
    cnn.close
    return user

def get_user_bill(id_user):
    cnn = get_connection()
    user = None
    with cnn.cursor() as cursor:
        cursor.execute("SELECT US.id,(select count(*) from invoice.invoice where id_customer=US.id) invoices FROM invoice.customer AS US WHERE US.id=%s",(id_user))
        user = cursor.fetchone()
    cnn.close
    
    return user