from PIL import Image, ImageFont, ImageDraw 

# my_image = Image.open("asset/Standard-Card-Template.png")
base = Image.open("application/asset/base/BR_base.jpg")
logo = Image.open("application/asset/eg-qr.png")

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
title_font = ImageFont.truetype("/Library/Fonts/Microsoft/stixgeneral-regular.otf", title_size)
# title_font = ImageFont.truetype("/Library/Fonts/Monaco.dfont", title_size)
wallet_font = ImageFont.truetype("/Library/Fonts/Microsoft/stixgeneral-regular.otf", wallet_size)

# offsets
member_id_text = "BR-199"
member_id_text_offset_w = 90
member_id_text_offset_h = 250
member_id_text_offset = (member_id_text_offset_w, member_id_text_offset_h)

name_text = "NAME: " + "JOHN DOE"
name_text_offset_w = 90
name_text_offset_h = 290
name_text_offset = (name_text_offset_w, name_text_offset_h)


UID_text = "UID: " + "122"
UID_text_offset_w = 90
UID_text_offset_h = 330
UID_text_offset = (UID_text_offset_w, UID_text_offset_h)


coin_types = ["ETH", "BTC"]
coin_text = " | ".join(coin_types)
coin_text_offset_w = 90
coin_text_offset_h = 500
UID_text_offset = (coin_text_offset_w, coin_text_offset_h)


wallet_text = "1j2hg13i872whgy34hb4k1ugxjuygemz"
wallet_text_offset_w = 90
wallet_text_offset_h = 550
wallet_text_offset = (wallet_text_offset_w, wallet_text_offset_h)


valid_dates_text = "VALID DATES"
valid_dates_text_offset_w = round(5.5 * logo_w) - 25
valid_dates_text_offset_h = round(3.5 * logo_h) + 5
valid_dates_text_offset = (valid_dates_text_offset_w, valid_dates_text_offset_h)

from_date_text = "12" + "/" + "09"
to_date_text = "12" + "/" + "09"
date_text = from_date_text + " - " + to_date_text
date_text_offset_w = valid_dates_text_offset_w + 45
date_text_offset_h = valid_dates_text_offset_h + 35




def add_shadow(image_editable, offset_w, offset_h, text, font):
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


# add text
image_editable = ImageDraw.Draw(base)
add_shadow(image_editable, name_text_offset_w, name_text_offset_h, name_text, title_font)
add_shadow(image_editable, UID_text_offset_w, UID_text_offset_h, UID_text, title_font)
add_shadow(image_editable, member_id_text_offset_w, member_id_text_offset_h, member_id_text, title_font)
add_shadow(image_editable, coin_text_offset_w, coin_text_offset_h, coin_text, title_font)
add_shadow(image_editable, wallet_text_offset_w, wallet_text_offset_h, wallet_text, wallet_font)
add_shadow(image_editable, valid_dates_text_offset_w, valid_dates_text_offset_h, valid_dates_text, title_font)
add_shadow(image_editable, date_text_offset_w, date_text_offset_h, date_text, wallet_font)




# image_editable.text((300, 200), "yeet", font=title_font, fill=(0,0,0,0))
base.show()



