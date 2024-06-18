import random


def main(contador,rando,listaDevalores):
    valor = int(input("Escolha um valor entre 0 e 100\n"))
    diference = rando-valor
    listaDevalores.insert(0,diference)
    
    contador+=1
    
    
    if(int(valor) <0 or int(valor) > 100):
        print("aprende a ler, filho da puta\n")
    else:
        if(contador == 1):
            if(diference <10 and diference > 0):
                print("quente")
            elif(diference >10 and diference < 100):
                print("frio")
            
        
        elif(diference == 0):
                print(f"Parabéns meu puto. só demorou {contador} tentativas")
                contador = -1
                

        else:
            lastDifference = listaDevalores[1]
            if( diference > lastDifference):
                print("mais frio")
            elif(diference < lastDifference):
                print("mais quente")
    
    return contador
    
    
if __name__ == "__main__":
    contador = 0
    rando = random.randint(0,100)
    listaDevalores = [0]
    print(rando)
    while(True):
        contador = main(contador,rando, listaDevalores)
        if(contador == -1):
            break
       