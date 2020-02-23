class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

    def initialize():
        points = [] 
        points.append(Point(1, 3)) 
        points.append(Point(2, 2)) 
        points.append(Point(1, 1)) 
        points.append(Point(2, 1)) 
        points.append(Point(3, 0)) 
        points.append(Point(0, 0)) 
        points.append(Point(3, 3)) 
        points.append(Point(3, 2))
        points.append(Point(5, 5))
        points.append(Point(0, 5))
        # points.append(Point(0,0))
        # points.append(Point(1,1))
        # points.append(Point(2,1))
        # points.append(Point(1,2))
        # points.append(Point(3,3))
        print("Graph Initialized")
        return points
    
class Equations:
    def straightLineThroughTwoPoints(points, i):

        n = 1
        for each in points:
            try:
                x1 = points[i].x
                y1 = points[i].y
                x2 = points[n].x
                y2 = points[n].y
                # print("Point 1: " + str(x1) + "," + str(y1))
                # print("Point 2: " + str(x2) + "," + str(y2))
                print()

                a = y2- y1 
                b = x1 - x2 
                c = (x1*y2) - (y1*x2) 
                # print("A: " + str(a))
                # print("B: " + str(b))
                # print("C: " + str(c))
                Equations.findSigns(a, b, c, points, i, n)
                n = n + 1
            except:
                # print("All combinations tested for point: " + str(x1) + "," + str(y1) )
                # print("n: " + str(n))
                # print("i: " + str(i))
                n = n + 1
        

    def findSigns(a, b, c, points, i, n):
        signArray = []
        for point in points:
            
            # print("Checking " + str(point.x) + "," + str(point.y))
            if((a*point.x + b*point.y - c) > 0): #determine sign of point we are checking
                signArray.append(1)
                # print("positive")
            elif((a*point.x + b*point.y - c) < 0):
                signArray.append(-1)
                # print("negative")
                
        Equations.determineIfEdge(signArray, points, i, n)
        print("i is: " + i)
        print("n is: " + n)
        
    def determineIfEdge(signArray, points, i, n):
        isAnEdge = True
        x1 = points[i].x
        y1 = points[i].y
        x2 = points[n].x
        y2 = points[n].y
        print("Point 1: " + str(x1) + "," + str(y1))
        print("Point 2: " + str(x2) + "," + str(y2))
        print(signArray)
        compareTo = signArray[0]
        for each in signArray:
            
            if(each != compareTo):
                isAnEdge = False
                break
        if(isAnEdge == True):
            hull.append("There is an edge between " + str(x1) + "," + str(y1) + " and " + str(x2) + "," + str(y2))


            ###### Need to iterate through all the indecies now, and make sure that every possible combination of edge was tested, not 
            # just indecies next to each other, which is what is happening now with testing i, i+1





            
            
    

#Driver code

hull = []
points = Point.initialize()
for i in range(10):   
    Equations.straightLineThroughTwoPoints(points, i)

# y1 = points[index].y
# x1 = points[index].x

# print("For the point " + str(x1) + "," + str(y1))
print(hull)
