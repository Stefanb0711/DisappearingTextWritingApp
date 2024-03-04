from tkinter import *

def timer_starten():
    current_value = count_var.get()
    if current_value > 0:
        count_var.set(current_value - 1)
        label_timer.config(text= str(current_value))
        timer_id = label_timer.after(1000, timer_starten)


    else:
        timer_zurücksetzen()


def timer_zurücksetzen():
    timer_gestartet.set(False)
    count_var.set(6)
    label_timer.config(text=str(count_var.get()))



def onkey_pressed():
    # Wenn Timer gestartet wurde
    if timer_gestartet.get():
        timer_zurücksetzen()
        timer_gestartet.set(False)

    elif not timer_gestartet.get():
        timer_starten()
        timer_gestartet.set(True)








root = Tk()
root.title("Textfeld - Zeichen löschen jede Sekunde")

text_feld = Text(root, height=5, width=30, wrap="word")
text_feld.pack(pady=10)

count_var = IntVar(value=6)
timer_gestartet = BooleanVar(value=False)

label_timer = Label(root, text="")
label_timer.pack()


klick_button = Button(root, text="Start", command=onkey_pressed)
klick_button.pack()

#text_feld.bind("<Key>", onkey_pressed)

root.mainloop()
