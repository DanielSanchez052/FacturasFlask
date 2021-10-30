from flask import render_template, request, redirect, jsonify, url_for
from . import routes
from controllers import invoice_controller

@routes.route('/bills')
def bills():
    bills = invoice_controller.get_bills()
    return render_template('invoice/index.html',bills=bills)


@routes.route('/add_bill')
def add_bill():
    return render_template('invoice/add_bill.html')

@routes.route("/save_bill", methods=["POST"])
def save_bill():
    try:
        number = request.form["number"]
        user = request.form["user"]
        price = request.form["price"]
        balance = request.form["balance"]
        date = request.form["date"]
        invoice_controller.add_bill(number,user,price,balance,date)
        return redirect("/bills")
    except:
        return redirect("/bills")

@routes.route('/edit_bill/<int:id>')
def edit_bill(id):
    bill = invoice_controller.get_bill_id(id)
    return render_template('invoice/update_bill.html',bill=bill)

@routes.route('/update_bill', methods=['POST'])
def update_bill():
    # obtener los datos del formulario que invocó este end-point
    id = request.form['id']
    number = request.form["number"]
    price = request.form["price"]
    balance = request.form["balance"]
    date = request.form["date"]
    
    invoice_controller.update_bill(number,price,balance,date, id)
    return redirect('/bills')

@routes.route("/delete_bill", methods=["POST"])
def delete_bill():
    res = invoice_controller.delete_invoice(request.form["id"])
    return redirect(url_for("routes.bills"))
