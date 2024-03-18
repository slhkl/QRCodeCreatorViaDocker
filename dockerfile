FROM python:3.8

WORKDIR /app/qrCodeCreator
RUN pip install qrcode pillow
CMD [ "python", "./main.py" ]