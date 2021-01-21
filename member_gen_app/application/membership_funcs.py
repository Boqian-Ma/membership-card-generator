from member_gen_app.application import FONT_PATH
from PIL import Image, ImageFont, ImageDraw 
import os
from application import app, BASE_IMAGE_DIR, MEMBER_IMAGE_DIR, FONT_PATH
from werkzeug.utils import secure_filename
# my_image = Image.open("asset/Standard-Card-Template.png")


BASE_IMAGES = {
    "BR" : BASE_IMAGE_DIR + "/BR_base.jpg",
    "CT" : BASE_IMAGE_DIR + "/CT_base.jpg",
    "CU" : BASE_IMAGE_DIR + "/CU_base.jpg",
    "D" : BASE_IMAGE_DIR + "/D_base.jpg", 
    "RE" : BASE_IMAGE_DIR + "/RE_base.jpg"
}

# Types of certified traders in different currencies
CERTIFIED_TRADER = ["CAT", "CUT", "CCT", "CST"]

def create_user_folder(first_name, last_name, UID):
    """
    Create a folder in "../members" for this member

    Returns: (string) path to new folder
    """
    dir_name = first_name + "-" + last_name + "-" + UID
    curr_path = os.getcwd()
    curr_path += "/members"
    path = os.path.join(curr_path, dir_name)
    print("path " + path)
    try:
        os.mkdir(path)
        os.chmod(path, 666)
    except FileExistsError:
        return path
    return path



def get_form_data(form):
    """Cleans up form data 

    Args:
        form ([type]): [description]
    Returns:
        dict (dictionary): key-value pairs of data
    """
    dict = {
        "first_name" : form.get("firstName"),
        "last_name" : form.get("lastName"),
        "UID" : form.get("cardNumber"),
        "wallet_address" : form.get("walletAddress"),
        "user_type" : form.get("userType"),
        "start_month" : form.get("startMonth"),
        "start_year" : form.get("startYear"),
        "end_month" : form.get("endMonth"),
        "end_year" : form.get("endYear"),
        "card_type" : form.get("userType"),
    }

    if form.get("userType") in CERTIFIED_TRADER:
        dict["user_type"] = "CT"

    return dict

# def save_qr_code(file, data):
#     filename = secure_filename(file.filename)
#     file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#     return os.path.join(app.config['UPLOAD_FOLDER'], filename)

def generate_image(data, qr_path):
    base = Image.open(BASE_IMAGES[data["user_type"]])
    logo = Image.open(qr_path)

    base_w, base_h = base.size
    QRSIZE = int(base_w/7)
    # Resize image to keep ratio
    logo = logo.resize((QRSIZE, QRSIZE), Image.ANTIALIAS)
    base = base.resize((1005, 639), Image.ANTIALIAS)
    logo_w, logo_h = logo.size
    # QR code offset
    offset_w = round(5.5 * logo_w)
    offset_h = round(2.5 * logo_h)
    offset = (offset_w, offset_h)
    # Paste qr code
    base.paste(logo, offset)
    title_size = 30
    wallet_size = 20
    title_font = ImageFont.truetype(FONT_PATH, title_size)
    # title_font = ImageFont.truetype("/Library/Fonts/Monaco.dfont", title_size)
    wallet_font = ImageFont.truetype(FONT_PATH, wallet_size)

    # offsets
    member_id_text = data["user_type"] + "-" + data["UID"]
    member_id_text_offset_w = 90
    member_id_text_offset_h = 250

    name_text = "NAME: " + data["first_name"] + " " + data["last_name"]
    name_text_offset_w = 90
    name_text_offset_h = 290
    name_text_offset = (name_text_offset_w, name_text_offset_h)


    UID_text = "UID: " + data["UID"]
    UID_text_offset_w = 90
    UID_text_offset_h = 330
    UID_text_offset = (UID_text_offset_w, UID_text_offset_h)


    coin_types = ["ETH", "BTC", "PMGT"]
    coin_text = " | ".join(coin_types)
    coin_text_offset_w = 90
    coin_text_offset_h = 500
    UID_text_offset = (coin_text_offset_w, coin_text_offset_h)


    wallet_text = data["wallet_address"]
    wallet_text_offset_w = 90
    wallet_text_offset_h = 550
    wallet_text_offset = (wallet_text_offset_w, wallet_text_offset_h)


    valid_dates_text = "VALID DATES"
    valid_dates_text_offset_w = round(5.5 * logo_w) - 25
    valid_dates_text_offset_h = round(3.5 * logo_h) + 5
    valid_dates_text_offset = (valid_dates_text_offset_w, valid_dates_text_offset_h)

    from_date_text = data["start_month"] + "/" + data["start_year"]
    to_date_text = data["end_month"] + "/" + data["end_year"]
    date_text = from_date_text + " - " + to_date_text
    date_text_offset_w = valid_dates_text_offset_w + 45
    date_text_offset_h = valid_dates_text_offset_h + 35

    image_editable = ImageDraw.Draw(base)
    add_shadow(image_editable, name_text_offset_w, name_text_offset_h, name_text, title_font)
    add_shadow(image_editable, UID_text_offset_w, UID_text_offset_h, UID_text, title_font)
    add_shadow(image_editable, member_id_text_offset_w, member_id_text_offset_h, member_id_text, title_font)
    add_shadow(image_editable, coin_text_offset_w, coin_text_offset_h, coin_text, title_font)
    add_shadow(image_editable, wallet_text_offset_w, wallet_text_offset_h, wallet_text, wallet_font)
    add_shadow(image_editable, valid_dates_text_offset_w, valid_dates_text_offset_h, valid_dates_text, title_font)
    add_shadow(image_editable, date_text_offset_w, date_text_offset_h, date_text, wallet_font)
    # image_editable.text((300, 200), "yeet", font=title_font, fill=(0,0,0,0))
    
    image_name = data["first_name"] + "-" + data["last_name"] + "-" + data["user_type"] + "-" + data["UID"]
    
    # save_path = MEMBER_IMAGE_DIR + "/members"
    path = os.path.join(MEMBER_IMAGE_DIR, image_name)
    base.show(path + image_name + ".png")
    base.convert('RGB').save(path + ".png", "PNG", optimize=True)


def generate_membership_card(form, qr_path):
    data = get_form_data(form)
    generate_image(data, qr_path)


def add_shadow(image_editable, offset_w, offset_h, text, font):
    """Add shadow around text

    Args:
        image_editable (): [description]
        offset_w (int): x offset pixels
        offset_h (int): y offset pixels
        text (string): Text 
        font (ImageFont): text font
    """
    shadow = (52, 56, 53, 100)
    text_color = (52, 56, 53, 250)
    image_editable.text((offset_w - 1 , offset_h), text, font=font, fill=shadow)
    image_editable.text((offset_w + 1 , offset_h), text, font=font, fill=shadow)
    image_editable.text((offset_w, offset_h - 1), text, font=font, fill=shadow)
    image_editable.text((offset_w, offset_h + 1), text, font=font, fill=shadow)
    image_editable.text((offset_w - 1 , offset_h - 1), text, font=font, fill=shadow)
    image_editable.text((offset_w + 1 , offset_h - 1), text, font=font, fill=shadow)
    image_editable.text((offset_w - 1, offset_h + 1), text, font=font, fill=shadow)
    image_editable.text((offset_w + 1, offset_h + 1), text, font=font, fill=shadow)
    image_editable.text((offset_w, offset_h), text, font=font, fill=text_color)

