import random
from tkinter import *
# user_data = {
#     "first_name": input("Enter your first name: "),
#     "last_name": input("Enter your last name: "),
#     "num_length": int(input("How many digit you want in your password: "))
# }
user_data = {
    "first_name": "First",
    "last_name": "Last",
    "num_length": 3
}
# user_data = {
#     "first_name": "First",
#     "last_name": "Last",
#     "num_length": 3
# }

keys = list(user_data.keys())
symbol = ["@", "$", "#", "%", "&"]
number= [1, 2, 3, 4, 5, 6, 7, 8, 9]

def num_genrator(number=number):
    num = ""
    for i in range(user_data["num_length"]):
        num = num + str(random.choice(number))
    return num

def symbol_genrator(symbol=symbol):
    sym = random.choice(symbol)
    return sym

def name_generator(user_data=user_data):
    y = random.randint(0,1)
    if y == 0:
        name = str(user_data[keys[y]]) + str(user_data[keys[1]])
    else:
        name = str(user_data[keys[y]]) + str(user_data[keys[0]])
    return name

def combine_genrator():
    global user_data
    if first_name_entry.get() != "":
        user_data["first_name"] = first_name_entry.get()
    else:
        user_data["first_name"] = "First"
        
    if last_name_entry.get() != "":
        user_data["last_name"] = last_name_entry.get()
    else:
        user_data["last_name"] = "Last"

    pass_word = ""
    digit = [1,2,3]
    for k in range(3):
        z = random.choice(digit)
        if z == 1:
            digit.remove(1)
            pass_word = pass_word + name_generator()
        elif z == 2:
            digit.remove(2)
            pass_word = pass_word + symbol_genrator()
        else:
            digit.remove(3)
            pass_word = pass_word + num_genrator()
        
    return password_label.config(text=pass_word)

root = Tk()
root.title("Password Generator")
root.geometry("400x320")
root.resizable(0, 0)
root.config(bg="#C2F8B6")

frame = Frame(root, bg="#F6F6F6",width=80,borderwidth=5, relief=RAISED)
title_label = Label(frame, text="   Password Generator  ", relief=RAISED, fg="white", bg="#014E1E")
title_label.pack(fill=X,expand=True)
title_label.config(font=("Arial", 20, "bold"))

frame1 = Frame(root, bg="lightblue")
first_name_label = Label(frame1, text="First Name:", bg="lightblue")
first_name_label.grid(row=0, column=0, padx=10, pady=10)
first_name_label.config(font=("Arial", 14, "bold"))
first_name_entry = Entry(frame1,width=33)
first_name_entry.grid(row=0, column=1, padx=10, pady=10)


last_name_label = Label(frame1, text="Last Name:", bg="lightblue")
last_name_label.grid(row=1, column=0, padx=10, pady=10)
last_name_label.config(font=("Arial", 14, "bold"))
last_name_entry = Entry(frame1,width=33)
last_name_entry.grid(row=1, column=1, padx=10, pady=10)

frame2 = Frame(root)
generate_button = Button(frame2, text="Generate Password", command=combine_genrator)
generate_button.pack()
generate_button.config(font=("Arial", 14, "bold"), bg="#AB4506", fg="white", relief=RAISED, borderwidth=3)

frame3 = Frame(root, bg="lightblue")
password_label = Button(frame3, text=".....", bg="lightblue", fg="red",command=lambda: root.clipboard_clear() or root.clipboard_append(password_label.cget("text")))
password_label.grid(row=0, column=2,columnspan=2)
password_label.config(font=("Arial", 16, "bold"),width=25, relief=RAISED, borderwidth=3)

frame.pack(pady=10)
frame1.pack(pady=20)
frame2.pack()
frame3.pack(pady=10)


root.mainloop()