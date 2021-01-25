from flask import Flask
import os

cwd = os.getcwd()
print(cwd)


# Things to modify
UPLOAD_FOLDER = "/Users/sdce/Documents/GitHub/membership-card-generator/member_gen_app/application/uploads"
# UPLOAD_FOLDER = "/Users/<usr>/Desktop/membership-card-generator/member_gen_app/application/uploads"



ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
# Get abslute path to base image filder
BASE_IMAGE_DIR = "/Users/sdce/Documents/GitHub/membership-card-generator/member_gen_app/application/asset/base"
# BASE_IMAGE_DIR = "/Users/<usr>/Desktop/membership-card-generator/member_gen_app/application/asset/base"



# Path to members saving filder
MEMBER_IMAGE_DIR = "/Users/sdce/Documents/GitHub/membership-card-generator/members"
# MEMBER_IMAGE_DIR = "/Users/<usr>/Desktop/membership-card-generator/members"

FONT_PATH = "/Library/Fonts/Microsoft/stixgeneral-regular.otf"
# FONT_PATH = "/Library/Fonts/Microsoft/stixgeneral-regular.otf"


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "/Users/sdce/Documents/GitHub/membership-card-generator/member_gen_app/application/uploads"
# app.config['UPLOAD_FOLDER'] = "/Users/<usr>/Desktop/membership-card-generator/member_gen_app/application/uploads"





from application import routes