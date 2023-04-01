from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
from functools import partial


def reset_gui(image_area):
    global save_image_button, discard_image_button
    save_image_button.destroy()
    discard_image_button.destroy()
    image_area.destroy()
    select_image_button.grid(column=1, row=2)


def save_image(filename, image, image_area):
    filename_list = filename.rsplit('/', 1)
    watermarked_filename = filename_list[0] + '/watermarked_' + filename_list[1][:filename_list[1].index('.')] + '.png'

    image.save(watermarked_filename)

    messagebox.showinfo(
        title="Done",
        message=f"Image saved at\n{watermarked_filename}"
    )

    reset_gui(image_area)


def open_image():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select an Image",
        filetypes=[
            ("Image file", "*.jpeg"), ("Image file", "*.jpg"), ("Image file", "*.png")
        ]
    )

    basewidth = 500
    try:
        image_file = Image.open(filename)
    except AttributeError:
        return
    w_percent = (basewidth / float(image_file.size[0]))
    h_size = int((float(image_file.size[1]) * float(w_percent)))
    image_file = image_file.resize((basewidth, h_size))
    image_file = image_file.convert('RGBA')
    base = Image.new('RGBA', image_file.size, (255, 255, 255, 0))
    fnt = ImageFont.truetype("Slabo27px-Regular.ttf", 200)
    draw = ImageDraw.Draw(base, 'RGBA')
    draw.text((100, h_size - 230), "CCJ", fill=(255, 255, 255, 100), font=fnt)
    out = Image.alpha_composite(image_file, base)

    # change GUI
    select_image_button.grid_forget()

    image = ImageTk.PhotoImage(out)
    image_area = Label(image=image, relief='ridge')
    image_area.image = image
    image_area.grid(column=1, row=1)

    global save_image_button
    save_image_button = Button(
        text="Save",
        command=partial(save_image, filename, out, image_area)
    )
    save_image_button.grid(column=1, row=2, pady=(20, 10))

    global discard_image_button
    discard_image_button = Button(
        text="Discard",
        command=partial(reset_gui, image_area)
    )
    discard_image_button.grid(column=1, row=3)


# ---------------------------- UI INITIAL SETUP ------------------------------- #
window = Tk()
frame = Frame(window)
window.title("Image Watermarker")
window.config(padx=50, pady=50)

select_image_prompt = Label(
        window,
        text="Start by finding an image to watermark",
        width=100, height=4,
        fg="white"
)

select_image_prompt.grid(column=1, row=1)

select_image_button = Button(
    text="Select Image",
    command=open_image
)
select_image_button.grid(column=1, row=2)

save_image_button = Button()
discard_image_button = Button()

window.mainloop()
