#!/bin/zsh
# Simple script to start a flask server for membership card generation
# By Adam Ma - 21/01/2021


source /Users/sdce/Documents/GitHub/membership-card-generator/member_gen_app/venv/bin/activate
# source /Users/<name>/Desktop/

open http://127.0.0.1:5000/
python3 /Users/sdce/Documents/GitHub/membership-card-generator/member_gen_app/run.py

# python3 /Users/<usr>/Desktop/membership-card-generator/member_gen_app/run.py

