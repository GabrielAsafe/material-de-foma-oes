#raise quebra o programa se alguma condição é true  

# for i in range(101):
#     if(i % 3== 0):
#         raise Exception(f"The number is mod 3)")
#     if(i % 5== 0):
#         raise Exception(f"The number is mod 5)")
    
#     if(i % 3== 0 and i % 5 == 0) :
#         raise Exception(f"The number is mod 3 and 5)")
    

#assert  quebra o programa também mas só quando ele retorna false

# i = 3

# print(i % 3)

# assert(i % 3== 0),f"The number is mod 3)"

# assert(i % 5== 0),f"The number is mod 5)"

# assert(i % 3== 0 and i % 5 == 0),f"The number is mod 3 and 5)"

# print(i)





for i in range(101):

   
        try:   
            if(i % 3== 0): 
                print(f"The number {i} is mod 3)")

        except:
            if(i % 5== 0):
                
                print(f"The number {i} is mod 5)")
        else:
    
            if(i % 3== 0 and i % 5 == 0) :
                print(f"The number {i} is mod 3 and 5)")
            
        finally:
            print("")