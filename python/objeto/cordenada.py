class Line:
    def __init__(self,c1, c2):
        self.c1 = c1
        self.c2 = c2

    def distance(self):
        y = self.c2[1]-self.c1[1]
        x = self.c2[0]-self.c1[0]
        print(y/x) 





d1 = (3,5)
d2=(9,7)

linha = Line(d1,d2)

linha.distance()

