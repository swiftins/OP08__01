import tkinter as tk
from PIL import Image, ImageTk
import pygame
import os

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load(r"C:\\Users\\АСУС\\Downloads\\android.mp3")  # Укажите путь к вашему аудиофайлу
    pygame.mixer.music.play()

def save_tasks_to_file():
    with open("tasks.txt", "w", encoding="utf-8") as file:
        tasks = tasks_listBox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def load_tasks_from_file():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for task in file:
                tasks_listBox.insert(tk.END, task.strip())

def add_task():
    task = task_entry.get()
    if task:
        tasks_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks_to_file()
        play_sound()  # Воспроизведение звука при добавлении задачи

def delete_task():
    selected_task_index = tasks_listBox.curselection()
    if selected_task_index:
        tasks_listBox.delete(selected_task_index)
        save_tasks_to_file()
        play_sound()  # Воспроизведение звука при удалении задачи

def mark_task_done():
    selected_task_index = tasks_listBox.curselection()
    if selected_task_index:
        current_task = tasks_listBox.get(selected_task_index)
        tasks_listBox.delete(selected_task_index)
        tasks_listBox.insert(tk.END, f"{current_task} (done)")
        save_tasks_to_file()
        play_sound()  # Воспроизведение звука при выполнении задачи

def mark_task_important():
    selected_task_index = tasks_listBox.curselection()
    if selected_task_index:
        current_task = tasks_listBox.get(selected_task_index)
        if not current_task.endswith("!!!!"):
            tasks_listBox.delete(selected_task_index)
            tasks_listBox.insert(selected_task_index, f"{current_task} !!!!")
            save_tasks_to_file()
            play_sound()  # Воспроизведение звука

def remove_important_mark():
    selected_task_index = tasks_listBox.curselection()
    if selected_task_index:
        current_task = tasks_listBox.get(selected_task_index)
        if current_task.endswith("!!!!"):
            current_task = current_task[:-4]
            tasks_listBox.delete(selected_task_index)
            tasks_listBox.insert(selected_task_index, current_task)
            save_tasks_to_file()
            play_sound()  # Воспроизведение звука

root = tk.Tk()
root.title("ПЛАН")
root.configure(background="khaki3")

# Загрузка изображения
img_path = r"C:\\Users\\АСУС\\Desktop\\top-view-january-calendar-plant_23-2149204277.jpg"
#img_path = "/content/top-view-january-calendar-plant_23-2149204277.jpg"

image = Image.open(img_path)
image = image.resize((200, 200), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Отображение изображения
img_label = tk.Label(root, image=photo, bg="khaki3")
img_label.pack(pady=10)

text1 = tk.Label(root, text="ЗАПЛАНИРУЙ ДЕЛА:", bg="khaki3", width=40)
text1.pack(pady=20)

task_entry = tk.Entry(root, width=40, bg="goldenrod4", fg="black")
task_entry.pack(pady=20)

add_tasks_button = tk.Button(root, text="Добавь новое дело", command=add_task)
add_tasks_button.pack(pady=10)

delete_button = tk.Button(root, text="Удали, если уже не актуально", command=delete_task)
delete_button.pack(pady=10)

mark_button = tk.Button(root, text="Отметь, если сделано", command=mark_task_done)
mark_button.pack(pady=10)

important_button = tk.Button(root, text="Пометь как срочное !", command=mark_task_important)
important_button.pack(pady=10)

# Кнопка для удаления пометки срочности
delete_important_button = tk.Button(root, text="Удали пометку срочности", command=remove_important_mark)
delete_important_button.pack(pady=10)

text2 = tk.Label(root, text="МОИ ДЕЛА:", bg="khaki3")
text2.pack(pady=10)

tasks_listBox = tk.Listbox(root, height=15, width=50, bg="linen")
tasks_listBox.pack(pady=10)

# Загрузка задач из файла при запуске программы
load_tasks_from_file()

root.mainloop()
