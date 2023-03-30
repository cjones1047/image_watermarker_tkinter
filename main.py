from tkinter import *
from tkinter import filedialog

FONT_TUPLE = ("Arial", 17, "normal")


def open_image():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select an Image",
        filetypes=[
            ("Image file","*.jpeg"), ("Image file", "*.jpg"), ("Image file", "*.png")
        ]
    )

    # Change label contents
    print(filename)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Image Watermarker")
window.config(padx=50, pady=50)

# Set window size
# window.geometry("500x500")

# Create a File Explorer label
select_image_prompt = Label(
    window,
    text="Start by finding an image to watermark",
    width=100, height=4,
    fg="white"
)

select_image_button = Button(
    text="Select Image",
    command=open_image
)

# button_exit = Button(window,
#                      text="Exit",
#                      command=exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
select_image_prompt.grid(column=1, row=1)

select_image_button.grid(column=1, row=2)

window.mainloop()
