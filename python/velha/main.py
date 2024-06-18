import tkinter as tk
import numpy as np

preenchidos = [[0,0,0],[0,0,0],[0,0,0]]
contador = 0


def verificarPreencimento(row, col):
    print(preenchidos)
    matches =0

    obj = preenchidos[row][col]

    for i in range(3):
        if preenchidos[row][i] == obj:
            matches +=1
    if (matches == 3):
        print("row completa")
        root.destroy()
    matches =0

    for i in range(3):
        if preenchidos[i][col] == obj:
            matches +=1
    if (matches == 3):
        print("col completa")
        root.destroy()
    matches =0

    for item in np.diagonal(preenchidos):
        if(item == "y"):
            matches+=1
        elif(item == "x"):
            matches-=1

        if (matches == abs(3)):
            print("diagonal1 completa")
            root.destroy()
   
    matches = 0
    for item in np.diagonal(np.fliplr(preenchidos)):
        if(item == "x"):
            matches+=1
        elif(item == "y"):
            matches-=1

        if (matches == abs(3)):
            print("diagonal1 completa")
            root.destroy()
   
def on_button_click(row, col):
    global contador
   

    if(preenchidos[row][col] ==0 ):
        contador+=1

        if contador%2 == 0:
            preenchidos[row][col] = "x"
            button_text = f"X"
            buttons[row][col].configure(text=button_text)
        else:
            preenchidos[row][col] = "y"
            button_text = f"Y"
            buttons[row][col].configure(text=button_text)

        verificarPreencimento(row,col)
    

def create_grid(rows, columns):
    for row in range(rows):
        root.grid_rowconfigure(row, weight=1)
        for col in range(columns):
            root.grid_columnconfigure(col, weight=1)
            button = tk.Button(root, text=f"Button {row}-{col}", command=lambda r=row, c=col: on_button_click(r, c))##não é meu código
            button.grid(row=row, column=col, sticky="nsew")
            buttons[row][col] = button##não é meu código

# Create the main window
root = tk.Tk()
root.title("Resizable Clickable Button Grid")

# Set the number of rows and columns in the grid
num_rows = 3
num_columns = 3

# Initialize the 2D list to store button references
buttons = [[None for _ in range(num_columns)] for _ in range(num_rows)]##não é meu código


# Create the resizable grid of buttons
create_grid(num_rows, num_columns)




# Start the Tkinter event loop
root.mainloop()


