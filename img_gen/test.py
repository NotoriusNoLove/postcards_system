from PIL import Image

# Открываем основное изображение
background = Image.open(
    r"D:\Projects\postcards_system\storage\core\only_text.png")

# Открываем изображение, которое хотим разместить
image = Image.open(r"D:\Projects\postcards_system\storage\arts\cat.png")

# Убедитесь, что изображение имеет альфа-канал
image_with_alpha = image.convert("RGBA")

# Вычисляем координаты размещения по центру
x = (background.width - image_with_alpha.width) // 2
y = (background.height - image_with_alpha.height) // 2

# Размещаем изображение на основном изображении
background.paste(image_with_alpha, (x, y), mask=image_with_alpha)

# Сохраняем измененное изображение
background.save("result_image.png")
