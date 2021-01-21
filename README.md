# Membership generation app

# To Run 
- Install python virtual environment 
- Start new virtual environment with ```python3 -m venv member_gen_app/venv```
- ```pip3 install -r member_gen_app/requirements.txt```
- Modify the following globals 
    - UPLOAD_FOLDER -> absolute path to ```member_gen_app/application/uploads```
    - BASE_IMAGE_DIR -> absolute path to ```member_gen_app/application/asset/base```
    - MEMBER_IMAGE_DIR -> absolute path to ```members```
- Modify paths in app.command in root directory
- Run ```app.command```

# Tech Stack
- Python3 
- Flask
- Bootstrap 5.0
