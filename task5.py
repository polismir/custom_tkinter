import customtkinter as ctk  # подключаем модуль customtkinter (необходимо установить: pip install customtkinter)

# здесь объявляются функции-хендлеры и обычные функции


# задаём цветовое оформление всего приложения
ctk.set_appearance_mode("dark")  # также можно "light"
ctk.set_default_color_theme("green")  # также можно: "blue", "dark-blue"

root = ctk.CTk()  # создаём окно и привязываем его к переменной root
root.title("Добавление траты")  # устанавливаем заголовок окна
root.geometry("700x400")  # устанавливаем размеры окна
my_font = ctk.CTkFont(size=35)  # задаём шрифт, потом будем применять его к виджетам

# здесь создаются виджеты: настраивается их внешний вид и привязка к хендлера
label1 = ctk.CTkLabel(master=root)
label1.configure(
    text="Добавьте товар",
    font=my_font,
    text_color="white"
)

label2 = ctk.CTkLabel(master=root)
label2.configure(
    text="Суть:",
    font=my_font,
    text_color="white"
)

label3 = ctk.CTkLabel(master=root)
label3.configure(
    text="Категория товара",
    font=my_font,
    text_color="white"
)

entry1 = ctk.CTkEntry(master=root)
entry1.configure(
    placeholder_text="Название",  # данный текст должен подсказывать, что нужно ввести в поле
    justify="center",  # расположение текста и подсказки будет по центру поля
    font=my_font,
    width=200  # ширина виджета в пикселях
)

entry2 = ctk.CTkEntry(master=root)
entry2.configure(
    placeholder_text="Цена",  # данный текст должен подсказывать, что нужно ввести в поле
    justify="center",  # расположение текста и подсказки будет по центру поля
    font=my_font,
    width=200  # ширина виджета в пикселях
)

elems = ["Еда", "Транспорт", "Одежда", "Быт.товары", "Лекарства", "Крупные траты"]  # список элементов
combobox = ctk.CTkComboBox(master=root)
combobox.configure(
    font=my_font,
    values=elems,
    width=270
)
combobox.configure(state="readonly")
combobox.set("Еда")  # значение элемента по умолчанию

button1 = ctk.CTkButton(master=root)  # создание кнопки и её привязка к окну root
button1.configure(  # настройка её внешнего вида
    text="Вернуться",  # текст на кнопке
    font=my_font,  # шрифт текста (привязываем наш ранее созданный шрифт my_font)
    text_color="white",  # цвет текста
    fg_color="#00D66C",  # цвет тела кнопки
    hover_color="#00BA5F",  # цвет тела кнопки при наведении курсора (лучше брать более тёмный оттенок)
)

button2 = ctk.CTkButton(master=root)  # создание кнопки и её привязка к окну root
button2.configure(  # настройка её внешнего вида
    text="Добавить",  # текст на кнопке
    font=my_font,  # шрифт текста (привязываем наш ранее созданный шрифт my_font)
    text_color="white",  # цвет текста
    fg_color="#00D66C",  # цвет тела кнопки
    hover_color="#00BA5F",  # цвет тела кнопки при наведении курсора (лучше брать более тёмный оттенок)
)

# здесь располагаются виджеты в окне приложения так, как они должны отображаться на старте
rows, columns = 5, 3
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=0, weight=2)
    root.columnconfigure(index=1, weight=1)
    root.columnconfigure(index=2, weight=1)

label1.grid(row=0, column=0, columnspan=3)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)
entry1.grid(row=1, column=1)
entry2.grid(row=1, column=2)
combobox.grid(row=2, column=1, columnspan=3)
button1.grid(row=3, column=0)
button2.grid(row=4, column=0)


root.mainloop()  # запускаем главный цикл программы
