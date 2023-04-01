from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont

FONT_TUPLE = ("Arial", 17, "normal")


def open_image():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select an Image",
        filetypes=[
            ("Image file","*.jpeg"), ("Image file", "*.jpg"), ("Image file", "*.png")
        ]
    )

    # Create a photoimage object of the image in the path and resize it while maintaining aspect ratio
    basewidth = 500
    image_file = Image.open(filename)
    w_percent = (basewidth / float(image_file.size[0]))
    h_size = int((float(image_file.size[1]) * float(w_percent)))
    image_file = image_file.resize((basewidth, h_size))
    image_file = image_file.convert('RGBA')
    base = Image.new('RGBA', image_file.size, (255, 255, 255, 0))
    fnt = ImageFont.truetype("Slabo27px-Regular.ttf", 200)
    draw = ImageDraw.Draw(base, 'RGBA')
    draw.text((100, h_size - 230), "CCJ", fill=(255, 255, 255, 100), font=fnt)
    out = Image.alpha_composite(image_file, base)

    image = ImageTk.PhotoImage(out)

    image_area = Label(image=image, relief='ridge')
    image_area.image = image

    # Position image
    image_area.grid(column=1, row=1, pady=20)

    select_image_button.destroy()


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

select_image_prompt.grid(column=1, row=1)

select_image_button.grid(column=1, row=2)

window.mainloop()
