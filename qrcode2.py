import qrcode
import PIL
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)                                                        #QRCode=it can chang the fuctionality(border,colour,etc)
 
qr.add_data("")
qr.make(fit=True)
img=qr.make_image(fill_color="green",back_color="white")
img.save("hdproject_qr.png") 