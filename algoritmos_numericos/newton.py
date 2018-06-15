from math import fabs

class Newton:

    def __init__(self, function, derivative, initial_x, error):
        self.function = function
        self.derivative = derivative
        self.x = initial_x
        self.error = fabs(error)
        
    def calculate_root(self):
        
        while True:
            
            f_x = self.function(self.x)
            d_x = self.derivative(self.x)  
            
            print("============================================")
            print("Current x:", self.x)
            print("Current f(x):", f_x)
            print("Current f'(x):", d_x)            

            self.x = self.x - ( f_x / d_x )
     
            if(fabs(f_x) < self.error):
                return self.x

        return self.x

def f_example_1(x):
    return x ** 3 + 4 * x ** 2 - 10

def d_example_1(x):
    return 3 * x ** 2 + 8 * x 

def f_example_2(x):
    return ( x - 1 ) ** 2

def d_example_2(x):
    return 2 * ( x - 1 ) 


newton = Newton(f_example_2, d_example_2, 2, 0.000000001)
print(newton.calculate_root())
