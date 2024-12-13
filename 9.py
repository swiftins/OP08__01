import gdown
from PIL import Image

# Правильный FILE_ID файла из Google Drive
file_id = "1zL8jGii_TdTouvsmla4hLogQSEuO2DDu"
download_url = f"https://drive.google.com/uc?id={file_id}"

# Скачивание файла
output_file = "image.jpg"
gdown.download(download_url, output_file, quiet=False)

# Проверка: файл должен существовать
import os
if not os.path.exists(output_file):
    print("*********************************  Файл не был скачан. Проверьте URL и доступ.")

# Открытие изображения
try:
    image = Image.open(output_file)
    image.show()
except Exception as e:
    print(f"Ошибка при открытии изображения: {e}")
