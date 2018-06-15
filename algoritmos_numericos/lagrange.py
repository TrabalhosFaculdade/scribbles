class Lagrange:

    def __init__(self, points):
        self.points = points
    
    def lagrange_k(self, point_k, x):

        numerator = 1
        for k in range (len(self.points)):
            if k != point_k:
                numerator *= x - self.points[k][0]

        denominator = 1
        for k in range (len(self.points)):
            if k != point_k:
                denominator *= self.points[point_k][0] - self.points[k][0]         
        
        return numerator / denominator

    # we could check if is within the interval
    # but right now we are just studying for a test    
    def interpolate_x (self,x):
        result = 0
        for i in range(len(self.points)):
            result += self.points[i][1] * self.lagrange_k(i, x)
        return result

initial_points = [[1,2],[5,0],[7,3]]
lagrange = Lagrange(initial_points)
print(lagrange.interpolate_x (4) )
