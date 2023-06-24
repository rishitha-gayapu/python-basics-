#even or odd
#class=number,function with in
#called check and output with boolean which has to be apprehended with a sconsideratiom
#another fn to print even or odd
class number:
    even=0
    def check(self,num):
        if num%2==0:
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
n=number()
n.even_odd(99)
