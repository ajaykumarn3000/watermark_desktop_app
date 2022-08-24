from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont


def open_file():
    file = filedialog.askopenfile(mode='r')
    if file:
        path = file.name
        file_name = path.split("/")[-1]
        result = path.replace(file_name, "")
        print(path)
        print(file_name)
        print(result)

        image1 = Image.open(path)
        width, height = image1.size

        ratio = width / height
        if width > height:
            new_width = 400
            new_height = int(400 / ratio)
        elif width < height:
            new_height = 400
            new_width = int(400 * ratio)
        else:
            new_width = 400
            new_height = 400

        image2 = image1.resize((new_width, new_height), Image.LANCZOS)
        test = ImageTk.PhotoImage(image2)

        def add_watermark():
            colors = [(0, 0, 0, 128), (255, 255, 255, 128), (255, 255, 0, 128), (255, 0, 0, 128), (0, 255, 0, 128), (0, 0, 255, 128)]
            watermark_text = watermark_input.get()
            text = watermark_text
            color_no = radio_state.get()
            x = int(x_spinbox.get())
            y = int(y_spinbox.get())

            with Image.open(path).convert("RGBA") as base:
                txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
                # get a font
                fnt = ImageFont.truetype('arial', 150)
                # get a drawing context
                d = ImageDraw.Draw(txt)

                # draw text, half opacity
                d.text((x, y), text, font=fnt, fill=colors[color_no])

                out = Image.alpha_composite(base, txt)
                out.save(f"{result}results.png")
                out.show()

            # wm_font = ImageFont.truetype('arial', 60)
            # result = ImageDraw.Draw(image1)
            # result.text((x, y), text, colors[color_no], font=wm_font, stroke_width=0, anchor="mm", align="center")
            # image1.save("C:\\Users\Ajay kumar\Desktop\\results.png")

        work_image = Label(image=test)
        work_image.image = test

        window.config(padx=20, pady=20)

        welcome_label.config(font=('algerian', 15, 'italic'), foreground="cyan")
        welcome_label.grid(row=0, column=0, columnspan=10)

        path_label = Label(text=f"'{file_name}'", font=('arial', 15, ""), foreground="white", background="black")
        path_label.grid(row=1, column=0)

        browse_button.destroy()

        work_image.grid(row=2, column=0, columnspan=2, rowspan=100, padx=20)

        # Watermark area

        watermark_label = Label(text="Watermark text:", font=('arial', 15, ""), foreground="yellow", background="black")
        watermark_label.grid(row=2, column=2, columnspan=10)

        watermark_input = Entry(width=50)
        watermark_input.grid(row=3, column=2, columnspan=10)

        blank = Label(text="", foreground="black", background="black")
        blank.grid(row=4, column=2)
        # ----------------------------------------------------------
        position_label = Label(text="Watermark position:", font=('arial', 15, ""), foreground="yellow",
                               background="black")
        position_label.grid(row=5, column=2, columnspan=10)

        x_position_label = Label(text="X value:", font=('arial', 15), background="black", foreground="orange")
        x_position_label.grid(row=6, column=2)

        x_spinbox = Spinbox(from_=1, to=width, width=7)
        x_spinbox.grid(row=6, column=3)

        blank_pos = Label(text="", foreground="black", background="black")
        blank_pos.grid(row=6, column=4)

        y_position_label = Label(text="Y value: ", font=('arial', 15), background="black", foreground="orange")
        y_position_label.grid(row=6, column=5)

        y_spinbox = Spinbox(from_=1, to=height, width=7)
        y_spinbox.grid(row=6, column=6)

        blank_ = Label(text="", foreground="black", background="black")
        blank_.grid(row=7, column=2, columnspan=10)

        color_label = Label(text="Add color: ", font=('arial', 15, ""), foreground="yellow", background="black")
        color_label.grid(row=8, column=2, columnspan=10)

        radio_state = IntVar()

        color0 = Radiobutton(text="White", value=0, variable=radio_state, background="white")
        color0.grid(row=9, column=2)

        blank_1 = Label(text="", foreground="black", background="black")
        blank_1.grid(row=9, column=3)

        color1 = Radiobutton(text="Black", value=1, variable=radio_state, background="grey")
        color1.grid(row=9, column=4)

        blank_2 = Label(text="", foreground="black", background="black")
        blank_2.grid(row=9, column=5)

        color2 = Radiobutton(text="Yellow", value=2, variable=radio_state, background="yellow")
        color2.grid(row=9, column=6)

        color3 = Radiobutton(text="Red", value=3, variable=radio_state, background="red")
        color3.grid(row=10, column=2)

        blank_3 = Label(text="", foreground="black", background="black")
        blank_3.grid(row=10, column=3)

        color4 = Radiobutton(text="Green", value=4, variable=radio_state, background="green")
        color4.grid(row=10, column=4)

        blank_4 = Label(text="", foreground="black", background="black")
        blank_4.grid(row=10, column=5)

        color5 = Radiobutton(text="Blue", value=5, variable=radio_state, background="blue")
        color5.grid(row=10, column=6)

        blank_5 = Label(text="", foreground="black", background="black")
        blank_5.grid(row=11, column=2, columnspan=10)

        watermark_button = Button(text="LETS GOOO!!", command=add_watermark)
        watermark_button.grid(row=12, column=2, columnspan=10)


window = Tk()
window.title("Watermark.exe")
window.minsize(height=500, width=800)
window.config(padx=200, pady=200, background="black")

welcome_label = Label(text="Watermark.exe", font=('algerian', 50, 'italic'), foreground="white", background="black")
welcome_label.grid(row=0)

browse_button = Button(text="Browse Image", command=open_file)
browse_button.config(font=('arial', 15,), foreground="white", background="grey")
browse_button.grid(row=1)

window.mainloop()
