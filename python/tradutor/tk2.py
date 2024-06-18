import tkinter as tk
from tkinter.ttk import *



# quando se associa um widget a um frame usando o master, ao posicionarmos o frame, tudo dentro dele fica sujeito a posição inicial, mas
# quando posicionamos outro widget fora do frame e definimos o grid para fora daquela posição, ele fica fora da borda do frame



# window = tk.Tk()

# window.columnconfigure([0,1,2],weight=1,minsize=50)#index,resizing,minsize
# window.rowconfigure([0,1,2],weight=1,minsize=50)#index,height,minsize


# frame = tk.Frame(master=window, relief="solid",borderwidth=1, background="yellow")


# frame.grid(row=0,column=0)




# label = tk.Label(master=frame,text="a",background="green")
# labe2 = tk.Label(master=frame,text="a",background="blue")
# labe3 = tk.Label(master=frame,text="a")

# labe4 = tk.Label(text="a")


# label.grid(row=0,column=0,sticky="nswe")
# labe2.grid(row=1,column=1,sticky="nswe")
# labe3.grid(row=2,column=2,sticky="nswe")

# labe4.grid(row=1,column=1)

# window.mainloop()





##interactions

# import tkinter as tk

# inputs = []


# window = tk.Tk()

# def handle_keypress(event):
#     """Print the character associated to the key pressed"""
#     print(event.char)
#     inputs.append(event.char)

# # Bind keypress event to handle_keypress()
# window.bind("<Key>", handle_keypress)

# window.mainloop()


# print(inputs)



####input hadling

# def getText():
#     labelText = label["text"]
#     label["text"] = "0"

# def increase():
#     value = int(label["text"])
#     label["text"] = f"{value + 1}"


# def decrease():
#     value = int(label["text"])
#     label["text"] = f"{value - 1}"



# window = tk.Tk()

# window.rowconfigure(0, minsize=50, weight=1)
# window.columnconfigure([0,1,2], minsize=50, weight=1)

# btnDecrease = tk.Button(master=window, text="-",relief="solid",command=decrease)
# btnDecrease.grid(row=0,column=0,sticky="nwes")

# label = tk.Label(master=window, text="0")
# label.grid(row=0,column=1)

# btnIncrease = tk.Button(master=window, text="+",relief="solid", command=increase)
# btnIncrease.grid(row=0,column=2,sticky="nwes")

# getText()

# window.mainloop()



import random

def roll():
    r1 = random.randint(1, 6)

    text["text"] = f"{r1}"


window = tk.Tk()

but = tk.Button(master=window,text="Random",command=roll)

text = tk.Label(master=window,text="0")

text.pack()
but.pack()

window.mainloop()