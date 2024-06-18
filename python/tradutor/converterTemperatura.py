import tkinter as tk
from tkinter.ttk import *


def converter():
    output.insert(0,int(entry.get())*(9/5) + 32)




window = tk.Tk()
window.rowconfigure([0,1,2],minsize=50,weight=1)
window.columnconfigure([0,1,2],minsize=50,weight=1)





entry = tk.Entry(
    
    foreground="black",
     width=100
)



button = tk.Button(
    text="converter",
    command=converter,
    width=30
)


labelF = tk.Label(
    text="Temperatura em Fº"
)

labelC = tk.Label(
    text="Temperatura em Cº"
)


output = tk.Entry(
    foreground="black",
     width=30
)

entry.grid(column=1,row=1)
button.grid(column=0,row=1)
labelC.grid(column=1,row=0)
labelF.grid(column=2,row=0)
output.grid(column=2,row=1)
window.mainloop()
