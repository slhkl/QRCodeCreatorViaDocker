docker build . -t createqrcode

docker run --rm -v C:\Users\P2049\Desktop\Mü\PythonQRCode:/app/qrCodeCreator -e data=https://youtu.be/EX8qEqcQMZE createqrcode

- You need docker if you want to use this way to create QR code.
- This docker image contains python 3.11 version and runs qr create transactions.
- Run this command in terminal to create image.
- docker build . -t createqrcode

- The Docker image does not contain the main.py file.
- Must be run with the volume and give the parent folder of main.py on the volume. (1)
- It should be run with the data environment and the given as data string value. (2) 
- docker run --rm -v 1:/app/qrCodeCreator -e data=2 createqrcode

- Sample transaction
- docker run --rm -v C:\Users\P2049\Desktop\Mü\PythonQRCode:/app/qrCodeCreator -e data=https://youtu.be/EX8qEqcQMZE createqrcode