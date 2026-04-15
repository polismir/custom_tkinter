import customtkinter as ctk

# здесь объявляются функции-хендлеры и обычные функции

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Приложение")
root.geometry("500x500")
my_font = ctk.CTkFont(size=20)

# здесь создаются виджеты: настраивается их внешний вид и привязка к хендлера
entry = ctk.CTkEntry(master=root)
entry.configure(
    placeholder_text="Введите текст",
    justify="center",
    font=my_font,
    height=40,
    width=350
)

button = ctk.CTkButton(master=root)  # создание кнопки и её привязка к окну root
button.configure(  # настройка её внешнего вида
    text="Сгенерировать QR-код",
    font=my_font,
    width=350,
    text_color="white",
    fg_color="#1FC26D",
    hover_color="#147D46",
)

label = ctk.CTkLabel(master=root)
label.configure(
    text="",
    font=my_font,
    text_color="white"
)

# здесь располагаются виджеты в окне приложения так, как они должны отображаться на старте
entry.pack(pady=(50, 10))
button.pack(pady=10)

root.mainloop()
