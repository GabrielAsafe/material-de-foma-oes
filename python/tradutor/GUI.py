import tkinter as tk

import map,tradutor


dict = map.inicializar('palavras.txt')


palavras = []#vetor de palavras escritas

def handle_keypress(event):
    palavras = txt.get("1.0", tk.END).split()#pega todo da primeira linha até o fim do texto e da split com base nos espaços
    match = map.verifica_palavras_corretas(palavras[-1],dict)
    if(match != None):
        correctText.insert(tk.END, "\n"+str(match))

    translatedText.delete("1.0", tk.END)
    translatedText.insert(tk.END, tradutor.translate(str(txt.get("1.0", tk.END))))
    


    

#window configuration
window = tk.Tk()
window.title("Simple Text Editor")
window.rowconfigure(0, minsize=40, weight=1)
window.columnconfigure([0,1,2], minsize=40, weight=1)

#define widgets
correctText = tk.Text(master=window)
translatedText = tk.Text(master=window)
txt = tk.Text(master=window)
#frame = tk.Frame(master=window, relief=tk.RAISED, bd=2)
#btn_open = tk.Button(master=frame, text="Open")
#btn_save = tk.Button(master=frame, text="Save As...")


#desenhar os grids
#btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
#btn_save.grid(row=1, column=0, sticky="ew", padx=5)
#frame.grid(column=0, row=0,sticky="nswe")
txt.grid(row=0, column=0, sticky="nsew")
correctText.grid(row=0, column=1, sticky="nsew")
translatedText.grid(row=0, column=2, sticky="nsew")

#bind
window.bind("<space>", handle_keypress)

window.mainloop()