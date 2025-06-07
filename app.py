from flask import Flask, render_template, request, redirect, url_for
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
auth = HTTPBasicAuth()
UPLOAD_FOLDER = 'static'
FLYER_FILENAME = 'flyer.jpg'

users = {
    "admin": generate_password_hash("frondi123")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users[username], password):
        return username

@app.route('/')
def index():
    return render_template('index.html', flyer_url=url_for('static', filename=FLYER_FILENAME))

@app.route('/admin', methods=['GET', 'POST'])
@auth.login_required
def admin():
    if request.method == 'POST':
        flyer = request.files['flyer']
        if flyer:
            flyer.save(os.path.join(UPLOAD_FOLDER, FLYER_FILENAME))
            return redirect(url_for('index'))
    return render_template('admin.html')
if __name__ == '__main__':
    app.run(debug=True)