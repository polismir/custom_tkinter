import customtkinter as ctk  # подключаем модуль customtkinter (необходимо установить: pip install customtkinter)

# здесь объявляются функции-хендлеры и обычные функции
def switch_choice():
    value = var_switch.get()
    if value:
        ctk.set_appearance_mode("light")
        switch.configure(text="Светлая тема", font=my_font)
    if not value:
        ctk.set_appearance_mode("dark")
        switch.configure(text="Тёмная тема", font=my_font)

def slider_choice():
    value = var_slider.get()
    if value == 1:
        

# задаём цветовое оформление всего приложения
ctk.set_appearance_mode("dark")  # также можно "light"
ctk.set_default_color_theme("green")  # также можно: "blue", "dark-blue"

root = ctk.CTk()  # создаём окно и привязываем его к переменной root
root.title("Приложение")  # устанавливаем заголовок окна
root.geometry("500x500")  # устанавливаем размеры окна
my_font = ctk.CTkFont(size=20)  # задаём шрифт, потом будем применять его к виджетам

# здесь создаются виджеты: настраивается их внешний вид и привязка к хендлера
var_switch = ctk.BooleanVar()
switch = ctk.CTkSwitch(master=root, variable=var_switch, onvalue=True, offvalue=False)
switch.configure(text="Тёмная тема", font=my_font)
var_switch.set(False)
switch.configure(command=switch_choice)

var_slider = ctk.IntVar()
slider = ctk.CTkSlider(
    master=root,
    from_=1, to=3,
    orientation="horizontal",
    number_of_steps=2,  # количество отделений
    height=20,
    button_color="red",
    button_hover_color="red"
)
slider.set(0)
label = ctk.CTkLabel(master=root, text="красный ползунок", font=my_font)
slider.configure(command=slider_choice)


# здесь располагаются виджеты в окне приложения так, как они должны отображаться на старте
switch.pack(pady=50)
slider.pack(pady=(200, 10))
label.pack(pady=(10, 10))


root.mainloop()  # запускаем главный цикл программы
