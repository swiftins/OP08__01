import gdown
from PIL import Image

# URL общего доступа
file_url = "https://drive.google.com/file/d/1zL8jGii_TdTouvsmla4hLogQSEuO2DDu/view?usp=drive_link"

# Скачивание файла
output_file = "image.jpg"
gdown.download(file_url, output_file, quiet=False)


# Проверяем содержимое файла
with open(output_file, 'rb') as f:
    content = f.read(500)  # Читаем первые 500 байт
    print(content)





# Открытие изображения
image = Image.open(output_file)
image.show()
