
import tkinter as tk
from PIL import Image, ImageTk

def add_task():
    task = task_entry.get()
    if task:
        tasks_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task_index = tasks_listBox.curselection()
    if selected_task_index:
        tasks_listBox.delete(selected_task_index)

def mark_task_done():
    selected_task_index = tasks_listBox.curselection()
    if selected_task_index:
        current_task = tasks_listBox.get(selected_task_index)
        tasks_listBox.delete(selected_task_index)
        tasks_listBox.insert(tk.END, f"{current_task} (done)")

def mark_task_important():
    selected_task_index = tasks_listBox.curselection()
    if selected_task_index:
        current_task = tasks_listBox.get(selected_task_index)
        if not current_task.endswith("!!!!"):  # Проверяем, не добавлена ли уже пометка срочности
            tasks_listBox.delete(selected_task_index)
            tasks_listBox.insert(selected_task_index, f"{current_task} !!!!")

def remove_important_mark():
    selected_task_index = tasks_listBox.curselection()
    if selected_task_index:
        current_task = tasks_listBox.get(selected_task_index)
        if current_task.endswith("!!!!"):  # Проверяем, есть ли пометка срочности
            current_task = current_task[:-4]  # Убираем последние 4 знака "!!!!"
            tasks_listBox.delete(selected_task_index)
            tasks_listBox.insert(selected_task_index, current_task)

root = tk.Tk()
root.title("ПЛАН")
root.configure(background="khaki3")

# Загрузка изображения
img_path = r"C:\Users\АСУС\Desktop\top-view-january-calendar-plant_23-2149204277.jpg"
#img_path = 'https://cloud.mail.ru/public/ff38/wgXvZpBZ5'
image = Image.open(img_path)
image = image.resize((200, 200), Image.Resampling.LANCZOS)  # Изменение размера изображения
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

mark_button= tk.Button(root, text="Пометь, если сделано", command=mark_task_done)
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

root.mainloop()

