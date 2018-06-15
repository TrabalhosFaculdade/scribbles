class Plot:

  def __init__(self, points):
  
    #initializing values
    self.points = points
    self.m = len(points)
    
    #to be incremented using calculate_sums()
    self.sum_square_x = 0
    self.sum_y = 0
    self.sum_x_y = 0
    self.sum_x = 0
    
    #incremeting sums
    #used more than once, hence the way this class is organized
    self.calculate_sums()
    self.calculate_a0()
    self.calculate_a1()
  

  def calculate_sums(self):
    """
      incrementing values to be used to calculate a0 and a1
      in this case, they are all done once for every point passed to the constructor
    """
    for point in self.points:
      self.sum_square_x += point[0] ** 2
      self.sum_y += point[1]
      self.sum_x_y += point[0] * point[1]
      self.sum_x += point[0]

  def calculate_a0(self):
    self.a0 = (self.sum_square_x * self.sum_y - self.sum_x_y * self.sum_x) / (self.m * self.sum_square_x - self.sum_x ** 2)

  def calculate_a1(self):
    self.a1 = (self.m * self.sum_x_y - self.sum_x * self.sum_y) / (self.m * self.sum_square_x - self.sum_x ** 2)

  def express_function(self):
    """
    returns a string with the function of our "curve" to represent approximately our points
    in this case, it will be a straight line
    """
    function = "P(x) = {} * x + {}"
    return function.format(self.a1,self.a0)
   
  def calculate_x(self,x):
    """
    with a given x, calculates its equivalent y given the calcualted equation
    """
    return self.a1 * x + self.a0
  

print("\n================= Primeiro exemplo aula ================")
input_class = [[0,1],
                [0.25,1.2],
                [0.5,1.6],
                [0.75,2.1],
                [1,2.7]]
                
example_class = Plot(input_class)
print("Sum of all x's squared:", example_class.sum_square_x)
print("Sum of all y's:        ", example_class.sum_y)
print("Sum of all x * y:      ", example_class.sum_x_y)
print("Sum of all x's:        ", example_class.sum_x)
print("Resulting function:    ", example_class.express_function())
print("A0:", example_class.a0)
print("A1:", example_class.a1)
print(example_class.calculate_x(2))

print("=======================================================")

print("\n================= Primeiro exercício ==================")
initial_input = [[1,1.84],
                [1.1,1.96],
                [1.3,2.21],
                [1.5,2.45],
                [1.9,2.94],
                [2.1,3.18]]
                
first = Plot(initial_input)
print("Sum of all x's squared:", first.sum_square_x)
print("Sum of all y's:        ", first.sum_y)
print("Sum of all x * y:      ", first.sum_x_y)
print("Sum of all x's:        ", first.sum_x)
print("Resulting function:    ", first.express_function())
print("A0:", first.a0)
print("A1:", first.a1)
print(first.calculate_x(2))

print("=======================================================")

print("\n================= Segundo exercício ===================")
initial_input = [[4,102.56],
                 [4.2,113.18],
                 [4.5,130.11],
                 [4.7,142.05],
                 [5.1,167.53],
                 [5.5,195.14],
                 [5.9,224.87],
                 [6.3,256.73],
                 [6.8,299.50],
                 [7.1,326.72]]
                
first = Plot(initial_input)
print("Sum of all x's squared:", first.sum_square_x)
print("Sum of all y's:        ", first.sum_y)
print("Sum of all x * y:      ", first.sum_x_y)
print("Sum of all x's:        ", first.sum_x)
print("Resulting function:    ", first.express_function())
print("A0:", first.a0)
print("A1:", first.a1)
print(first.calculate_x(2))

print("=======================================================")

# ==========================================================

print("\n=================Example from the book=================")
initial_input_book = [[1,1.3],
                      [2,3.5],
                      [3,4.2],
                      [4,5],
                      [5,7],
                      [6,8.8],
                      [7,10.1],
                      [8,12.5],
                      [9,13],
                      [10,15.6]]

calculate2 = Plot(initial_input_book)
print("Sum of all x's squared:", calculate2.sum_square_x)
print("Sum of all y's:        ", calculate2.sum_y)
print("Sum of all x * y:      ", calculate2.sum_x_y)
print("Sum of all x's:        ", calculate2.sum_x)
print("Resulting function:    ",calculate2.express_function())
print("A0:", calculate2.a0)
print("A1:", calculate2.a1)
print(calculate2.calculate_x(2))
print("=======================================================")

