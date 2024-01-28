import tkinter

window = tkinter.Tk()
window.title("Unit Converter")
window.minsize(width=500, height=300)


input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

miles = tkinter.Label(text="Miles")
miles.grid(column=2, row=0)

is_equal_to = tkinter.Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

result = tkinter.Label(text="0")
result.grid(column=1, row=1)

km = tkinter.Label(text="Km")
km.grid(column=2, row=1)

button = tkinter.Button(text="Calculate")
button.grid(column=1, row=2)

window.mainloop()


# def button_clicked():
#     """This function will be called when the button is clicked"""
#     new_text = input.get()
#     my_label.config(text=new_text)


# window = tkinter.Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)

# # Label
# my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.grid(column=0, row=0)

# # Button
# button = tkinter.Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)

# button2 = tkinter.Button(text="New Button", command=button_clicked)
# button2.grid(column=2, row=0)

# # Entry
# input = tkinter.Entry(width=10)
# input.grid(column=3, row=2)


# window.mainloop()
