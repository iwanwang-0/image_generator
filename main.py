from email.mime import image
import os
from re import I
from sqlite3 import Row
from turtle import color, position
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import openpyxl



def draw_img(image, name, country, type):
    image.paste((255, 255, 255, 100), (145, 960, 655, 1060))

    draw = ImageDraw.Draw(image)
    name_font = ImageFont.truetype("MesloLGS NF Italic.ttf", 40)
    country_font = ImageFont.truetype("MesloLGS NF Italic.ttf", 20)
    type_font = ImageFont.truetype("MesloLGS NF Italic.ttf", 20)

    bbox = image.getbbox()
    imgWidth = bbox[2] - bbox[0]

    text_size = get_font_render_size(name, name_font)
    text_x = (imgWidth - text_size[0]) / 2
    # print("text_x: {0}", text_x)
    draw.text((text_x, 970), name, fill=(255, 255, 255, 255), align='center', font=name_font)

    text_size = get_font_render_size(country, country_font)
    text_x = (imgWidth - text_size[0]) / 2
    # print("text_x: {0}", text_x)
    draw.text((text_x, 1025), country, fill=(255, 255, 255, 255), align='center', font=country_font)

    text_size = get_font_render_size(type, type_font)
    text_x = 665 - text_size[0] - 20
    # print("text_x: {0}", text_x)
    draw.text((text_x, 1025), type, fill=(255, 0, 0, 255), align='center', font=type_font)

def get_font_render_size(text, font):
    canvas = Image.new("RGB", (2048, 2048))
    draw = ImageDraw.Draw(canvas)
    draw.text((0, 0), text, font=font)
    bbox = canvas.getbbox()
    size = (bbox[2] - bbox[0], bbox[3] - bbox[1])
    return size

# def read_excel(file_name):
#     book = openpyxl.load_workbook(file_name)
#     sheet = book['Sheet1']
#     for row in sheet.rows:
#         print(row[0].value, "\t\t\t\t\t\t\t", row[1].value, "\t\t\t\t\t\t\t", row[2].value)
#     book.close()

if '__main__' == __name__:
    print("start")

    # read_excel("players.xlsx")

    type_arr = ["Black diamond", "Gold", "Silver", "Bronze", "Common"]

    book = openpyxl.load_workbook("players.xlsx")
    sheet = book['Sheet1']
    for i in range(0, len(list(sheet.rows))):
        if i == 0:
            continue
        row = list(sheet.rows)[i]
        
        name = row[0].value
        country = row[1].value
        position = row[2].value

        for j in range(0, len(type_arr)):
            player_type = type_arr[j]
            # print(i, name, "\t\t\t\t\t\t\t", country, "\t\t\t\t\t\t\t", position, "\t\t\t\t", player_type)
            image = Image.open("default.png")
            image = image.convert('RGBA')
            draw_img(image, name, country, player_type)
            imageName = "./imgs/" + str(i - 1) + "_" + str(j) + ".png"
            print(imageName)
            image.save(imageName)
            image.close()
        
    book.close()

    # for i in range(0, 5):
    #     image = Image.open("default.png")
    #     image = image.convert('RGBA')
    #     draw_img(image, "LIONEL MESSI", "ARGENTINA", "Gold")
    #     imageName = "./imgs/" + str(i) + ".png"
    #     image.save(imageName)
    

