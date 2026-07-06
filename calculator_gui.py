from tkinter import *
from PIL import Image, ImageTk

def digit_handler(digit):
    current_text = result_label.cget("text") #to get the current text in the result label.
    if current_text == "0": #if the current text is 0, we will replace it with the digit that is clicked. this is to avoid having leading zeros in the result.
        result_label.config(text=digit) #to update the text in the result label to the digit that is clicked.
    else:
        result_label.config(text=current_text + digit) #to update the text in the result label to the current text + the digit that is clicked.

def operator_handler(operator):
    current_text = result_label.cget("text")
    if current_text and current_text[-1] in "+-*/": #to check if the last character in the current text is an operator. if it is, we will replace it with the new operator that is clicked. this is to avoid having multiple operators in a row.
        result_label.config(text=current_text[:-1] + operator) #to update the text in the result label to the current text without the last character + the new operator that is clicked.
    else:
        result_label.config(text=current_text + operator) #to update the text in the result label to the current text + the new operator that is clicked.

def clear_handler(cmd):
    if cmd == "Bsp":
        current_text = result_label.cget("text")
        if current_text: #to check if the current text is not empty. if it is not empty, we will remove the last character from the current text. this is to implement the backspace functionality.
            result_label.config(text=current_text[:-1]) #to update the text in the result label to the current text without the last character.
    elif cmd == "C":
        result_label.config(text="") #to clear the text in the result label.

def equal_handler(_):
    current_text = result_label.cget("text")
    try:
        result = eval(current_text) #to evaluate the expression in the current text and get the result. eval is a built-in function that can evaluate a string as a Python expression. we will use this to evaluate the expression in the result label and get the result.
        result_label.config(text=str(round(result,3))) #to update the text in the result label to the result of the evaluation.
        exp_label.config(text=current_text) #to update the text in the expression label to the current text.
    except Exception as e: #to catch any exceptions that may occur during the evaluation of the expression. this is to handle cases where the expression is invalid and cannot be evaluated.
        result_label.config(text="Error") #to update the text in the result label to "Error" if there is an exception during the evaluation of the expression.
        # clear_handler(None) #to clear the text in the result label after showing the error message.

root = Tk()
root.title("Calculator")
root.geometry("282x415")
root.resizable(0, 0)
root.configure(bg="black")

exp_label = Label(root,text = "0", bg="black", fg="white")
exp_label.grid(row=0, column=0, columnspan=15, pady=(5,5), padx=(5,5), sticky=E) #east
exp_label.config(font=("Arial", 14, "bold"))


result_label = Label(root,text = "", bg="black", fg="white")
result_label.grid(row=1, column=0, columnspan=10, pady=(15,20), sticky=E) #east
result_label.config(font=("Arial", 24, "bold"))

btn7 = Button(root,text = "7", bg="red", fg="white", width=5, height=2, command=lambda: digit_handler("7")) #to set the command of the button to a function that will handle the digit that is clicked. we will use a lambda function to pass the digit as an argument to the handler function.
btn7.grid(row=3, column=0)
btn7.config(font=("Arial", 14, "bold"), cursor="hand2")

btn8 = Button(root,text = "8", bg="red", fg="white", width=5, height=2, command=lambda: digit_handler("8"))
btn8.grid(row=3, column=1)
btn8.config(font=("Arial", 14, "bold"), cursor="hand2")

btn9 = Button(root,text = "9", bg="red", fg="white", width=5, height=2, command=lambda: digit_handler("9"))
btn9.grid(row=3, column=2)
btn9.config(font=("Arial", 14, "bold"), cursor="hand2")

btn_div = Button(root,text = "/", bg="red", fg="white", width=5, height=2, command=lambda: operator_handler("/"))
btn_div.grid(row=2, column=3)
btn_div.config(font=("Arial", 14, "bold"), cursor="hand2")

btn4 = Button(root,text = "4", bg="red", fg="white", width=5, height=2, command=lambda: digit_handler("4"))
btn4.grid(row=4, column=0)
btn4.config(font=("Arial", 14, "bold"), cursor="hand2")

btn5 = Button(root,text = "5", bg="red", fg="white", width=5, height=2, command=lambda: digit_handler("5"))
btn5.grid(row=4, column=1)
btn5.config(font=("Arial", 14, "bold"), cursor="hand2")

btn6 = Button(root,text = "6", bg="red", fg="white", width=5, height=2, command=lambda: digit_handler("6"))
btn6.grid(row=4, column=2)
btn6.config(font=("Arial", 14, "bold"), cursor="hand2")

btn_mul = Button(root,text = "*", bg="red", fg="white", width=5, height=2, command=lambda: operator_handler("*"))
btn_mul.grid(row=3, column=3)
btn_mul.config(font=("Arial", 14, "bold"), cursor="hand2")

btn1 = Button(root,text = "1", bg="red", fg="white", width=5, height=2, command=lambda: digit_handler("1"))
btn1.grid(row=5, column=0)
btn1.config(font=("Arial", 14, "bold"), cursor="hand2")

btn2 = Button(root,text = "2", bg="red", fg="white", width=5, height=2, command=lambda: digit_handler("2"))
btn2.grid(row=5, column=1)
btn2.config(font=("Arial", 14, "bold"), cursor="hand2")

btn3 = Button(root,text = "3", bg="red", fg="white", width=5, height=2, command=lambda: digit_handler("3")  )
btn3.grid(row=5, column=2)
btn3.config(font=("Arial", 14, "bold"), cursor="hand2")

btn_sub = Button(root,text = "-", bg="red", fg="white", width=5, height=2, command=lambda: operator_handler("-"))
btn_sub.grid(row=4, column=3)
btn_sub.config(font=("Arial", 14, "bold"), cursor="hand2")

btn0 = Button(root,text = "0", bg="red", fg="white", width=5, height=2, command=lambda: digit_handler("0"))
btn0.grid(row=6, column=0)
btn0.config(font=("Arial", 14, "bold"), cursor="hand2")

btn_dot = Button(root,text = ".", bg="red", fg="white", width=5, height=2, command=lambda: digit_handler("."))
btn_dot.grid(row=6, column=1)
btn_dot.config(font=("Arial", 14, "bold"), cursor="hand2")

btn_equal = Button(root,text = "=", bg="red", fg="white", width=11, height=2, command=lambda: equal_handler("="))
btn_equal.grid(row=6, column=2, columnspan=2) #to make the equal button span across 2 columns.
btn_equal.config(font=("Arial", 14, "bold"), cursor="hand2")

btn_add = Button(root,text = "+", bg="red", fg="white", width=5, height=2, command=lambda: operator_handler("+")       )
btn_add.grid(row=5, column=3)
btn_add.config(font=("Arial", 14, "bold"), cursor="hand2")

btn_clr = Button(root,text = "C", bg="red", fg="white", width=5, height=2, command=lambda: clear_handler("C"))
btn_clr.grid(row=2, column=2)
btn_clr.config(font=("Arial", 14, "bold"), cursor="hand2")

btn_bsp = Button(root,text = "<<<", bg="red", fg="white", width=11, height=2, command=lambda: clear_handler("Bsp"))
btn_bsp.grid(row=2, column=0, columnspan=2) #to make the backspace button span across 2 columns.
btn_bsp.config(font=("Arial", 14, "bold"), cursor="hand2")

root.mainloop()