from PIL import Image

logo = Image.open("logo_watermark/Logo_bg.png")

def addLogo(x, y, pos):
    transparent = Image.open("output/output.jpg")
    wm_position = (x, y)
    transparent.paste(im = logo, box = wm_position, mask = logo)
    transparent.save("saved_logo/logo_" + pos + ".jpg")

def processLogo():
    img = Image.open("output/output.jpg")
    img_w, img_h = map(int, img.size)

    logo.thumbnail((min(img.size) // 3.5, min(img.size) // 3.5))
    water_mark_w, water_mark_h = map(int, logo.size)

    # Căn phải dưới
    x = img_w - water_mark_w
    y = img_h - water_mark_h

    addLogo(x, y, "bottom_right")

    # Căn trái dưới
    x = 0
    y = img_h - water_mark_h

    addLogo(x, y, "bottom_left")

    # Căn phải trên
    x = img_w - water_mark_w
    y = 0

    addLogo(x, y, "upper_right")

    # Căn trái trên
    x = 0
    y = 0

    addLogo(x, y, "upper_left")