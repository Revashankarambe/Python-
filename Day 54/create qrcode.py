# import qrcode
# qr = qrcode.make("9238515169@ybl")
# qr.save("My_qrcode.png")
# print("qrcode generated successfully")
# 

import qrcode

data = input("9238515169@ybl ")

qr = qrcode.make(data)
qr.save(r"C:\Users\hp\Desktop\python\Day 54\My_qrcode.png")

print("QR code generated successfully ")