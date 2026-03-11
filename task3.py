import customtkinter as ctk  # подключаем модуль customtkinter (необходимо установить: pip install customtkinter)

# здесь объявляются функции-хендлеры и обычные функции
def press_button():
    text = combobox.get()
    color = var_radiobuttons.get()
    mark1 = var_checkbox_1.get()
    mark2 = var_checkbox_2.get()
    if color == 1:
        color = "white"
    if color == 2:
        color = "red"
    if color == 3:
        color = "yellow"
    if mark2:
        text = text + "?"
    if mark1:
        text = text + "!"
    entry.configure(state="normal")
    entry.delete(0, "end")
    entry.insert(0, str(text))
    entry.configure(state="readonly", text_color=color)


# задаём цветовое оформление всего приложения
ctk.set_appearance_mode("dark")  # также можно "light"
ctk.set_default_color_theme("green")  # также можно: "blue", "dark-blue"

root = ctk.CTk()  # создаём окно и привязываем его к переменной root
root.title("Приложение")  # устанавливаем заголовок окна
root.geometry("500x500")  # устанавливаем размеры окна
my_font = ctk.CTkFont(size=20)  # задаём шрифт, потом будем применять его к виджетам

# здесь создаются виджеты: настраивается их внешний вид и привязка к хендлера
entry = ctk.CTkEntry(master=root)
entry.configure(
    placeholder_text="",  # данный текст должен подсказывать, что нужно ввести в поле
    justify="center",  # расположение текста и подсказки будет по центру поля
    font=my_font,
    width=250  # ширина виджета в пикселях
)
entry.configure(state="readonly")


var_radiobuttons = ctk.IntVar()

radiobutton_1 = ctk.CTkRadioButton(
    master=root,
    variable=var_radiobuttons,  # привязываем переключатель к переменной
    value=1  # значение данного переключателя
)
# параметры variable и value обязательно указываем при создании, а не в .configure()
radiobutton_1.configure(text="Белый цвет текста", font=my_font)

radiobutton_2 = ctk.CTkRadioButton(master=root, variable=var_radiobuttons, value=2)
radiobutton_2.configure(text="Красный цвет текста", font=my_font)

radiobutton_3 = ctk.CTkRadioButton(master=root, variable=var_radiobuttons, value=3)
radiobutton_3.configure(text="Желтый цвет текста", font=my_font)

var_radiobuttons.set(1)  # значение переменной по умолчанию, то есть по умолчанию будет активен 1-ый переключатель

# взаимодействие с RadioButton:
var_radiobuttons.get()  # получаем текущее значение переменной, если 1 => включён первый переключатель, иначе - второй


elems = ["Ты уходишь", "Ты здесь", "Ты пришел"]  # список элементов
combobox = ctk.CTkComboBox(master=root)
combobox.configure(
    font=my_font,
    values=elems,
    width=250
)
combobox.configure(state="readonly")
combobox.set("Выберите фразу:")  # значение элемента по умолчанию

# взаимодействие с ComboBox:
combobox.get()  # получить выбранное значение

var_checkbox_1 = ctk.BooleanVar()

checkbox_1 = ctk.CTkCheckBox(
    master=root,
    variable=var_checkbox_1,  # переменная, к которой привязываем флажок
    onvalue=True,  # значение переменной, когда флажок активен, мы решили, что это будет True
    offvalue=False  # значение переменной, когда флажок не активен, мы решили, что это будет False
)
checkbox_1.configure(text="Добавить в конец !", font=my_font)

var_checkbox_1.set(True)  # значение переменной по умолчанию, то есть по умолчанию первый флажок будет активен

var_checkbox_2 = ctk.BooleanVar()  # второй флажок будет привязан ко второй переменной
checkbox_2 = ctk.CTkCheckBox(master=root, variable=var_checkbox_2, onvalue=True, offvalue=False)
checkbox_2.configure(text="Добавить в конец ?", font=my_font)
var_checkbox_2.set(False)  # значение переменной по умолчанию, то есть по умолчанию второй флажок будет неактивен

# взаимодействие с CheckBox:
var_checkbox_1.get()  # True или False
var_checkbox_2.get()


button = ctk.CTkButton(master=root)  # создание кнопки и её привязка к окну root
button.configure(  # настройка её внешнего вида
    text="Выбрать",  # текст на кнопке
    font=my_font,  # шрифт текста (привязываем наш ранее созданный шрифт my_font)
    text_color="white",  # цвет текста
    fg_color="#00D66C",  # цвет тела кнопки
    hover_color="#00BA5F",  # цвет тела кнопки при наведении курсора (лучше брать более тёмный оттенок)
)
button.configure(command=press_button)


# здесь располагаются виджеты в окне приложения так, как они должны отображаться на старте
entry.pack(pady=20)
radiobutton_1.pack(pady=15)
radiobutton_2.pack(pady=15)
radiobutton_3.pack(pady=15)
combobox.pack(pady=20)
checkbox_1.pack(pady=15)
checkbox_2.pack(pady=15)
button.pack(pady=20)


root.mainloop()  # запускаем главный цикл программы
