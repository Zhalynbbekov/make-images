from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

for i in os.listdir('.'):
    if i.endswith('.jpg'):
        img = Image.open(i)
        fn, flext = os.path.splitext(i)

        r = img.convert('L')
        r1 = r.filter(ImageFilter.DETAIL)
        r2 = r1.resize((1080, 1080))
        width, height = r2.size

        point = ImageDraw.Draw(rs2)
        txt = "#Zhalynbekov"
        subject = "WHITE"
        font = ImageFont.truetype("arial.ttf", 80)
        textwidth, textheight = draw.textsize(txt, font)

        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        point.text((x, y), txt, subject, font=font)

        r2.save('GG/{}{}'.format(fn, flext))
