from PIL import Image
from PIL import ImageFilter

maaan = Image.open('pillow-7.jpg')
blur = maaan.filter(ImageFilter.BLUR)
detail = maaan.filter(ImageFilter.DETAIL)
edges = maaan.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()