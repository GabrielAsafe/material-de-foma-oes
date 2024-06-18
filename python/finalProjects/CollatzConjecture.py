"""
 Start with a number *n > 1*. Find the number of steps it takes to reach one using the following process: If *n* is even, divide it by 2. If *n* is odd, multiply it by 3 and add 1.

"""

def findN(n, steps):
    
    if n<1:
       
        return "Numero deve ser positivo"
    
    if n == 1:
        return steps
    
    steps = steps +1
    
    if n % 2 == 0:
        n = n/2
        return findN(n, steps)
        

    if n % 2 != 0:
        n = n *3 +1 
        return findN(n, steps)




n = findN(1001,0)

print(n)