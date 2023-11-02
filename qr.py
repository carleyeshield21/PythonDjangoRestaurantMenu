import qrcode

qr_code_image = qrcode.make('https://127.0.0.1:8000')
qr_code_image.save('qr_code_image.png')