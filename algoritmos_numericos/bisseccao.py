from math import fabs
from math import e

class Bissec:

    def __init__(self, function, a, b, error):

        self.a = a
        self.b = b
                   
        self.error = fabs(error)
        self.function = function     

        self.f_a = function(a)
        self.f_b = function(b)

    def calculate_root(self):
        
        i = 0
        limit = 20 # max number of iterations
    
        while i < limit:

            print("a:", self.a, ", f(a):", self.f_a)
            print("b:", self.b, ", f(b):", self.f_b)

            if self.check_value(self.f_a):
                return self.a

            if self.check_value(self.f_b):
                return self.b

            p = ( self.a + self.b ) / 2
            f_p = self.function(p)
            
            if f_p * self.f_a < 0:
                # root between a and p 
                self.b = p
                self.f_b = f_p
            
            else:
                # root between b and p 
                self.a = p
                self.f_a = f_p
                        
            i += 1        
        
        print("Did not get there")        

    def check_value (self, value):
        return fabs(value) <= self.error

def bissec (function, a, b, error):

    while True:
        
        # halfway point
        p = ( a + b ) / 2
        
        f_a = function(a)
        f_b = function(b)
        f_p = function(p)
        
        print(p)

        if(fabs(f_p) <= error):
            # found a good enough result
            return p
        else:
            if(f_p * f_a < 0):
                               
                b = p
            else:
                # root between b and p
                a = p

def example (x):
    return x ** 3 + 4 * x ** 2 - 10
           
def ex_a (x):
    return x - 2 ** -x

def ex_b(x):
    return e ** x ** 2 + 3 * x - 2


bissec = Bissec(ex_b,0,1,0.1)
print(bissec.calculate_root())

