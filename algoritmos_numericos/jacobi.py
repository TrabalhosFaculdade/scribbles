class Jacobi:
   
    def __init__(self, initial_params, functions):
          
        if len(initial_params) != len(functions):
            raise ValueError("How am i supposed to deal with this?")
        
        self.functions = functions
        
        self.n = 0        
        self.iterations = []
        self.iterations.append(initial_params)
        
    def solve_next_iteration(self):
        
        current_iteration = []
        for function in self.functions:
            current_iteration.append(function(self.iterations[self.n]))
        
        self.iterations.append(current_iteration)
        self.n += 1

    def is_done_yet(self):
        # TODO replace this with some kind of stopping condition
        return self.n > 45 # let's repeat this 200x, just for testing purposes

    def solve_system(self):

        while(not self.is_done_yet()):
            self.solve_next_iteration()

    def print_result(self):
        for line in self.iterations:
            print(line)
        

# we will be solving for xn already
def fun_x1 (params):
    x2 = params[1]
    x3 = params[2]
    x4 = params[3]
    return (x2 - 2 * x3 + 6)/10

def fun_x2 (params):
    x1 = params[0]
    x3 = params[2]
    x4 = params[3]
    return (x1 + x3 - 3 * x4 + 25) / 11

def fun_x3 (params):
    x1 = params[0]
    x2 = params[1]
    x4 = params[3]
    return (-2 * x1 + x2 + x4 - 11) / 10

def fun_x4 (params):
    x1 = params[0]
    x2 = params[1]
    x3 = params[2]
    return (-3 * x2 + x3 + 15) / 8


problem_functions = [fun_x1,fun_x2,fun_x3,fun_x4]
initial_params   = [0,0,0,0]

jacobi = Jacobi(initial_params, problem_functions)
jacobi.solve_system()
jacobi.print_result()
