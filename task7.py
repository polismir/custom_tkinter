import customtkinter as ctk
from PIL import Image

# здесь объявляются функции-хендлеры и обычные функции
def handler(i, j):
    global flag_player, matrix_lbls, matrix, flag_game
    if matrix[i][j] == -1 and flag_game == True:
        if flag_player == 1:
            matrix_lbls[i][j].configure(image=image_ctk_utility1)
            matrix[i][j] = 1
            flag_player = 0
        elif flag_player == 0:
            matrix_lbls[i][j].configure(image=image_ctk_utility2)
            matrix[i][j] = 0
            flag_player = 1
        # проверка победы
        if matrix[0][0] == matrix[0][1] == matrix[0][2] != -1:
            print("Выиграли " + ("крестики" if matrix[0][0] == 1 else "нолики"))
            flag_game = False
        if matrix[1][0] == matrix[1][1] == matrix[1][2] != -1:
            print("Выиграли " + ("крестики" if matrix[1][0] == 1 else "нолики"))
            flag_game = False
        if matrix[2][0] == matrix[2][1] == matrix[2][2] != -1:
            print("Выиграли " + ("крестики" if matrix[2][0] == 1 else "нолики"))
            flag_game = False
        if matrix[0][0] == matrix[1][0] == matrix[2][0] != -1:
            print("Выиграли " + ("крестики" if matrix[0][0] == 1 else "нолики"))
            flag_game = False
        if matrix[0][1] == matrix[1][1] == matrix[2][1] != -1:
            print("Выиграли " + ("крестики" if matrix[0][1] == 1 else "нолики"))
            flag_game = False
        if matrix[0][2] == matrix[1][2] == matrix[2][2] != -1:
            print("Выиграли " + ("крестики" if matrix[0][2] == 1 else "нолики"))
            flag_game = False
        if matrix[0][0] == matrix[1][1] == matrix[2][2] != -1:
            print("Выиграли " + ("крестики" if matrix[0][0] == 1 else "нолики"))
            flag_game = False
        if matrix[0][2] == matrix[1][1] == matrix[2][0] != -1:
            print("Выиграли " + ("крестики" if matrix[0][2] == 1 else "нолики"))
            flag_game = False


# задаём цветовое оформление всего приложения
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Приложение")
root.geometry("500x500")
my_font = ctk.CTkFont(size=20)

# здесь создаются виджеты: настраивается их внешний вид и привязка к хендлера
image_object1 = Image.open("images/cross.png")
image_ctk_utility1 = ctk.CTkImage(dark_image=image_object1, size=(100, 100))
image_object2 = Image.open("images/zero.png")
image_ctk_utility2 = ctk.CTkImage(dark_image=image_object2, size=(100, 100))
image_object3 = Image.open("images/white_background.png")
image_ctk_utility3 = ctk.CTkImage(dark_image=image_object3, size=(100, 100))

label = ctk.CTkLabel(master=root)
label.configure(
    text="",
    font=my_font,
    text_color="white"
)

# рамка frame
frame = ctk.CTkFrame(master=root)

# создание хендлеров для labels:
matrix_handlers = []
for i in range(3):
    tmp_lst = []
    for j in range(3):
        handler_ij = lambda x, i_actual=i, j_actual=j: handler(i_actual, j_actual)
        # параметр x был нужен, так как при привязке хендлера к Label
        # обязательно должен быть один принимающий значение параметр, хоть он нам и не понадобится
        tmp_lst.append(handler_ij)
    matrix_handlers.append(tmp_lst)

# создание виджетов labels и привязка к ним изображений и хендлеров:
matrix_lbls = []
for i in range(3):
    tmp_lst = []
    for j in range(3):
        lbl_ij = ctk.CTkLabel(master=frame, text="", image=image_ctk_utility3)
        lbl_ij.bind("<Button-1>", matrix_handlers[i][j])
        lbl_ij.configure(cursor="hand2")
        tmp_lst.append(lbl_ij)
    matrix_lbls.append(tmp_lst)

# внешняя сетка для окна root:
rows, columns = 3, 3
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)
frame.grid(row=1, column=1)

# внутренняя сетка для рамки frame:
rows, columns = 3, 3
for i in range(rows):
    frame.rowconfigure(index=i, weight=1)
for i in range(columns):
    frame.columnconfigure(index=i, weight=1)
for i in range(3):
    for j in range(3):
        lbl_ij = matrix_lbls[i][j]
        lbl_ij.grid(row=i, column=j, padx=5, pady=5)

flag_player = 1 # 1 - крестик, 0 - нолик
flag_game = True
# здесь располагаются виджеты в окне приложения так, как они должны отображаться на старте
matrix = [
    [-1, -1, -1],
    [-1, -1, -1],
    [-1, -1, -1]
] # -1 - пустая клетка

root.mainloop()
