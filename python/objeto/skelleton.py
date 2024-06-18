class Character:
    def __init__(self,nome, classe) -> None:
        self.nome = nome
        self.classe = classe

    def __str__(self) -> str:
        return f"meu nome é {self.nome} e sou um {self.classe}"

    def __del__(self):
        print(f"{self.nome} foi de arrasta pra cima")


class Mago:
     hp = 10
     mana = 30
     defesa = 5
     defesa_magica = 12

class Cavaleiro:
     hp = 18
     mana = 3
     defesa = 15
     defesa_magica = 6


player = Character("marcelo",Mago)



print(player.nome)
print(player.classe.defesa)

del player



