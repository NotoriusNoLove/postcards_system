__all__ = ['draw_image', 'calculate_font_size']

import random
from PIL import Image, ImageDraw, ImageFont


def calculate_font_size(text: str, font_path: str, column_width: int) -> int:
    font_size = 1
    font = ImageFont.truetype(font_path, font_size)
    text_width = font.getsize(text)[0]
    while text_width < column_width:
        font_size += 1
        font = ImageFont.truetype(font_path, font_size)
        text_width = font.getsize(text)[0]
    font_size -= 1
    return font_size


def draw_image(text_img: str, shad: str) -> str:
    front = 'D:\Projects\postcards_system\storage\core\pixelfont_7.ttf'
    image = Image.open(
        r'D:\Projects\postcards_system\storage\core\only_text.png')
    font = ImageFont.truetype(
        front, calculate_font_size(text_img, front, 1000))
    inserted_image = Image.open(
        r"D:\Projects\postcards_system\storage\arts\cat.png")

    width, height = image.size
    text_bbox = ImageDraw.Draw(image).textbbox((0, 0), text_img, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1] + 70

    # Вычисляем координаты размещения изображения по центру
    x = 1500 + random.randint(10, 40)
    y = 500 + random.randint(10, 100)

    # Размещаем изображение по центру
    image.paste(inserted_image, (x, y, x + inserted_image.width,
                y + inserted_image.height), mask=inserted_image)
    x = 50 + random.randint(10, 40)
    y = 500 + random.randint(10, 200)
    image.paste(inserted_image, (x, y, x + inserted_image.width,
                y + inserted_image.height), mask=inserted_image)

    # Размещаем текст по центру
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    draw = ImageDraw.Draw(image)
    draw.text((text_x, text_y), text_img, fill=(255, 255, 255), font=font)
    font = ImageFont.truetype(
        front, calculate_font_size(text_img, front, 1000)//2)
    draw.text((text_x+350, text_y+150), shad, fill=(255, 255, 255), font=font)

    result_path = fr'D:/Projects/postcards_system/storage/temp/image_{text_img}.jpg'
    image.save(result_path)
    return result_path


# draw_image("Данила Гинда", "ШАД-112")
# def draw_image(text_img: str) -> str:
#     front = 'D:\Projects\postcards_system\storage\core\pixelfont_7.ttf'
#     image = Image.open('D:\Projects\postcards_system\storage\core\pict.png')
#     font = ImageFont.truetype(
#         front, calculate_font_size(text_img, front, 1000))
#     draw = ImageDraw.Draw(image)
#     width, height = image.size
#     text = text_img
#     text_bbox = draw.textbbox((0, 0), text, font=font)

#     x = (width - text_bbox[2])
#     y = (height - text_bbox[3])

#     draw.text((x//2, y//2), text, fill=(255, 255, 255), font=font)

#     image.save(
#         f'D:/Projects/postcards_system/storage/temp/image_{text_img}.jpg')
#     return (f'D:/Projects/postcards_system/storage/temp/image_{text_img}.jpg')
