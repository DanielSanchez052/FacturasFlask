from flask import render_template, request, redirect, jsonify,url_for, flash
from . import routes
from controllers import auth_controller
from util.uploadImages import uploadImage
from util.validateEmail import validateEmail
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
            
        if  validateEmail(email):
            flash('El Email ya existe', 'error')
            return redirect(request.url)

        if name =='' or password == '':
            flash('Hay campos Vacios', 'error')
            return redirect(request.url)
        else:
            auth_controller.register_user(name, email, password, photo)
            return redirect("/")
        
    elif request.method == 'GET':
        return render_template('auth/register.html')