__all__ = ['draw_image', 'calculate_font_size']

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


def draw_image(text_img: str) -> str:
    front = 'storage\pixelfont_7.ttf'
    image = Image.open('storage\pict.png')
    font = ImageFont.truetype(
        front, calculate_font_size(text_img, front, 1000))
    draw = ImageDraw.Draw(image)
    width, height = image.size
    text = text_img
    text_bbox = draw.textbbox((0, 0), text, font=font)

    x = (width - text_bbox[2])
    y = (height - text_bbox[3])

    draw.text((x//2, y//2), text, fill=(255, 255, 255), font=font)

    image.save(f'temp/image_{text_img}.jpg')
    return (f'temp/image_{text_img}.jpg')


draw_image('ЗЗЗЗЗЗЗЗЗЗ ЗЗЗЗЗЗЗ')
