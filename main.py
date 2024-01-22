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


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")


my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)


window.mainloop()
