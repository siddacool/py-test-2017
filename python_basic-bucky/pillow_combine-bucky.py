from PIL import Image

maaan = Image.open('pillow-2.jpg')
stars_bg = Image.open('pillow-4.jpg')

width, height = maaan.size
stars_w, stars_h = stars_bg.size

top = 100
left = 300
width = (width + left)
height = (height + top)


area = (left, top, width, height)
stars_bg.paste(maaan, area)

stars_bg.show()