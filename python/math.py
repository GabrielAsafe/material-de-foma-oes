#    multiplicador X multiplicando      multiplicando == 1; x = multiplicador
#    1 X 1 = 1    
#    1X2 = 
#
#
#



for multiplicador in range(1,11):

    dif = 10 - multiplicador# 1-9, 2-8, 3-7...
    base = multiplicador
    zero=0
    x = 0
    
    print("\n")
    for multiplicando in range(1,11):


        if(multiplicando == 1):
            #print(f"A diferença é {dif}")
            print(f"{multiplicador} X {multiplicando} = {multiplicador} padrão")
            x = multiplicador
            continue


        # 1 - 9 < 0; x = multiplicador + x
        if(x - dif <0):
            x+=multiplicador

            print(f"{base} X {multiplicando} = {zero}{x} <0 ")
            continue



        if(x - dif >0):
            if(x + dif >= 10 or x +x+x+x+x >= 10):
                zero = zero+1

            x = x-dif
            print(f"{base} X {multiplicando} = {zero}{x} >0 ")
            continue


        if(x -dif == 0):
            zero = zero+1
            x = 0
            print(f"{base} X {multiplicando} = {zero}{x} ==0 ")
