from PIL import Image

cuc = Image.open('pillow-6.jpg')
asian = Image.open('pillow-7.jpg')
black = Image.open('pillow-5.jpg')

r1, g1, b1 = cuc.split()
r2, g2, b2 = asian.split()
r3, g3, b3 = black.split()

new_img = Image.merge('RGB', (r2, g1, b1))

new_img.show()