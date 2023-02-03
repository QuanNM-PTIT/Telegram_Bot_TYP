from telegram import *
from telegram.ext import *
from addWatermark import processWatermark
from addLogo import processLogo

TOKEN = "6124580913:AAGzSDPm7Y9VZE9ExZQsWQxVdbXyijsqtYA"
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

def start_command(update, context):
    buttons = [[KeyboardButton("/Add_logo_or_watermark")],
               [KeyboardButton("/Get_logo_TYP")]]

    context.bot.send_message(chat_id=update.message.chat.id,
                             reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True),
                             text="Mời bạn chọn chức năng!")

    dp.add_handler(CommandHandler("Add_logo_or_watermark", add_logo_or_watermark_command))
    dp.add_handler(CommandHandler("Get_logo_TYP", get_logo_command))

def add_logo_or_watermark_command(update, context):
    name = update.message.chat.first_name
    update.message.reply_text("Đây là tính năng thêm logo hoặc watermark!\nHãy gửi file ảnh cho tôi, tôi có thể thêm logo hoặc watermark vào ảnh cho bạn!")

    dp.add_handler(MessageHandler(Filters.document, file_handler))

    dp.add_handler(MessageHandler(Filters.photo, image_handler))

    dp.add_handler(CommandHandler("Logo", addLogo))

    dp.add_handler(CommandHandler("Watermark", addWatermark))


def logoUpperLeft(update, context):
    update.message.bot.send_document(document=open("logo_upper_left.jpg", "rb"), chat_id=update.message.chat.id)
    update.message.reply_text("Đã sẵn sàng cho ảnh tiếp theo!")


def logoUpperRight(update, context):
    update.message.bot.send_document(document=open("logo_upper_right.jpg", "rb"), chat_id=update.message.chat.id)
    update.message.reply_text("Đã sẵn sàng cho ảnh tiếp theo!")


def logoBottomLeft(update, context):
    update.message.bot.send_document(document=open("logo_bottom_left.jpg", "rb"), chat_id=update.message.chat.id)
    update.message.reply_text("Đã sẵn sàng cho ảnh tiếp theo!")


def logoBottomRight(update, context):
    update.message.bot.send_document(document=open("logo_bottom_right.jpg", "rb"), chat_id=update.message.chat.id)
    update.message.reply_text("Đã sẵn sàng cho ảnh tiếp theo!")


def watermarkUpperLeft(update, context):
    update.message.bot.send_document(document=open("watermark_upper_left.jpg", "rb"), chat_id=update.message.chat.id)
    update.message.reply_text("Đã sẵn sàng cho ảnh tiếp theo!")


def watermarkUpperRight(update, context):
    update.message.bot.send_document(document=open("watermark_upper_right.jpg", "rb"), chat_id=update.message.chat.id)
    update.message.reply_text("Đã sẵn sàng cho ảnh tiếp theo!")


def watermarkBottomLeft(update, context):
    update.message.bot.send_document(document=open("watermark_bottom_left.jpg", "rb"), chat_id=update.message.chat.id)
    update.message.reply_text("Đã sẵn sàng cho ảnh tiếp theo!")


def watermarkBottomRight(update, context):
    update.message.bot.send_document(document=open("watermark_bottom_right.jpg", "rb"), chat_id=update.message.chat.id)
    update.message.reply_text("Đã sẵn sàng cho ảnh tiếp theo!")


def watermarkMiddle(update, context):
    update.message.bot.send_document(document=open("watermark_mid.jpg", "rb"), chat_id=update.message.chat.id)
    update.message.reply_text("Đã sẵn sàng cho ảnh tiếp theo!")


def addLogo(update, context):
    processLogo()

    buttons = [[KeyboardButton("/Logo_at_the_top_left")],
               [KeyboardButton("/Logo_at_the_top_right")],
               [KeyboardButton("/Logo_at_the_bottom_left")],
               [KeyboardButton("/Logo_at_the_bottom_right")]]

    context.bot.send_message(chat_id=update.message.chat.id,
                             reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True),
                             text="Bạn muốn thêm logo ở vị trí nào?")

    dp.add_handler(CommandHandler("Logo_at_the_top_left", logoUpperLeft))

    dp.add_handler(CommandHandler("Logo_at_the_top_right", logoUpperRight))

    dp.add_handler(CommandHandler("Logo_at_the_bottom_left", logoBottomLeft))

    dp.add_handler(CommandHandler("Logo_at_the_bottom_right", logoBottomRight))


def addWatermark(update, context):
    processWatermark()

    buttons = [[KeyboardButton("/Watermark_in_the_middle")],
               [KeyboardButton("/Watermark_at_the_top_left")],
               [KeyboardButton("/Watermark_at_the_top_right")],
               [KeyboardButton("/Watermark_at_the_bottom_left")],
               [KeyboardButton("/Watermark_at_the_bottom_right")]]

    context.bot.send_message(chat_id=update.message.chat.id,
                             reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True),
                             text="Bạn muốn thêm watermark ở vị trí nào?")

    dp.add_handler(CommandHandler("Watermark_in_the_middle", watermarkMiddle))

    dp.add_handler(CommandHandler("Watermark_at_the_bottom_left", watermarkBottomLeft))

    dp.add_handler(CommandHandler("Watermark_at_the_bottom_right", watermarkBottomRight))

    dp.add_handler(CommandHandler("Watermark_at_the_top_left", watermarkUpperLeft))

    dp.add_handler(CommandHandler("Watermark_at_the_top_right", watermarkUpperRight))


def file_handler(update, context):
    file = update.message.document.get_file()
    file.download("output.jpg")

    update.message.reply_text("Tải lên thành công!")

    buttons = [[KeyboardButton("/Logo")], [KeyboardButton("/Watermark")]]
    context.bot.send_message(chat_id=update.message.chat.id,
                             reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True),
                             text="Bạn muốn thêm logo hay watermark?")

def image_handler(update, context):
    file = update.message.photo[-1].file_id
    obj = context.bot.get_file(file)
    obj.download("output.jpg")

    update.message.reply_text("Tải lên thành công!")

    buttons = [[KeyboardButton("/Logo")], [KeyboardButton("/Watermark")]]
    context.bot.send_message(chat_id=update.message.chat.id,
                             reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True),
                             text="Bạn muốn thêm logo hay watermark?")


def get_logo_command(update, context):
    buttons = [[KeyboardButton("/Round_logo")],
               [KeyboardButton("/Logo_transparent")],
               [KeyboardButton("/Square_logo")]]

    context.bot.send_message(chat_id=update.message.chat.id,
                             reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True),
                             text="Bạn muốn lấy logo nào?")

    dp.add_handler(CommandHandler("Round_logo", get_round_logo))

    dp.add_handler(CommandHandler("Logo_transparent", get_logo_transparent))

    dp.add_handler(CommandHandler("Square_logo", get_square_logo))


def get_round_logo(update, context):
    update.message.bot.send_document(document=open("Round_Logo.png", "rb"), chat_id=update.message.chat.id)


def get_square_logo(update, context):
    update.message.bot.send_document(document=open("Square_Logo.png", "rb"), chat_id=update.message.chat.id)


def get_logo_transparent(update, context):
    update.message.bot.send_document(document=open("Logo_Transparent.png", "rb"), chat_id=update.message.chat.id)

def main():
    print("Started")

    dp.add_handler(CommandHandler("start", start_command))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
