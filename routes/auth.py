from flask import render_template, request, redirect, session, url_for, flash
from . import routes
from controllers import auth_controller
from util.uploadImages import uploadImage
from util.validateEmail import validateEmail
from util.auth_decorator import authorization

@routes.route("/register", methods=["POST","GET"])
def register():
    if request.method=='POST':
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        if 'photo' not in request.files: 
            flash('No selected file', 'error')
            return redirect(request.url)
        else: 
            photo = uploadImage(request.files["photo"])
            
        if not validateEmail(email):
            flash('El Email ya existe', 'error')
            return redirect(request.url)

        if name =='' or password == '':
            flash('Hay campos Vacios', 'error')
            return redirect(request.url)
        else:
            msg,code = auth_controller.register_user(name, email, password, photo)
            if not code:
                flash(msg, 'error')
                return redirect(request.url)
            else:
                return redirect(url_for('routes.login'))
    elif request.method == 'GET':
        return render_template('auth/register.html')


@routes.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST' and 'user' not in session:
        email = request.form["email"]
        password = request.form["password"]

        if not auth_controller.checkPassword(email,password):
            flash('las credenciales introducidas no coinciden intentado de nuevo!', 'error')
            return redirect(request.url)
        else: 
            session['user'] = email
            return redirect(url_for('routes.customer'))
    elif request.method == 'GET' and 'user' not in session:
        return render_template('auth/login.html')
    elif 'user' in session:
        return redirect(url_for('routes.customer'))

@routes.route('/logout', methods=['POST'])
@authorization()

def logout():
    session.pop('user', default=None)
    return redirect(url_for('routes.login'))

