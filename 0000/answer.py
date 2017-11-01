#!/usr/bin/env python
# encoding: utf-8

from PIL import Image, ImageDraw, ImageFont
# get an image
base = Image.open('image/headphoto.jpg').convert('RGBA')

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
fnt = ImageFont.truetype('经典综艺体简.ttf', 160)
# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, full opacity
d.text((380,50), "4", font=fnt, fill=(255,8,28,255))

out = Image.alpha_composite(base, txt)

out.show()

# RGBA 不能转换为 JPEG
# out.save('result.jpg', 'JPEG')
out.save('result.png')
