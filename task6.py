import customtkinter as ctk

def handle_button_press(btn_ind):
    global flag_active_btn
    if flag_active_btn is not None:
        lst_btns[flag_active_btn].configure(fg_color="green")
    lst_btns[btn_ind].configure(fg_color="orange")
    flag_active_btn = btn_ind
    entry.configure(state="normal")
    if btn_ind == 9:
        entry.configure(text="0")
    else:
        entry.configure(text=f"{btn_ind + 1}")
    entry.configure(state="readonly")


# задаём цветовое оформление всего приложения
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Приложение")
root.geometry("600x600")
my_font = ctk.CTkFont(size=25)

# виджеты для внешнего окна root
scrollable_frame = ctk.CTkScrollableFrame(master=root)
scrollable_frame.configure(height=350, width=100)

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

# виджеты для внутренней рамки scrollable_frame

lst_handlers = []
for i in range(10):
    handler_i = lambda i_actual=i: handle_button_press(i_actual)
    lst_handlers.append(handler_i)

flag_active_btn = None
lst_btns = []
for i in range(10):
    btn_i = ctk.CTkButton(master=scrollable_frame)
    if i == 9:
        btn_i.configure(text="0", font=my_font, width=150, height=50)
    else:
        btn_i.configure(text=f"{i + 1}", font=my_font, width=150, height=50)
    btn_i.configure(command=lst_handlers[i])  # к каждой кнопке привязываем свой промежуточный хендлер
    lst_btns.append(btn_i)

# здесь располагаются виджеты в окне приложения так, как они должны отображаться на старте
rows, columns = 3, 3
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=3)
root.rowconfigure(index=2, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)

label.grid(row=0, column=0, columnspan=3, padx=20, pady=30)
scrollable_frame.grid(row=1, column=0, columnspan=3)
entry.grid(row=2, column=0, columnspan=3, padx=20, pady=30)

rows, columns = 10, 1
for i in range(rows):
    scrollable_frame.rowconfigure(index=i, weight=1)
for i in range(columns):
    scrollable_frame.columnconfigure(index=i, weight=1)
for i in range(10):
    btn_i = lst_btns[i]
    btn_i.grid(row=i, column=0, padx=20, pady=20)

root.mainloop()  # запускаем главный цикл программы
