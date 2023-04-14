from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets/frame2")


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
    191.76922988891602,
    656.9059753417969,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    720.0,
    173.0,
    image=image_image_2
)

canvas.create_text(
    494.0,
    595.0,
    anchor="nw",
    text="OpisOpisOpisOpisOpisOpisOpisOpisOpisOpisOpisOpisOpisOpisOpis",
    fill="#000000",
    font=("NerkoOne Regular", 64 * -1)
)

canvas.create_text(
    494.0,
    484.0,
    anchor="nw",
    text="Title",
    fill="#000000",
    font=("NerkoOne Regular", 96 * -1)
)
window.resizable(False, False)
window.mainloop()
