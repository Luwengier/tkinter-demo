import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()


def button_clicked():
    """This function will be called when the button is clicked"""
    my_label.config(text="I got clicked")


# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()


window.mainloop()
