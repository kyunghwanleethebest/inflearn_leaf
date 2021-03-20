# Method Overriding, Method Overloading

# Method Overriding
class Parent():
    def __init__(self):
        self.value = 20

    def get_value(self):
        return self.value

    def sayhi(self, who):
        saying = f'HI Hello {who}'
        print(saying)

class Child(Parent):
    def get_value(self):
        return self.value * 15

    def sotired(self, msg):
        say = f'LKH {msg}'
        super().sayhi(say)

a = Parent()
b = Child()

b.sotired('I want to go bed')



# Method Overloading
from multipledispatch import dispatch

class Suprise():
    
    @dispatch(int,int) 
    def product(a, b): 
        return a+b 

    @dispatch(int,int,int) 
    def product(a, b, c): 
        return a+b+c

    @dispatch(float,float,float) 
    def product(a, b, c): 
        return a+b+c
        
c = Suprise()


print('정수 2개 더하기 ', c.product(1, 2))
print('정수 3개 더하기', c.product(3, 4, 5))
print('실수 3개 더하기', c.product(3.4, 4.4, 5.2))