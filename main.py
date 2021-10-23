from flask import Flask
from routes import *

app = Flask(__name__)

app.register_blueprint(routes)

@app.route('/')
@app.route('/index')
def index():
    # users = user_controller.get_users()
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port = 4500, debug=True)

