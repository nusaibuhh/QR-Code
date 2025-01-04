import pyqrcode

url = 'https://www.youtube.com/watch?v=UNaYpBpRJOY'
qr_code = pyqrcode.create(url)
filename = 'qrcode.png'
qr_code.png(filename, scale=8)

import os
os.system(f'start {filename}')

#this code will generate a qr code for the given url and open it in the default image viewer. you can change the url to any other url you want to generate a qr code for.