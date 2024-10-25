import qrcode
img = qrcode.make("asmongold was wrong")
type(img) # qrcode.image.pill.PilImage
img.save("qrTest.png")