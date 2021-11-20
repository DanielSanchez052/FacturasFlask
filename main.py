import os
import config
from flask import Flask,render_template, send_from_directory
from routes import *
from util.auth_decorator import authorization

app = Flask(__name__)
app.config.from_object('config.Config')

app.register_blueprint(routes)

@app.route('/')
@app.route('/index')
@authorization()
def index():
    # users = user_controller.get_users()
    return render_template('index.html')

@app.route('/uploads/<filename>')
@authorization()
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__ == "__main__":
    app.run(port = 4500, debug=True)

