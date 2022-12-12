FROM python:3.11

WORKDIR /app/qrCodeCreator
RUN pip install qrcode pillow
CMD [ "python", "./main.py" ]