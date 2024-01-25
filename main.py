import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()


def button_clicked():
    """This function will be called when the button is clicked"""
    new_text = input.get()
    my_label.config(text=new_text)


# Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry
input = tkinter.Entry(width=10)
input.pack()


window.mainloop()
