from PIL import Image

img = Image.open('pillow-2.jpg')
area = (80, 20, 500, 375)
cropped_img = img.crop(area)

# Display OG
img.show()

# Display Cropped
cropped_img.show()