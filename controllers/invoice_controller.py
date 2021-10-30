from configdb import get_connection

def add_bill(number,user,price,balance,date):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("INSERT INTO invoice (number,id_customer,price,balance,date) VALUES (%s,%s,%s,%s,%s)",(number,user,price,balance,date))
    cnn.commit()
    cnn.close()

def update_bill(number,price,balance,date,id):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("UPDATE invoice SET number = %s, price = %s, balance = %s, date = %s WHERE id = %s",(number,price,balance,date,id))
    cnn.commit()
    cnn.close()

def delete_invoice(id):
    cnn = get_connection()
    balance = get_bill_id(id)[5]
    if balance == 0:
        with cnn.cursor() as cursor:
            cursor.execute("DELETE FROM invoice WHERE id = %s",(id))
        cnn.commit()
        cnn.close()


def get_bills():
    cnn = get_connection()
    bills = []
    with cnn.cursor() as cursor:
        cursor.execute("SELECT I.id, I.date, I.number, US.name, I.price, I.balance  FROM user AS US INNER JOIN invoice AS I ON I.id_customer= US.id ORDER BY US.id ASC")
        bills = cursor.fetchall()
    cnn.close()
    return bills

def get_bill_id(id):
    cnn = get_connection()
    bill = None
    with cnn.cursor() as cursor:
        cursor.execute("SELECT I.id, date, I.number, US.id, price, balance  FROM user AS US INNER JOIN invoice AS I ON I.id_customer= US.id WHERE I.id = %s",(id))
        bill = cursor.fetchone()
    cnn.close
    
    return bill


