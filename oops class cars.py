class car():
    def __init__(self,modelname,year):
        self.modelname=modelname
        self.year=year
    def display(self):
        print(self.modelname,self.year)

c1=car("audi",2020)
c2=car("benz",2040)
c1.display()
c2.display()
