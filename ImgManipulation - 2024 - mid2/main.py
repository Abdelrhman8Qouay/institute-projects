# Import required image module {Pillow}
from PIL import Image, ImageFilter, ImageDraw

# Import all the enhancement filter from pillow
from PIL.ImageFilter import (
    BLUR,
    CONTOUR,
    DETAIL,
    EDGE_ENHANCE,
    EDGE_ENHANCE_MORE,
    EMBOSS,
    FIND_EDGES,
    SMOOTH,
    SMOOTH_MORE,
    SHARPEN,
)

# Create image with merge another to main
im1 = Image.open("./alone.jpg")
im2 = Image.open("./ht.jpg")
#resize, first image
image1_size = im1.size
image2_size = im2.size
new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
new_image.paste(im1,(0,0))
new_image.paste(im2,(image1_size[0],0))
new_image.save("./merged_image.jpg","JPEG")
new_image.show()