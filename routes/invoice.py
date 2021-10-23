from flask import render_template, request, redirect, jsonify
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
    name = request.form["name"]
    mobile = request.form["mobile"]
    bill_controller.add_user(name, mobile)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/bill")
