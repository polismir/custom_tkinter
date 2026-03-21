import customtkinter as ctk  # подключаем модуль customtkinter (необходимо установить: pip install customtkinter)

# здесь объявляются функции-хендлеры и обычные функции


# задаём цветовое оформление всего приложения
ctk.set_appearance_mode("dark")  # также можно "light"
ctk.set_default_color_theme("green")  # также можно: "blue", "dark-blue"

root = ctk.CTk()  # создаём окно и привязываем его к переменной root
root.title("Добавление траты")  # устанавливаем заголовок окна
root.geometry("800x500")  # устанавливаем размеры окна
my_font = ctk.CTkFont(size=20)  # задаём шрифт, потом будем применять его к виджетам

# здесь создаются виджеты: настраивается их внешний вид и привязка к хендлера
elems = [""]  # список элементов
combobox1 = ctk.CTkComboBox(master=root)
combobox1.configure(
    font=my_font,
    values=elems,
    width=300,
)
combobox1.configure(state="readonly")
combobox1.set("Выберите тип шифрования")  # значение элемента по умолчанию

elems = [""]  # список элементов
combobox2 = ctk.CTkComboBox(master=root)
combobox2.configure(
    font=my_font,
    values=elems,
    width=250
)
combobox2.configure(state="readonly")
combobox2.set("Шифрование")  # значение элемента по умолчанию

elems = ["Русский язый", "Английский язык", "Французский язык", "Китайский язык"]  # список элементов
combobox3 = ctk.CTkComboBox(master=root)
combobox3.configure(
    font=my_font,
    values=elems,
    width=250
)
combobox3.configure(state="readonly")
combobox3.set("Русский язык")  # значение элемента по умолчанию

textbox1 = ctk.CTkTextbox(master=root)
textbox1.configure(font=my_font, width=400)

textbox2 = ctk.CTkTextbox(master=root)
textbox2.configure(font=my_font, height=250)

button = ctk.CTkButton(master=root)  # создание кнопки и её привязка к окну root
button.configure(  # настройка её внешнего вида
    text="Готово",  # текст на кнопке
    font=my_font,
    width=400,
    text_color="white",  # цвет текста
    fg_color="#00D66C",  # цвет тела кнопки
    hover_color="#00BA5F",  # цвет тела кнопки при наведении курсора (лучше брать более тёмный оттенок)
)

# здесь располагаются виджеты в окне приложения так, как они должны отображаться на старте
rows, columns = 5, 2
for i in range(rows):
    root.rowconfigure(index=0, weight=3)
    root.rowconfigure(index=1, weight=1)
    root.rowconfigure(index=2, weight=1)
    root.rowconfigure(index=3, weight=1)
    root.rowconfigure(index=4, weight=3)
for i in range(columns):
    root.columnconfigure(index=0, weight=1)
    root.columnconfigure(index=1, weight=3)

combobox1.grid(row=0, column=0)
combobox2.grid(row=1, column=0)
combobox3.grid(row=2, column=0)
textbox1.grid(row=0, column=1, rowspan=3)
button.grid(row=2, column=1, rowspan=3)

root.mainloop()  # запускаем главный цикл программы
