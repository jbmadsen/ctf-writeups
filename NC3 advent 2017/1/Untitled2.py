import csv
from PIL import Image

data = []

with open('/Users/Jacob/Desktop/secret3', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        data.extend(row)


t = [int(x, 16) for x in data]
lim = t[0::3]

print lim[0:20]

im = Image.new('L', (300, 300))
im.putdata(t)
im.show()
im.save('/Users/Jacob/Desktop/secret_image.png')

# AH_HE_IS_A_DUMB_KID_BUT_HE_IS_A_AN_ABOVE_AVERAGE_DOG_ROLL_OVER_SON
