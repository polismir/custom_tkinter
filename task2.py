import customtkinter as ctk  # подключаем модуль customtkinter (необходимо установить: pip install customtkinter)

# здесь объявляются функции-хендлеры и обычные функции
def press_button():
    text = int(entry1.get()) + int(entry2.get())
    entry3.configure(state="normal")
    entry3.delete(0, "end")
    entry3.insert(0, str(text))
    entry3.configure(state="readonly")

# задаём цветовое оформление всего приложения
ctk.set_appearance_mode("dark")  # также можно "light"
ctk.set_default_color_theme("green")  # также можно: "blue", "dark-blue"

root = ctk.CTk()  # создаём окно и привязываем его к переменной root
root.title("Задание №2")  # устанавливаем заголовок окна
root.geometry("500x500")  # устанавливаем размеры окна
my_font = ctk.CTkFont(size=20)  # задаём шрифт, потом будем применять его к виджетам

# здесь создаются виджеты: настраивается их внешний вид и привязка к хендлера
entry1 = ctk.CTkEntry(master=root)
entry1.configure(
    placeholder_text="",  # данный текст должен подсказывать, что нужно ввести в поле
    justify="center",  # расположение текста и подсказки будет по центру поля
    font=my_font,
    width=250  # ширина виджета в пикселях
)

label1 = ctk.CTkLabel(master=root)
label1.configure(
    text="+",
    font=my_font,
    text_color="white"
)

entry2 = ctk.CTkEntry(master=root)
entry2.configure(
    placeholder_text="",  # данный текст должен подсказывать, что нужно ввести в поле
    justify="center",  # расположение текста и подсказки будет по центру поля
    font=my_font,
    width=250  # ширина виджета в пикселях
)

label2 = ctk.CTkLabel(master=root)
label2.configure(
    text="=",
    font=my_font,
    text_color="white"
)

entry3 = ctk.CTkEntry(master=root)
entry3.configure(
    placeholder_text="",  # данный текст должен подсказывать, что нужно ввести в поле
    justify="center",  # расположение текста и подсказки будет по центру поля
    font=my_font,
    width=250  # ширина виджета в пикселях
)
entry3.configure(state="readonly")

button = ctk.CTkButton(master=root)  # создание кнопки и её привязка к окну root
button.configure(  # настройка её внешнего вида
    text="Посчитать",  # текст на кнопке
    font=my_font,  # шрифт текста (привязываем наш ранее созданный шрифт my_font)
    text_color="white",  # цвет текста
    fg_color="#00D66C",  # цвет тела кнопки
    hover_color="#00BA5F",  # цвет тела кнопки при наведении курсора (лучше брать более тёмный оттенок)
)
button.configure(command=press_button)

# здесь объявляются глобальные переменные: флаги, коллекции для хранения множества данных/виджетов

# здесь располагаются виджеты в окне приложения так, как они должны отображаться на старте
entry1.pack(pady=20)
label1.pack(pady=20)
entry2.pack(pady=20)
label2.pack(pady=20)
entry3.pack(pady=20)
button.pack(pady=30)

root.mainloop()  # запускаем главный цикл программы
