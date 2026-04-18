import customtkinter as ctk
import qrcode
from PIL import Image


def press_button():
    text = entry.get()
    if not text:
        label.configure(text="Введите текст!", image="")
        return

    qr = qrcode.QRCode(
        version=2,
        box_size=10,  # 21 × 10 = 210 пикселей
        border=0  # без рамки = точно 210×210
    )

    qr.add_data(text)
    qr.make(fit=False)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qr.png")

    # Загружаем для отображения
    pil_image = Image.open("qr.png")

    image_ctk_utility = ctk.CTkImage(
        dark_image=pil_image,
        size=(210, 210)  # <- КЛЮЧЕВОЕ ИСПРАВЛЕНИЕ
    )

    label.configure(image=image_ctk_utility, text="")

    # Для отладки - выводим реальный размер в консоль
    print(f"Реальный размер QR: {img.size}")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Приложение")
root.geometry("500x500")
my_font = ctk.CTkFont(size=20)

entry = ctk.CTkEntry(
    master=root,
    placeholder_text="Введите текст",
    justify="center",
    font=my_font,
    height=40,
    width=350
)

button = ctk.CTkButton(
    master=root,
    text="Сгенерировать QR-код",
    font=my_font,
    width=350,
    text_color="white",
    fg_color="#1FC26D",
    hover_color="#147D46",
    command=press_button
)

label = ctk.CTkLabel(master=root, text="", font=my_font)

entry.pack(pady=(50, 10))
button.pack(pady=10)
label.pack(pady=20)

root.mainloop()
