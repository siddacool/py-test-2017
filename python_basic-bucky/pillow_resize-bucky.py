from PIL import Image

maaan = Image.open('pillow-2.jpg')
square_it = maaan.resize((250, 250))
flip_baby = maaan.transpose(Image.FLIP_LEFT_RIGHT)
spin_baby = maaan.transpose(Image.ROTATE_90)

square_it.show()
flip_baby.show()
spin_baby.show()