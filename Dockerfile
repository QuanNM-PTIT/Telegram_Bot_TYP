FROM python:3.10-alpine

WORKDIR /bot_code

COPY ["../", "./bot_tele"]

WORKDIR /bot_code/bot_tele

RUN pip3 install -r requirements.txt

CMD ["python3", "bot.py"]  