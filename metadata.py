filename = "mx10-32-9-213_2021-06-25_144340_image.jpg"
from PIL import Image, ExifTags

img = Image.open(filename)
# print(dir(img))
# [... 'getexif' ...]

img_exif = img._getexif()
if img_exif:
    # print(type(img_exif))
    # <class 'PIL.Image.Exif'>
    # print(dict(img_exif))
    # { .. 271: 'FUJIFILM', 305: 'Adobe Photoshop Lightroom 6.14 (Macintosh)', }

    img_exif_dict = dict(img_exif)
    for key, val in img_exif_dict.items():
        # print(key, val)
        if key in ExifTags.TAGS:
            print(ExifTags.TAGS[key] + " - " + str(val))
else:
    print("Sorry, image has no exif data.")
from PIL import Image
im = Image.open("tempfile.jpg")
print(im.app["COM"])  # b'JPEG-COMMENT-TEST\x00'