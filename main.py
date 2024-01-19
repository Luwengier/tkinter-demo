import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()


def add(*args) -> None:
    """Adds all the numbers in the args together and prints the result"""
    for n in args:
        print(n)


window.mainloop()
