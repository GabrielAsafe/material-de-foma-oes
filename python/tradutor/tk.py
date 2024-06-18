import tkinter as tk
from tkinter.ttk import *


window = tk.Tk() #cria uma instância da janela

frame1 = tk.Frame(master=window, relief="solid",borderwidth=1)
frame2 = tk.Frame(master=window, relief="solid",borderwidth=1)
frame3 = tk.Frame(master=window, relief="solid",borderwidth=1)

label = Label(master = frame1,text="frame 1") #cria uma label
label.pack()#insere ela na janela 

label2 = Label(master = frame2,text="frame 2") #cria uma label
label2.pack()#insere ela na janela 
label3 = Label(master = frame3,text="frame 3") #cria uma label
label3.pack()#insere ela na janela 

frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)#usa todo o espaço na linha que aquele widget iria ficar. O pack joga onde tiver espaço 

frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# label = Label(text="teste", foreground="black",background="#ffd150", width=10) #cria uma label
# label.pack()#insere ela na janela 

# cria uma entry/text field
# entry = tk.Entry(
#     foreground="black",
#      width=25,
#     background="green",
# )
# entry.insert(0,"me mama")
# entry.delete(0, tk.END)
# entry.pack()

# button = tk.Button(
#     text="button",
#     width=25,
#     background="green",
#     height=10
# )
# button.pack()


# text box
# text_box = tk.Text()
# character = 0 #o charactere começa em 0 mas a linha em 1
# line = 1  
# text_box.get(str(line) + "."+ str(character))
# text_box.get("1.0", tk.END)
# text_box.insert("1.0", "me mama puta")#insiro o texto na primeira linha
# text_box.insert(tk.END, "\nme mama puta")#insiro o texto na última linha
# text_box.pack()




import tkinter as tk

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}






window.mainloop() #faz o display da janela