from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
FLYER_FILENAME = 'flyer.jpg'

@app.route('/')
def index():
    return render_template('index.html', flyer_url=url_for('static', filename=FLYER_FILENAME))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        flyer = request.files['flyer']
        if flyer:
            flyer.save(os.path.join(UPLOAD_FOLDER, FLYER_FILENAME))
            return redirect(url_for('index'))
    return render_template('admin.html')