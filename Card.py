from PIL import Image, ImageDraw, ImageFont
import QR


def cardName(id):
    levvel = QR.getLevelfromID(id)
    if levvel == 1:
        img = Image.open('petraChildrenCampLevel1.png')
    elif levvel == 2:
        img = Image.open('petraChildrenCampLevel2.png')
    
    name = QR.get_name_from_id(id)
    print(name)
    

    drawName = ImageDraw.Draw(img)
    drawName.text((500, 300), text=name, fill='black', font= ImageFont.truetype('arial.ttf', 50))
    img.save(f"{name}.png")




