from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from main import get_five_movies

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    655.0,
    453.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    655.5,
    453.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=197.0,
    y=428.0,
    width=917.0,
    height=48.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print(get_five_movies(entry_1.get())),
    relief="flat"
)
button_1.place(
    x=1119.0,
    y=423.0,
    width=130.0,
    height=60.0
)

canvas.create_text(
    192.0,
    384.0,
    anchor="nw",
    text="Search for your favourite movie or TV series:",
    fill="#000000",
    font=("NerkoOne Regular", 32 * -1)
)

canvas.create_text(
    41.0,
    562.0,
    anchor="nw",
    text="Or choose from popular:",
    fill="#000000",
    font=("NerkoOne Regular", 32 * -1)
)

film1 = PhotoImage(
    file=relative_to_assets("button_4.png"))
przycisk_film1 = Button(
    image=film1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("film1"),
    relief="flat"
)
przycisk_film1.place(
    x=41.0,
    y=601.0,
    width=234.0,
    height=390.0
)

film2 = PhotoImage(
    file=relative_to_assets("button_3.png"))
przycisk_film2 = Button(
    image=film2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("film2"),
    relief="flat"
)
przycisk_film2.place(
    x=322.0,
    y=601.0,
    width=234.0,
    height=390.0
)

film3 = PhotoImage(
    file=relative_to_assets("button_2.png"))
przycisk_film3 = Button(
    image=film3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("film3"),
    relief="flat"
)
przycisk_film3.place(
    x=603.0,
    y=601.0,
    width=234.0,
    height=390.0
)

film4 = PhotoImage(
    file=relative_to_assets("button_5.png"))
przycisk_film4 = Button(
    image=film4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
przycisk_film4.place(
    x=884.0,
    y=601.0,
    width=234.0,
    height=390.0
)

film5 = PhotoImage(
    file=relative_to_assets("button_6.png"))
przycisk_film5 = Button(
    image=film5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
przycisk_film5.place(
    x=1165.0,
    y=601.0,
    width=234.0,
    height=390.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    720.0,
    173.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
