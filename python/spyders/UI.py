from enum import Enum
import os
import random
import numpy as np

class Naipe(Enum):
    COPAS = 'Copas'
    OUROS = 'Ouros'
    PAUS = 'Paus'
    ESPADAS = 'Espadas'

class Valor(Enum):
    AS = 'A'
    DOIS = '2'
    TRES = '3'
    QUATRO = '4'
    CINCO = '5'
    SEIS = '6'
    SETE = '7'
    OITO = '8'
    NOVE = '9'
    DEZ = '10'
    VALETE = 'Valete'
    DAMA = 'Dama'
    REI = 'Rei'

class Carta:
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe

    def __str__(self):
        return f"{self.valor.value} de {self.naipe.value}"
    

class JogoPacienciaSpider:
    def __init__(self):
        self.baralho1 = [Carta(valor, naipe) for valor in Valor for naipe in Naipe] # cria uma carta de cada nipe para o primeiro baralho
        self.baralho2 = [Carta(valor, naipe) for valor in Valor for naipe in Naipe] # cria uma carta de cada nipe para o segundo baralho
        random.shuffle(self.baralho1) # embaralha as cartas 
        random.shuffle(self.baralho2) # embaralha as cartas 
        self.fullBaralho = self.baralho1 + self.baralho2 #concatena os dois baralhos embaralhados
        self.primeiraMetade = self.fullBaralho[:54]
        self.reservas = self.fullBaralho[54:] #diz que as últimas 50 cartas vão para reserva
        self.colunas = [] # define uma lista de colunas 10 no total
        self.minha_lista = [
            ['x9', 'x9', 'x9', 'x9', 'x9', 'x9', 'x9', 'x9', 'x9', 'x9'],
            ['x0', 'x0', 'x0', 'x0', 'x0', 'x0', 'x0', 'x0', 'x0', 'x0'],
            ['x0', 'x0', 'x0', 'x0', 'x0', 'x0', 'x0', 'x0', 'x0', 'x0'],
            ['x0', 'x0', 'x0', 'x0', 'x0', 'x0', 'x0', 'x0', 'x0', 'x0'],
            ['x0', 'x0', 'x0', 'x0', 'x0', 'x0', 'x0', 'x0', 'x0', 'x0'],
            ['x5', 'x5', 'x5', 'x5', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx'],
        ]

    def preencherBaralho(self):
        """preenche nas 10 colunas as primeiras 5 cartas"""
        for _ in range(10):
            self.coluna = []
            for j in range(5):
                self.coluna.append(self.primeiraMetade[0])
                self.primeiraMetade.pop(0)
            self.colunas.append(self.coluna)

        """preenche nas primeiras 4 colunas as 4 cartas que faltam no total, sendo uma em cada coluna"""
        for i in range(0,4):
            self.colunas[i].append(self.primeiraMetade[i])


    def pegarCartaTopo(self):


        for i in range(0,len(self.minha_lista)): #quantidade de linhas 
            for j in range(10): # em cada linha itera sobre as colunas
                if (self.minha_lista[i][j]== 'xx'):
                     self.minha_lista[i-1][j] = 'x5' #tudo que estiver em baixo de -- é visível
                


        


    
    def adicionar_carta(self):
        # for i in range(10):
        #     self.colunas[i].append(self.reservas[0])
        #     self.reservas.pop(0)


        
        self.minha_lista.append( ['x5', 'x5', 'x5', 'x5', 'x5', 'x5', 'x5', 'x5', 'x5', 'x5'])

        

        for i in range(0,len(self.minha_lista)): #quantidade de linhas
            for j in range(10): # em cada linha itera sobre as colunas
                if (self.minha_lista[i][j] == "xx"):
                        if(i+1 ==len(self.minha_lista) ):
                            continue
                        self.minha_lista[i+1][j] = "xx"
                        self.minha_lista[i][j] = "x5" #tudo que estiver em baixo de -- é visível

                        

                


        return self.reservas.__len__()

    def __len__(self):
        return self.reserva.__len__()

    def limparTela(self):
        os.system('cls')

    def screen(self):
        matriz_numpy = np.array(self.minha_lista, dtype=str)
        #self.limparTela()
        print(matriz_numpy)


    def moverValores(self):
        # print("xy xy xy")
        # print("00 01 02")
        # print("10 11 12")


        x=input("Insira a posiçao x ")
        y=input("Insira a posiçao y ")

        x1=input("Insira a posiçao x1 ")
        y1=input("Insira a posiçao y1 ")


        aux = self.colunas[int(x)][int(y)]
        self.minha_lista[int(x)][int(y)] = self.minha_lista[int(x1)][int(y1)]
        self.minha_lista[int(x1)][int(y1)] = aux





def main():

    jogo_spider = JogoPacienciaSpider()
    jogo_spider.preencherBaralho()

    jogo_spider.pegarCartaTopo()
    while(True):

        jogo_spider.screen()

        acao= input("introuza ação")
        if acao == "m":
            jogo_spider.moverValores()

        elif acao == "a":
            jogo_spider.adicionar_carta()





if __name__ == "__main__":

    main()