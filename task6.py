import customtkinter as ctk

def handle_button_press(btn_ind, number):
    global flag_active_btn1, flag_active_btn2, flag_active_btn3
    if number == 1:
        if flag_active_btn1 is not None:
            lst_btns1[flag_active_btn1].configure(fg_color="green")
        lst_btns1[btn_ind].configure(fg_color="orange")
        flag_active_btn1 = btn_ind
    if number == 2:
        global flag_active_btn2
        if flag_active_btn2 is not None:
            lst_btns2[flag_active_btn2].configure(fg_color="green")
        lst_btns2[btn_ind].configure(fg_color="orange")
        flag_active_btn2 = btn_ind
    if number == 3:
        global flag_active_btn3
        if flag_active_btn3 is not None:
            lst_btns3[flag_active_btn3].configure(fg_color="green")
        lst_btns3[btn_ind].configure(fg_color="orange")
        flag_active_btn3 = btn_ind

    if flag_active_btn1 is not None:
        if flag_active_btn1 == 9:
            number1 = "0"
        else:
            number1 = f"{flag_active_btn1 + 1}"
    else:
        number1 = ""

    if flag_active_btn2 is not None:
        if flag_active_btn2 == 9:
            number2 = "0"
        else:
            number2 = f"{flag_active_btn2 + 1}"
    else:
        number2 = ""

    if flag_active_btn3 is not None:
        if flag_active_btn3 == 9:
            number3 = "0"
        else:
            number3 = f"{flag_active_btn3 + 1}"
    else:
        number3 = ""

    entry.configure(state="normal")
    entry.delete(0, "end")
    entry.insert(0, number1 + number2 + number3)


# задаём цветовое оформление всего приложения
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Приложение")
root.geometry("600x600")
my_font = ctk.CTkFont(size=25)

# виджеты для внешнего окна root
scrollable_frame1 = ctk.CTkScrollableFrame(master=root)
scrollable_frame1.configure(height=350, width=100)

scrollable_frame2 = ctk.CTkScrollableFrame(master=root)
scrollable_frame2.configure(height=350, width=100)

scrollable_frame3 = ctk.CTkScrollableFrame(master=root)
scrollable_frame3.configure(height=350, width=100)

label = ctk.CTkLabel(master=root)
label.configure(
    text="Выберите код:",
    font=my_font,
    text_color="white"
)

entry = ctk.CTkEntry(master=root)
entry.configure(
    placeholder_text="",  # данный текст должен подсказывать, что нужно ввести в поле
    justify="center",  # расположение текста и подсказки будет по центру поля
    font=my_font,
    height=50,
    width=100 # ширина виджета в пикселях
)
entry.configure(state="readonly")

# виджеты для внутренней рамки scrollable_frame1
lst_handlers1 = []
for i in range(10):
    handler_i = lambda i_actual=i: handle_button_press(i_actual, 1)
    lst_handlers1.append(handler_i)

flag_active_btn1 = None
lst_btns1 = []
for i in range(10):
    btn_i = ctk.CTkButton(master=scrollable_frame1)
    if i == 9:
        btn_i.configure(text="0", font=my_font, fg_color="green", width=150, height=50)
    else:
        btn_i.configure(text=f"{i + 1}", font=my_font, fg_color="green", width=150, height=50)
    btn_i.configure(command=lst_handlers1[i])  # к каждой кнопке привязываем свой промежуточный хендлер
    lst_btns1.append(btn_i)

# виджеты для внутренней рамки scrollable_frame2
lst_handlers2 = []
for i in range(10):
    handler_i = lambda i_actual=i: handle_button_press(i_actual, 2)
    lst_handlers2.append(handler_i)

flag_active_btn2 = None
lst_btns2 = []
for i in range(10):
    btn_i = ctk.CTkButton(master=scrollable_frame2)
    if i == 9:
        btn_i.configure(text="0", font=my_font, fg_color="green", width=150, height=50)
    else:
        btn_i.configure(text=f"{i + 1}", font=my_font, fg_color="green", width=150, height=50)
    btn_i.configure(command=lst_handlers2[i])  # к каждой кнопке привязываем свой промежуточный хендлер
    lst_btns2.append(btn_i)

# виджеты для внутренней рамки scrollable_frame3
lst_handlers3 = []
for i in range(10):
    handler_i = lambda i_actual=i: handle_button_press(i_actual, 3)
    lst_handlers3.append(handler_i)

flag_active_btn3 = None
lst_btns3 = []
for i in range(10):
    btn_i = ctk.CTkButton(master=scrollable_frame3)
    if i == 9:
        btn_i.configure(text="0", font=my_font, fg_color="green", width=150, height=50)
    else:
        btn_i.configure(text=f"{i + 1}", font=my_font, fg_color="green", width=150, height=50)
    btn_i.configure(command=lst_handlers3[i])  # к каждой кнопке привязываем свой промежуточный хендлер
    lst_btns3.append(btn_i)

# здесь располагаются виджеты в окне приложения так, как они должны отображаться на старте
rows, columns = 3, 3
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=3)
root.rowconfigure(index=2, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

label.grid(row=0, column=0, columnspan=3, padx=20, pady=30)
scrollable_frame1.grid(row=1, column=0)
scrollable_frame2.grid(row=1, column=1)
scrollable_frame3.grid(row=1, column=2)
entry.grid(row=2, column=0, columnspan=3, padx=20, pady=30)

# сетка для scrollable_frame1
rows, columns = 10, 1
for i in range(rows):
    scrollable_frame1.rowconfigure(index=i, weight=1)
for i in range(columns):
    scrollable_frame1.columnconfigure(index=i, weight=1)
for i in range(10):
    btn_i = lst_btns1[i]
    btn_i.grid(row=i, column=0, padx=20, pady=20)

# сетка для scrollable_frame2
rows, columns = 10, 1
for i in range(rows):
    scrollable_frame2.rowconfigure(index=i, weight=1)
for i in range(columns):
    scrollable_frame2.columnconfigure(index=i, weight=1)
for i in range(10):
    btn_i = lst_btns2[i]
    btn_i.grid(row=i, column=0, padx=20, pady=20)

# сетка для scrollable_frame3
rows, columns = 10, 1
for i in range(rows):
    scrollable_frame3.rowconfigure(index=i, weight=1)
for i in range(columns):
    scrollable_frame3.columnconfigure(index=i, weight=1)
for i in range(10):
    btn_i = lst_btns3[i]
    btn_i.grid(row=i, column=0, padx=20, pady=20)

root.mainloop()  # запускаем главный цикл программы
