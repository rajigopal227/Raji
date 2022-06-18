class studentmark:
    def marklist(self):
        self.t=int(input("enter tamil mark:"))
        self.e=int(input("enter english mark:"))
        self.m=int(input("enter maths mark:"))
        self.sc=int(input("enter science mark:"))
        self.s=int(input("enter social mark:"))
    def print(self):
        self.tot=self.t+self.e+self.m+self.sc+self.s
        self.avg=self.tot/5
    def display(self):
        print("enter total no of marks:",self.tot)
        print("enter average mark:",self.avg)
        if self.avg>80:
            print("grade A")
        elif self.avg>60:
            print("grade B")
        elif self.avg>40:
            print("grade C")
        else:
            print("grade D")
s=studentmark()
s.marklist()
s.print()
s.display()
