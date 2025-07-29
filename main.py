from tkinter import*
root = Tk()

# Text Input
e = Entry(root, width=20, border=5)
e.grid(row=0, column=0, columnspan=3, padx=0, pady=0)


def num_input(number):
    current_value = e.get()
    e.delete(0, END)
    e.insert(0, str(current_value)+str(number))


def clear_val():
    e.delete(0, END)


# Function to evaluate the expression
def equals():
    num1 = e.get()
    ans = str(eval(num1))
    e.delete(0,END)
    e.insert(0,ans)


# Button 9-0 , add ,sub, clear ,equal
button9 = Button(root, text="9", padx=20, pady=20, command=lambda: num_input(9)).grid(row=1, column=0)
button8 = Button(root, text="8", padx=20, pady=20, command=lambda: num_input(8)).grid(row=1, column=1)
button7 = Button(root, text="7", padx=20, pady=20, command=lambda: num_input(7)).grid(row=1, column=2)

button6 = Button(root, text="6", padx=20, pady=20, command=lambda: num_input(6)).grid(row=2, column=0)
button5 = Button(root, text="5", padx=20, pady=20, command=lambda: num_input(5)).grid(row=2, column=1)
button4 = Button(root, text="4", padx=20, pady=20, command=lambda: num_input(4)).grid(row=2, column=2)

button3 = Button(root, text="3", padx=20, pady=20, command=lambda: num_input(3)).grid(row=3, column=0)
button2 = Button(root, text="2", padx=20, pady=20, command=lambda: num_input(2)).grid(row=3, column=1)
button1 = Button(root, text="1", padx=20, pady=20, command=lambda: num_input(1)).grid(row=3, column=2)

button0 = Button(root, text="0", padx=20, pady=20, command=lambda: num_input(0)).grid(row=4, column=0)

button_add = Button(root, text="+", padx=20, pady=20, command=lambda: num_input("+")).grid(row=4, column=1)
button_clear = Button(root, text="clear", padx=20, pady=20, command=lambda: clear_val()).grid(row=5, column=0)
button_equal = Button(root, text="=", padx=20, pady=20, command=lambda: equals()).grid(row=4, column=2)

root.mainloop()