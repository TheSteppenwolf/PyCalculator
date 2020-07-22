from tkinter import *
# Creation of the window.
window = Tk()
# Assigning a title to the window.
window.title("PyCalculator")

# Global variables
INDEX = 0

# Textbox to watch the entry of data.
outputs = Entry(window, font=("Calibri 20"))
outputs.grid(row=0, column=0, columnspan = 4, padx = 5, pady = 5)

# Useful methods
def click(valor):
	global INDEX
	outputs.insert(INDEX, valor)
	INDEX += 1

def delete_Calc():
	outputs.delete(0, END)
	INDEX = 0

def result():
	ecuation = outputs.get()
	outputs.delete(0, END)
	INDEX = 0
	outputs.insert(INDEX, eval(ecuation))	

# Setting the buttons of the calculator:
# Setting the numbers:
button0 = Button(window, text="0", width=13, height=2, command=lambda:click(0))
button1 = Button(window, text="1", width=5, height=2, command=lambda:click(1))
button2 = Button(window, text="2", width=5, height=2, command=lambda:click(2))
button3 = Button(window, text="3", width=5, height=2, command=lambda:click(3))
button4 = Button(window, text="4", width=5, height=2, command=lambda:click(4))
button5 = Button(window, text="5", width=5, height=2, command=lambda:click(5))
button6 = Button(window, text="6", width=5, height=2, command=lambda:click(6))
button7 = Button(window, text="7", width=5, height=2, command=lambda:click(7))
button8 = Button(window, text="8", width=5, height=2, command=lambda:click(8))
button9 = Button(window, text="9", width=5, height=2, command=lambda:click(9))
# Setting the operations and extras:
button_clear = Button(window, text="AC", width=5, height=2, command=delete_Calc)
button_open_parenthesis = Button(window, text="(", width=5, height=2, command=lambda:click("("))
button_close_parenthesis = Button(window, text=")", width=5, height=2, command=lambda:click(")"))
button_dot = Button(window, text=".", width=5, height=2, command=lambda:click("."))
button_division = Button(window, text="/", width=5, height=2, command=lambda:click("/"))
button_product = Button(window, text="*", width=5, height=2, command=lambda:click("*"))
button_minus = Button(window, text="-", width=5, height=2, command=lambda:click("-"))
button_plus = Button(window, text="+", width=5, height=2, command=lambda:click("+"))
button_result = Button(window, text="=", width=5, height=2, command=result)
# Button positioning.
button_clear.grid(row=1, column=0, padx=5, pady=5)
button_open_parenthesis.grid(row=1, column=1, padx=5, pady=5)
button_close_parenthesis.grid(row=1, column=2, padx=5, pady=5)
button_division.grid(row=1, column=3, padx=5, pady=5)
button7.grid(row=2, column=0, padx=5, pady=5)
button8.grid(row=2, column=1, padx=5, pady=5)
button9.grid(row=2, column=2, padx=5, pady=5)
button_product.grid(row=2, column=3, padx=5, pady=5)
button4.grid(row=3, column=0, padx=5, pady=5)
button5.grid(row=3, column=1, padx=5, pady=5)
button6.grid(row=3, column=2, padx=5, pady=5)
button_plus.grid(row=3, column=3, padx=5, pady=5)
button1.grid(row=4, column=0, padx=5, pady=5)
button2.grid(row=4, column=1, padx=5, pady=5)
button3.grid(row=4, column=2, padx=5, pady=5)
button_minus.grid(row=4, column=3, padx=5, pady=5)
button0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
button_dot.grid(row=5, column=2, padx=5, pady=5)
button_result.grid(row=5, column=3, padx=5, pady=5)


# Lets all events be recorded and analyzed
window.mainloop()