from PIL import Image

def addWaterMark(x, y, pos, water_mark):
    transparent = Image.open("output/output.jpg")
    wm_position = (x, y)
    transparent.paste(im = water_mark, box = wm_position, mask = water_mark)
    transparent.save("saved_watermark/watermark_" + pos + ".jpg")

def processWatermark():
    img = Image.open("output/output.jpg")
    img_w, img_h = map(int, img.size)

    water_mark = Image.open("logo_watermark/Logo.png")

    # Căn giữa ảnh
    water_mark.thumbnail((min(img.size) // 2, min(img.size) // 2))
    water_mark_w, water_mark_h = map(int, water_mark.size)

    x = img_w // 2 - water_mark_w // 2
    y = img_h // 2 - water_mark_h // 2

    addWaterMark(x, y, "mid", water_mark)

    water_mark = Image.open("logo_watermark/Logo.png")

    water_mark.thumbnail((min(img.size) // 4, min(img.size) // 4))
    water_mark_w, water_mark_h = map(int, water_mark.size)

    # Căn phải dưới
    x = img_w - water_mark_w + img_w // 50
    y = img_h - water_mark_h + img_h // 50

    addWaterMark(x, y, "bottom_right", water_mark)

    # Căn trái dưới
    x = - img_w // 50
    y = img_h - water_mark_h + img_h // 50

    addWaterMark(x, y, "bottom_left", water_mark)

    # Căn phải trên
    x = img_w - water_mark_w + img_w // 50
    y = - img_h // 50

    addWaterMark(x, y, "upper_right", water_mark)

    # Căn trái trên
    x = - img_w // 50
    y = - img_h // 50

    addWaterMark(x, y, "upper_left", water_mark)