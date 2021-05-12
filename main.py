from config import *
from tkinter import *
from tkinter import messagebox
from tkcalendar import *
from datetime import datetime as dt
from PIL import Image, ImageTk
import requests
import webbrowser

root = Tk()  # Create object
root.title("My Python Journey")
root.geometry("404x404")  # Adjust size
root.iconphoto(True, PhotoImage(file="images/code-icon.png"))
root.resizable(width=False, height=False)

image = Image.open("images/background-code.png")  # Read the Image

# Reszie the image using resize() method
resize_image = image.resize((400, 400))
img = ImageTk.PhotoImage(resize_image)

label1 = Label(root, image=img)  # Show image using label
label1.image = img
label1.grid(row=0, column=0, columnspan=4, rowspan=4)
frame1 = Frame(root)  # Create Frame
frame1.grid(row=0, column=0)

TODAY = dt.now()


def open_browser():
    webbrowser.open(url=URL, new=1)


def format_date():
    cal.config(date_pattern="yyyyMMdd")
    date = cal.get_date()
    cal.config(date_pattern="dd/MM/yyyy")
    return date


def add_pixel():
    pixel_add = {
        "date": format_date(),
        "quantity": user_in.get(),
    }
    response = requests.post(
        url=PIXELA_ENDPOINT, json=pixel_add, headers=headers)
    response.raise_for_status()
    user_in.delete(0, END)
    messagebox.showinfo(title="Infobox", message="Pixel added.")


def del_pixel():
    formatted_date = format_date()
    response = requests.delete(
        url=f"{PIXELA_ENDPOINT}/{formatted_date}", headers=headers)
    response.raise_for_status()
    messagebox.showinfo(title="Infobox", message="Pixel deleted.")


def change_pixel():
    formatted_date = format_date()
    pixel_update = {
        "quantity": user_in.get()
    }
    response = requests.put(
        url=f"{PIXELA_ENDPOINT}/{formatted_date}", json=pixel_update, headers=headers)
    response.raise_for_status()
    user_in.delete(0, END)
    messagebox.showinfo(title="Infobox", message="Pixel updated.")


cal = Calendar(root, selectmode="day", cursor="hand2", borderwidth=4, background=BACKGROUND, selectbackground=BACKGROUND, foreground=FOREGROUND, font=(FONT_LOOK), year=TODAY.year,
               month=TODAY.month, day=TODAY.day)
cal.grid(row=1, column=0, columnspan=4)
units = Label(text="Hours/Day:", background=BACKGROUND,
              foreground=FOREGROUND, font=(FONT_LOOK))
units.grid(row=2, column=0, columnspan=2, padx=10, sticky="e")
user_in = Entry(width=10)
user_in.grid(row=2, column=2, sticky="w")


# Buttons
add = Button(text="Add", background=BACKGROUND,
             foreground=FOREGROUND, font=(FONT_LOOK), command=add_pixel)
add.grid(row=3, column=0, pady=10)
update = Button(text="Update", background=BACKGROUND,
                foreground=FOREGROUND, font=(FONT_LOOK), command=change_pixel)
update.grid(row=3, column=1, pady=10, sticky="w")
delete = Button(text="Delete", background=BACKGROUND,
                foreground=FOREGROUND, font=(FONT_LOOK), command=del_pixel)
delete.grid(row=3, column=2, pady=10, sticky="w")
link = Button(text="Show\nJourney", background=BACKGROUND,
              foreground=FOREGROUND, font=(FONT_LOOK), command=open_browser)
link.grid(row=3, column=3)


root.mainloop()  # Execute tkinter
