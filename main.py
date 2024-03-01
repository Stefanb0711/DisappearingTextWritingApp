import time
from tkinter import *
from time import sleep



def objekte_zentrieren():
    x_center = window.winfo_width // 2
    y_center = window.winfo_width // 2




def text_löscher(event):
    #erste_zeit = time.time()
    #sleep(5)


    #window.after(3000, lambda: text_feld.delete("end-2c", "end-1c"))

    text_feld.config(borderwidth=2, relief="solid", highlightbackground="red")


def letzten_zeichen_löschen():

    """counter_var.set(counter_var.get() - 1)


    label_timer.config(text=f"{counter_var.get()}")

    if counter_var.get() > 0:
        window.after(1000, )"""


    text = text_feld.get("1.0", "end-1c")
    if text:
        text_feld.delete("end-3c", "end-1c")
        window.after(200, letzten_zeichen_löschen)


def countdowner(counter_var):
    counter_var.set(counter_var.get() - 1)

    label_timer.config(text=f"{counter_var.get()}")

    if counter_var.get() > 0:
        window.after(1000, countdowner, counter_var)


    #zeit_differenz = time.time() - erste_zeit


"""def on_key_press(event):
    key = event.keysym
    label.config(text=f"Du hast die Taste '{key}' gedrückt.")"""

window = Tk()
window.config()
window.title("Secret Writer")

window.geometry("1000x600")

window.resizable(False,False)

counter = IntVar(value=6)

erklärung_label = Label(window, text="Wenn du aufhörst zu schreiben, verschwindet der Text", font=("Helvetica", 15))
erklärung_label.place(x = 500, y = 100, anchor = CENTER)
#erklärung_label.grid(row=1, column=1)


text_feld = Text(window)
text_feld.place(x = 500, y = 350, anchor = CENTER)

label_timer = Label(window, font=("Helvetica"))
label_timer.pack()

window.after(5000, countdowner, counter )

window.after(5000, letzten_zeichen_löschen)


#text_feld.bind("<KeyPress>", letzten_zeichen_löschen)




window.mainloop()


#Wenn 3 sekunden nicht geschrieben wird, verschindet 1 buchstabe pro sekunde

#Wenn 7 sekunden nicht geschrieben wird 2 pro sec

#Wenn 12 sec dann 3