import tkinter as tk
from tkinter import font

# Функция для вывода приветственного сообщения
def say_hello():
    name = entry.get()  # Получаем введенное имя из поля ввода
    if name:
        label_result.config(text=f"Привет, {name}!")  # Обновляем текст метки
    else:
        label_result.config(text="Пожалуйста, введите имя!")  # Если имя не введено

# Создание главного окна
root = tk.Tk()
root.title("Приветствие")

# Размер окна
root.geometry("400x300")
root.configure(bg="#f0f0f0")  # Светло-серый фон

# Настройка шрифтов
header_font = font.Font(size=20, weight='bold')
button_font = font.Font(size=12)

# Метка для заголовка
label_header = tk.Label(root, text="ВВЕДИТЕ ВАШЕ ИМЯ", font=header_font, bg="#f0f0f0", fg="#333")
label_header.pack(pady=20)

# Рамка для поля ввода (чтобы поле ввода было более заметным)
frame_entry = tk.Frame(root, bd=2, relief=tk.SUNKEN)
frame_entry.pack(pady=10)

# Поле ввода для имени
entry = tk.Entry(frame_entry, font=("Arial", 14), justify='center', width=30, bd=2, relief=tk.FLAT)
entry.pack()

# Кнопка для приветствия
button = tk.Button(root, text="ПОЗДОРОВАТЬСЯ", font=button_font, bg='#4CAF50', fg='white', width=15, height=2, command=say_hello)
button.pack(pady=20)

# Рамка для вывода результата
frame_result = tk.Frame(root, bd=2, relief=tk.SUNKEN)
frame_result.pack(pady=10)

# Метка для вывода результата
label_result = tk.Label(frame_result, text="", font=("Arial", 16), width=30, bg="white", height=2, anchor='center')
label_result.pack()

# Запуск основного цикла программы
root.mainloop()
