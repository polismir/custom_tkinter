import customtkinter as ctk  # подключаем модуль customtkinter (необходимо установить: pip install customtkinter)

# здесь объявляются функции-хендлеры и обычные функции

# задаём цветовое оформление всего приложения
ctk.set_appearance_mode("dark")  # также можно "light"
ctk.set_default_color_theme("green")  # также можно: "blue", "dark-blue"

root = ctk.CTk()  # создаём окно и привязываем его к переменной root
root.title("Задание №1")  # устанавливаем заголовок окна
root.geometry("500x500")  # устанавливаем размеры окна
my_font = ctk.CTkFont(size=20)  # задаём шрифт, потом будем применять его к виджетам

# здесь создаются виджеты: настраивается их внешний вид и привязка к хендлера



label = ctk.CTkLabel(master=root)
label.configure(
    text="Привет, Аноним!",
    font=my_font,
    text_color="white"
)

entry = ctk.CTkEntry(master=root)
entry.configure(
    placeholder_text="Введи свое имя",  # данный текст должен подсказывать, что нужно ввести в поле
    justify="center",  # расположение текста и подсказки будет по центру поля
    font=my_font,
    width=250  # ширина виджета в пикселях
)

button = ctk.CTkButton(master=root)  # создание кнопки и её привязка к окну root
button.configure(  # настройка её внешнего вида
    text="Готово",  # текст на кнопке
    font=my_font,  # шрифт текста (привязываем наш ранее созданный шрифт my_font)
    text_color="white",  # цвет текста
    fg_color="#00D66C",  # цвет тела кнопки
    hover_color="#00BA5F",  # цвет тела кнопки при наведении курсора (лучше брать более тёмный оттенок)
)
# здесь объявляются глобальные переменные: флаги, коллекции для хранения множества данных/виджетов

# здесь располагаются виджеты в окне приложения так, как они должны отображаться на старте
label.pack(pady=50)
entry.pack(pady=50)
button.pack(pady=50)

root.mainloop()  # запускаем главный цикл программы
