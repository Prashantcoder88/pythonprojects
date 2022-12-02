import qrcode as qr # alias name as qr
import Image
img =qr.make("https://www.youtube.com/studyforcivilservices") #make string
img.save("studyforcivil_youtube.png")