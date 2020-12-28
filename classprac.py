import pickle
class Person: # first pararmeter of every class object has to be self
    def __init__(self,name,age,pay=0,job=None):
        self.name=name
        self.age=age
        self.pay=pay
        self.job=job
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay=self.pay*(1.0+percent)
    def __str__(self):
        return ('<%s=>name=%s,pay=%s,age=%s>'%(self.__class__.__name__,self.name,self.pay,self.age))
class Manager(Person):
    def __init__(self,name,age,pay):
        super().__init__(name,age,pay,'Manager') # or Person.__init__(self,name,age,pay,'Manager')
    def giveRaise(self,percent,bonus):
        Person.giveRaise(self,percent+bonus)

p=Manager(name='Abdul Basit',age=2,pay=200)
p.giveRaise(2,2)
q=Person('Zubaida',45)
#print(p)
#print(q)
#file=open('Hello','ab')
'''with open('hello','ab') as file:
    for obj in (p,q):
        pickle.dump(obj,file)
'''
with open('hello','rb') as file:
    while True:
        try:
            fp=pickle.load(file)
            print(fp)
        except:
            break
#if __name__=='__main__':
    #p1=Person('Bob Marley',42,30000,'swe')
    #print(p1.lastName())