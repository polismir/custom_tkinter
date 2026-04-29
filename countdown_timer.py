import customtkinter as ctk
import tkinter.messagebox as msgbox
import winsound

# ------------------ Функции управления таймером ------------------
remaining_seconds = 0
timer_running = False
after_id = None

def update_timer_display():
    hours = remaining_seconds // 3600
    minutes = (remaining_seconds % 3600) // 60
    seconds = remaining_seconds % 60
    time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    label_time.configure(text=time_str)

def tick():
    global remaining_seconds, timer_running, after_id
    if timer_running and remaining_seconds > 0:
        remaining_seconds -= 1
        update_timer_display()
        after_id = root.after(1000, tick)
    elif remaining_seconds == 0 and timer_running:
        timer_running = False
        update_timer_display()
        winsound.Beep(1000, 1000)
        after_id = None

def start_timer():
    global remaining_seconds, timer_running, after_id

    if timer_running:
        return  # уже идёт отсчёт

    # Если таймер на паузе (осталось время) – просто продолжаем
    if remaining_seconds > 0:
        timer_running = True
        # Отменяем старый after на случай, если он остался (на всякий случай)
        if after_id is not None:
            root.after_cancel(after_id)
            after_id = None
        tick()  # запускаем отсчёт с текущего remaining_seconds
        return

    # Иначе (remaining_seconds == 0) – запускаем новый таймер из полей
    try:
        hours = int(entry1.get()) if entry1.get() else 0
        minutes = int(entry2.get()) if entry2.get() else 0
        seconds = int(entry3.get()) if entry3.get() else 0
    except ValueError:
        msgbox.showerror("Ошибка", "Введите целые числа в поля часов, минут и секунд")
        return

    total = hours * 3600 + minutes * 60 + seconds
    if total <= 0:
        msgbox.showwarning("Предупреждение", "Задайте время больше нуля")
        return

    if after_id is not None:
        root.after_cancel(after_id)
        after_id = None

    remaining_seconds = total
    timer_running = True
    update_timer_display()
    tick()

def pause_timer():
    global timer_running, after_id
    if not timer_running:
        return
    timer_running = False
    if after_id is not None:   # была опечатка, исправляем
        root.after_cancel(after_id)
        after_id = None

def reset_timer():
    global remaining_seconds, timer_running, after_id
    timer_running = False
    if after_id is not None:
        root.after_cancel(after_id)
        after_id = None
    entry1.delete(0, ctk.END)
    entry2.delete(0, ctk.END)
    entry3.delete(0, ctk.END)
    remaining_seconds = 0
    update_timer_display()

# ------------------ Настройки окна ------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("Обратный отсчёт")
root.geometry("500x600")

my_font = ctk.CTkFont(size=20)

# ------------------ Виджеты ------------------
entry1 = ctk.CTkEntry(master=root)
entry1.configure(placeholder_text="Часы", justify="center", font=my_font, width=150)

entry2 = ctk.CTkEntry(master=root)
entry2.configure(placeholder_text="Минуты", justify="center", font=my_font, width=150)

entry3 = ctk.CTkEntry(master=root)
entry3.configure(placeholder_text="Секунды", justify="center", font=my_font, width=150)

label_time = ctk.CTkLabel(
    master=root,
    text="00:00:00",
    font=ctk.CTkFont(size=64, weight="bold"),
    fg_color="transparent"
)

btn_start = ctk.CTkButton(
    master=root,
    text="Старт",
    font=my_font,
    width=150,
    text_color="white",
    fg_color="#1FC26D",
    hover_color="#147D46",
    command=start_timer
)

btn_pause = ctk.CTkButton(
    master=root,
    text="Пауза",
    font=my_font,
    width=150,
    fg_color="#FFA500",
    hover_color="#CC8400",
    command=pause_timer
)

btn_reset = ctk.CTkButton(
    master=root,
    text="Сброс",
    font=my_font,
    width=150,
    fg_color="#E34234",
    hover_color="#B22222",
    command=reset_timer
)

# ------------------ Размещение ------------------
entry1.pack(pady=(50, 10))
entry2.pack(pady=10)
entry3.pack(pady=10)
label_time.pack(pady=20)
btn_start.pack(pady=10)
btn_pause.pack(pady=10)
btn_reset.pack(pady=10)

root.mainloop()
