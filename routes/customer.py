from flask import render_template, request, redirect, jsonify,url_for
from . import routes
from controllers import customer_controller

@routes.route('/customer')
def customer():
    users = customer_controller.get_users()
    return render_template('customer/index.html',users=users)

@routes.route('/customer/<int:id>')
def customerId(id):
    user = customer_controller.get_user_id(id)
    if(user):
        return jsonify({
            "id":user[0],
            "name":user[1],
            "mobile":user[2],
            "active":user[3]
        })
    else:
        return jsonify({
            "message":"no exists",
        })


@routes.route('/add_customer')
def add_customer():
    return render_template('customer/add_customer.html')

@routes.route("/save_customer", methods=["POST"])
def save_customer():
    Identification = request.form["Identification"]
    name = request.form["name"]
    mobile = request.form["mobile"]
    customer_controller.add_user(Identification, name, mobile)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/customer")

@routes.route('/edit_customer/<int:id>')
def edit_customer(id):
    user = customer_controller.get_user_id(id)
    return render_template('customer/update_customer.html',user=user)

@routes.route('/update_customer', methods=['POST'])
def update_customer():
    # obtener los datos del formulario que invocó este end-point
    id = request.form['id']
    name = request.form['name']
    mobile = request.form['mobile']
    active = 1 if 'active' in request.form else 0
    customer_controller.update_user(name,mobile,active, id)
    return redirect('/customer')

@routes.route("/delete_customer", methods=["POST"])
def delete_customer():
    res = customer_controller.delete_user(request.form["id"])
    return redirect(url_for("routes.customer"))

