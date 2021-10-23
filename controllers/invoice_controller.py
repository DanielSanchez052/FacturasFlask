from configdb import get_connection

def add_bill(date, name,price,balance):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("INSERT INTO invoice (date, name,price,balance) VALUES (%s,%s,%s,%s)",(date,name,price,balance))
    cnn.commit()
    cnn.close()

def update_bill(name,mobile,active,id):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("UPDATE user SET name = %s, mobile = %s, status = %s WHERE id = %s",(name,mobile,active,id))
    cnn.commit()
    cnn.close()

# def delete_user(id):
#     cnn = get_connection()
#     with cnn.cursor() as cursor:
#         cursor.execute("DELETE FROM user WHERE id = %s",(id))
#     cnn.commit()
#     cnn.close()


def get_bills():
    cnn = get_connection()
    bills = []
    with cnn.cursor() as cursor:
        cursor.execute("SELECT I.id, I.date, US.name, I.price, I.balance  FROM user AS US INNER JOIN invoice AS I ON I.id_customer= US.id ORDER BY US.id ASC")
        bills = cursor.fetchall()
    cnn.close()
    return bills

def get_bill_id(id):
    cnn = get_connection()
    bill = None
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, date, US.name, price, balance  FROM user AS US INNER JOIN invoice AS I ON I.id_customer= US.id WHERE US.id = %s",(id))
        bill = cursor.fetchone()
    cnn.close
    return bill
