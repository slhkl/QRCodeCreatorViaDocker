import qrcode  
import os

obj_qr = qrcode.QRCode(  
    version = 1,  
    error_correction = qrcode.constants.ERROR_CORRECT_L,  
    box_size = 10,  
    border = 4,  
)
data = os.getenv("data")
obj_qr.add_data(data)  
obj_qr.make(fit = True)  
qr_img = obj_qr.make_image()
qr_img.save("QrCode.png")  