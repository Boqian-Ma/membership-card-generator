from flask import render_template, url_for, redirect, request

import os
from application import app 
from application.membership_funcs import generate_membership_card
from werkzeug.utils import secure_filename

@app.route('/')
def index():
    # Get form

    #task_content = request.form[]
    return render_template("index.html")

@app.route('/generate', methods=["POST"])
def generate():
    form = request.form
    file = request.files['qrCode']

    filename = secure_filename(file.filename)
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    qr_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)



    print(qr_path)

    # Secure_filename
    generate_membership_card(form, qr_path)
    print(file.filename)
    return redirect(url_for("index"))


@app.route('/members')
def members():
    return render_template("members.html")