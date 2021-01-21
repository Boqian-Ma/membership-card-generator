from flask import Flask
import os

cwd = os.getcwd()
print(cwd)


# Things to modify
UPLOAD_FOLDER = "/Users/sdce/Documents/GitHub/membership-card-generator/member_gen_app/application/uploads"
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
# Get abslute path to base image filder
BASE_IMAGE_DIR = "/Users/sdce/Documents/GitHub/membership-card-generator/member_gen_app/application/asset/base"
# Path to members saving filder
MEMBER_IMAGE_DIR = "/Users/sdce/Documents/GitHub/membership-card-generator/members"


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "/Users/sdce/Documents/GitHub/membership-card-generator/member_gen_app/application/uploads"

from application import routes

#/Users/sdce/Desktop/acgl/membership_card_gen/member_gen_app/application/uploads