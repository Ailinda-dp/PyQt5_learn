import os
from PIL import Image

img_path = "G:\shiyan\PyQt5_learn\src\controls\images/"
files = os.listdir(img_path)
size = (128, 128)
for inName in files:
    tmp = os.path.splitext(inName)
    if tmp[1] == '.JPG':
        outName = tmp[0] + '.ico'
        im = Image.open(img_path + inName).resize(size)
        try:
            path = os.path.join('./images', outName)
            im.save(path)
            print('{}-->{}'.format(inName, outName))
        except IOError:
            print('connot convert :', inName)

