for multiplicador in range(1,11):
    dif = 10 - multiplicador
    base = multiplicador
    ValorDecimal=0
    x = 0
    print("\n")
    for multiplicando in range(1,11):
        if(multiplicando == 1):
            print(f"{multiplicador} X {multiplicando} = {ValorDecimal}{multiplicador} padrão")
            x = multiplicador
            continue
        if(x - dif > 0):
             if(multiplicador % 10 == 0):
                x+=1
                print(f"{multiplicador} X {multiplicando} = {x+1}{0} x")
                continue
             
             x -= dif
             ValorDecimal +=1
             print(f"{multiplicador} X {multiplicando} = {ValorDecimal}{x} > 0") 
             continue           

        if(x - dif < 0):
            x += multiplicador
            print(f"{multiplicador} X {multiplicando} = {ValorDecimal}{x} <0")
            continue
        if(x -dif == 0):
            ValorDecimal = ValorDecimal+1
            x = 0
            print(f"{base} X {multiplicando} = {ValorDecimal}{x} ==0 ")
        
        
 
