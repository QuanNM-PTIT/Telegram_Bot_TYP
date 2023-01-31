from PIL import Image

img = Image.open("/Users/jimmy/PycharmProjects/ToiYeuPTIT/Pictures/IMG_1837.jpg")
water_mark = Image.open("/Users/jimmy/PycharmProjects/ToiYeuPTIT/Pictures/Logo.png")

def addWaterMark(x, y, pos):
    transparent = Image.new(mode = 'RGBA', size = img.size, color = 0)
    transparent.paste(img)
    wm_position = (x, y)
    transparent.paste(im = water_mark, box = wm_position, mask = water_mark)
    transparent.save("/Users/jimmy/PycharmProjects/ToiYeuPTIT/Saved/new_image_" + pos + ".png")

img_w, img_h = map(int, img.size)
print(img.size)

# Căn giữa ảnh
water_mark.thumbnail((min(img.size) // 2, min(img.size) // 2))
water_mark_w, water_mark_h = map(int, water_mark.size)

x = img_w // 2 - water_mark_w // 2
y = img_h // 2 - water_mark_h // 2

addWaterMark(x, y, "mid")


water_mark.thumbnail((min(img.size) // 4, min(img.size) // 4))
water_mark_w, water_mark_h = map(int, water_mark.size)

# Căn phải dưới
x = img_w - water_mark_w + img_w // 50
y = img_h - water_mark_h + img_h // 50

addWaterMark(x, y, "bottom_right")

# Căn trái dưới
x = - img_w // 50
y = img_h - water_mark_h + img_h // 50

addWaterMark(x, y, "bottom_left")

# Căn phải trên
x = img_w - water_mark_w + img_w // 50
y = - img_h // 50

addWaterMark(x, y, "upper_right")

# Căn trái trên
x = - img_w // 50
y = - img_h // 50

addWaterMark(x, y, "upper_left")

