import tkinter as tk
from datetime import datetime

def add_task():
    task = task_entry.get()  # Получаем слова из поля для ввода
    if task:
        task_listBox.insert(tk.END, task)  # Вставляем полученное слово в конец списка
        task_entry.delete(0, tk.END)  # Очищаем поле для ввода, от нулевого индекса и до конца

def delete_task():
    selected_task = task_listBox.curselection()  # Получаем ID, индекс выбранного элемента
    if selected_task:
        task_listBox.delete(selected_task)  # Удаляем выбранный элемент из списка

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="slate blue")  # Изменяем цвет заливки выполненной задачи

# Создаём окно, в котором мы будем работать
root = tk.Tk()
# Получаем текущую дату
current_date = datetime.now().strftime("%d-%m-%Y")

# Указываем заголовок окна с текущей датой
root.title(f"Дела на сегодня - {current_date}")

# Меняем цвет заднего фона
root.configure(background="aquamarine4")

# Создаём и позиционируем надпись, чтобы у поля для ввода задачи был заголовок
text1 = tk.Label(root, text="Введите вашу задачу:", bg="aquamarine4")
text1.pack(pady=5)

# Чтобы дать возможность вводить задачи, создаём переменную
task_entry = tk.Entry(root, width=30, bg="grey82", cursor="hand2")
task_entry.pack(pady=2)
task_entry.focus_set()  # Устанавливаем фокус на поле ввода

# Создаём и позиционируем кнопку, которая будет добавлять задачу в список
add_task_button = tk.Button(root, text="Добавить задачу", command=add_task)
add_task_button.pack(pady=5)

# Создаём и позиционируем кнопку, которая будет удалять задачу из списка
delete_button = tk.Button(root, text="Удалить задачу", command=delete_task)
delete_button.pack(pady=5)

# Создаём и позиционируем кнопку, которая будет отмечать задачу выполненной
mark_button = tk.Button(root, text="Отметить выполненную задачу", command=mark_task)
mark_button.pack(pady=5)

# Добавляем и позиционируем надпись, чтобы у списка задач был заголовок
text2 = tk.Label(root, text="Список задач:", bg="aquamarine4")
text2.pack(pady=5)

# Используем новую команду, чтобы создать список, в который будут добавляться задачи
task_listBox = tk.Listbox(root, height=10, width=80, bg="light salmon")
task_listBox.pack(pady=10)

root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

# Чтобы окно не закрывалось, прописываем
root.mainloop()
