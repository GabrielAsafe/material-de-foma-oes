import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")

        # Inicializar o jogador atual
        self.current_player = 'X'

        # Criar os botões do jogo
        self.buttons = [[None, None, None] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text='', font=('normal', 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        # Verificar se o botão já foi clicado
        if self.buttons[row][col]['text'] == '':
            # Atualizar o texto do botão com o símbolo do jogador atual
            self.buttons[row][col]['text'] = self.current_player

            # Verificar se há um vencedor
            if self.check_winner(row, col):
                messagebox.showinfo("Tic-Tac-Toe", f"Jogador {self.current_player} venceu!")
                self.reset_game()
            else:
                # Alternar para o próximo jogador
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self, row, col):
        # Verificar a linha
        if all(self.buttons[row][i]['text'] == self.current_player for i in range(3)):
            return True

        # Verificar a coluna
        if all(self.buttons[i][col]['text'] == self.current_player for i in range(3)):
            return True

        # Verificar diagonais
        if all(self.buttons[i][i]['text'] == self.current_player for i in range(3)) or \
           all(self.buttons[i][2-i]['text'] == self.current_player for i in range(3)):
            return True

        return False

    def reset_game(self):
        # Limpar os textos dos botões
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ''

        # Reiniciar o jogador atual
        self.current_player = 'X'

    def run(self):
        self.root.mainloop()

# Instanciar e executar o jogo
game = TicTacToe()
game.run()
