from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar
from PIL import ImageTk
from urllib.request import urlopen

from main import get_five_movies

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assetsv2/frame0")
URL_PREFIX = "https://image.tmdb.org/t/p/w500"

options = [
    "Title",
    "Director"
]

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def get_movies(x):
    movies = get_five_movies(x)
    #posters = get_five_posters(movies)   ---------------------------------------------TUTAJ PROSZE O POSTERY-------------------------------------------

    canvas.delete("one")
    canvas.delete("two")
    canvas.delete("three")
    canvas.delete("four")
    canvas.delete("five")
    canvas.delete("firstPoster")
    canvas.delete("secondPoster")
    canvas.delete("thirdPoster")
    canvas.delete("fourthPoster")
    canvas.delete("fifthPoster")
    canvas.create_text(
        911.07470703125,
        693.66796875,
        anchor="nw",
        text=movies[4],
        fill="#000000",
        font=("Nerko One", 16 * -1),
        width=150,
        tags="five"
    )
    # u4 = urlopen(URL_PREFIX + posters[4])
    # fifth_poster_raw = u4.read()
    # u4.close()
    # button_image_4 = ImageTk.PhotoImage(
    #     fifth_poster=fifth_poster_raw)
    # button_4 = Button(
    #     image=button_image_4,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_4 clicked"),
    #     relief="flat",
    #     tags="fifthPoster"
    # )
    # button_4.image = button_image_4
    # button_4.pack()
    #
    # button_4.place(
    #     x=911.07470703125,
    #     y=470.0050354003906,
    #     width=182.9969482421875,
    #     height=220
    # )
    canvas.create_text(
        691.32177734375,
        693.66796875,
        anchor="nw",
        text=movies[3],
        fill="#000000",
        font=("Nerko One", 16 * -1),
        width=150,
        tags="four"
    )
    # u3 = urlopen(URL_PREFIX + posters[3])
    # fourth_poster_raw = u3.read()
    # u3.close()
    # button_image_3 = ImageTk.PhotoImage(
    #     fourth_poster=fourth_poster_raw)
    # button_3 = Button(
    #     image=button_image_3,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_3 clicked"),
    #     relief="flat",
    #     tags="fourthPoster"
    # )
    # button_3.image = button_image_3
    # button_3.pack()
    #
    # button_3.place(
    #     x=691.32177734375,
    #     y=470.0050354003906,
    #     width=182.9969482421875,
    #     height=220
    # )

    canvas.create_text(
        471.5693359375,
        693.66796875,
        anchor="nw",
        text=movies[2],
        fill="#000000",
        font=("Nerko One", 16 * -1),
        width=150,
        tags="three"
    )
    # u2 = urlopen(URL_PREFIX + posters[2])
    # third_poster_raw = u2.read()
    # u2.close()
    # button_image_2 = ImageTk.PhotoImage(
    #     third_poster=third_poster_raw)
    # button_2 = Button(
    #     image=button_image_2,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_2 clicked"),
    #     relief="flat",
    #     tags="thirdPoster"
    # )
    # button_2.image = button_image_2
    # button_2.pack()
    #
    # button_2.place(
    #     x=471.5693359375,
    #     y=470.0050354003906,
    #     width=182.9969482421875,
    #     height=220
    # )

    canvas.create_text(
        251.81640625,
        693.66796875,
        anchor="nw",
        text=movies[1],
        fill="#000000",
        font=("Nerko One", 16 * -1),
        width=150,
        tags="two"
    )
    # u1 = urlopen(URL_PREFIX + posters[1])
    # second_poster_raw = u1.read()
    # u1.close()
    # button_image_1 = ImageTk.PhotoImage(
    #     second_poster=second_poster_raw)
    # button_1 = Button(
    #     image=button_image_1,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_1 clicked"),
    #     relief="flat",
    #     tags="secondPoster"
    # )
    # button_1.image = button_image_1
    # button_1.pack()
    #
    # button_1.place(
    #     x=251.81634521484375,
    #     y=470.0050354003906,
    #     width=182.9969482421875,
    #     height=220
    # )

    canvas.create_text(
        32.0634765625,
        693.66796875,
        anchor="nw",
        text=movies[0],
        fill="#000000",
        font=("Nerko One", 16 * -1),
        width=150,
        tags="one"
    )
    # u0 = urlopen(URL_PREFIX + posters[0])
    # first_poster_raw = u0.read()
    # u0.close()
    # button_image_0 = ImageTk.PhotoImage(
    #     first_poster=first_poster_raw)
    # button_0 = Button(
    #     image=button_image_0,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: print("button_0 clicked"),
    #     relief="flat",
    #     tags="firstPoster"
    # )
    # button_0.image = button_image_0
    # button_0.pack()
    #
    # button_0.place(
    #     x=32.0634765625,
    #     y=470.0050354003906,
    #     width=182.9969482421875,
    #     height=220
    # )

window = Tk()
dropdown_variable = StringVar(window)
dropdown_variable.set("Title")

window.geometry("1126x801")
window.configure(bg = "#FFFFFF")
window.title("Recommendinator")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 801,
    width = 1126,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    512.5,
    354.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=("NerkoOne", 24 * -1)
)
entry_1.place(
    x=153.0,
    y=334.0,
    width=722.0,
    height=42.0
)

canvas.create_text(
    150.0,
    300.0,
    anchor="nw",
    text="Search for your favourite movie or TV series:",
    fill="#000000",
    font=("Nerko One", 32 * -1)
)

dropdown = OptionMenu(window, dropdown_variable, *options)
dropdown.pack()
dropdown.config(font=("Nerko One", 20 * -1))
dropdown.place(x=750,
               y=330,
               width=125,
               height=50)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print(get_movies(entry_1.get())),
    relief="flat"
)
button_1.place(
    x=875.10107421875,
    y=330.8022155761719,
    width=101.66497802734375,
    height=46.92230224609375
)

canvas.create_text(
    32.0,
    440.0,
    anchor="nw",
    text="Results:",
    fill="#000000",
    font=("Nerko One", 32 * -1)
)

canvas.create_text(
    911.07470703125,
    693.66796875,
    anchor="nw",
    text="",
    fill="#000000",
    font=("NerkoOne Regular", 32 * -1),
    tags="one"
)

canvas.create_text(
    691.32177734375,
    693.66796875,
    anchor="nw",
    text="",
    fill="#000000",
    font=("NerkoOne Regular", 32 * -1),
    tags="two"
)

canvas.create_text(
    471.5693359375,
    693.66796875,
    anchor="nw",
    text="",
    fill="#000000",
    font=("NerkoOne Regular", 32 * -1),
    tags="three"
)

canvas.create_text(
    251.81640625,
    693.66796875,
    anchor="nw",
    text="",
    fill="#000000",
    font=("NerkoOne Regular", 32 * -1),
    tags="four"
)

canvas.create_text(
    32.0634765625,
    693.66796875,
    anchor="nw",
    text="",
    fill="#000000",
    font=("NerkoOne Regular", 32 * -1),
    tags="five"
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    563.0,
    135.0,
    image=image_image_1
)

window.resizable(False, False)
window.mainloop()
