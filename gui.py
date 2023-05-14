from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

from main import get_five_movies

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assetsv2/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def get_movies(x):
    movies = get_five_movies(x)
    canvas.delete("one")
    canvas.delete("two")
    canvas.delete("three")
    canvas.delete("four")
    canvas.delete("five")
    canvas.create_text(
        911.07470703125,
        693.66796875,
        anchor="nw",
        text=movies[0],
        fill="#000000",
        font=("NerkoOne Regular", 16 * -1),
        width=150,
        tags="one"
    )
    canvas.create_text(
        691.32177734375,
        693.66796875,
        anchor="nw",
        text=movies[1],
        fill="#000000",
        font=("NerkoOne Regular", 16 * -1),
        width=150,
        tags="two"
    )
    canvas.create_text(
        471.5693359375,
        693.66796875,
        anchor="nw",
        text=movies[2],
        fill="#000000",
        font=("NerkoOne Regular", 16 * -1),
        width=150,
        tags="three"
    )
    canvas.create_text(
        251.81640625,
        693.66796875,
        anchor="nw",
        text=movies[3],
        fill="#000000",
        font=("NerkoOne Regular", 16 * -1),
        width=150,
        tags="four"
    )
    canvas.create_text(
        32.0634765625,
        693.66796875,
        anchor="nw",
        text=movies[4],
        fill="#000000",
        font=("NerkoOne Regular", 16 * -1),
        width=150,
        tags="five"
    )

window = Tk()

window.geometry("1126x801")
window.configure(bg = "#FFFFFF")


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
    highlightthickness=0
)
entry_1.place(
    x=150.0,
    y=331.0,
    width=725.0,
    height=45.0
)

canvas.create_text(
    150.0,
    300.0,
    anchor="nw",
    text="Search for your favourite movie or TV series:",
    fill="#000000",
    font=("NerkoOne Regular", 32 * -1)
)

canvas.create_text(
    32.0,
    440.0,
    anchor="nw",
    text="Results:",
    fill="#000000",
    font=("NerkoOne Regular", 32 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: get_movies(entry_1.get()),
    relief="flat"
)
button_1.place(
    x=875.10107421875,
    y=330.8022155761719,
    width=101.66497802734375,
    height=46.92230224609375
)

# button_image_2 = PhotoImage(
#     file=relative_to_assets("button_2.png"))
# button_2 = Button(
#     image=button_image_2,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_2 clicked"),
#     relief="flat"
# )
# button_2.place(
#     x=911.07470703125,
#     y=470.0050354003906,
#     width=182.9969482421875,
#     height=304.9949645996094
# )

canvas.create_text(
    911.07470703125,
    693.66796875,
    anchor="nw",
    text="title1",
    fill="#000000",
    font=("NerkoOne Regular", 32 * -1),
    tags="one"
)

# button_image_3 = PhotoImage(
#     file=relative_to_assets("button_3.png"))
# button_3 = Button(
#     image=button_image_3,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_3 clicked"),
#     relief="flat"
# )
# button_3.place(
#     x=691.32177734375,
#     y=470.0050354003906,
#     width=182.99697875976562,
#     height=304.9949645996094
# )

canvas.create_text(
    691.32177734375,
    693.66796875,
    anchor="nw",
    text="title1",
    fill="#000000",
    font=("NerkoOne Regular", 32 * -1),
    tags="two"
)

# button_image_4 = PhotoImage(
#     file=relative_to_assets("button_4.png"))
# button_4 = Button(
#     image=button_image_4,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_4 clicked"),
#     relief="flat"
# )
# button_4.place(
#     x=471.5693359375,
#     y=470.0050354003906,
#     width=182.99697875976562,
#     height=304.9949645996094
# )

canvas.create_text(
    471.5693359375,
    693.66796875,
    anchor="nw",
    text="title1",
    fill="#000000",
    font=("NerkoOne Regular", 32 * -1),
    tags="three"
)

# button_image_5 = PhotoImage(
#     file=relative_to_assets("button_5.png"))
# button_5 = Button(
#     image=button_image_5,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_5 clicked"),
#     relief="flat"
# )
# button_5.place(
#     x=251.81634521484375,
#     y=470.0050354003906,
#     width=182.99697875976562,
#     height=304.9949645996094
# )

canvas.create_text(
    251.81640625,
    693.66796875,
    anchor="nw",
    text="title1",
    fill="#000000",
    font=("NerkoOne Regular", 32 * -1),
    tags="four"
)

# button_image_6 = PhotoImage(
#     file=relative_to_assets("button_6.png"))
# button_6 = Button(
#     image=button_image_6,
#     borderwidth=0,
#     highlightthickness=0,
#     command=lambda: print("button_6 clicked"),
#     relief="flat"
# )
# button_6.place(
#     x=32.0634765625,
#     y=470.0050354003906,
#     width=182.99697875976562,
#     height=304.9949645996094
# )

canvas.create_text(
    32.0634765625,
    693.66796875,
    anchor="nw",
    text="title1",
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
