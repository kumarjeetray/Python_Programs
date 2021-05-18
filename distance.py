'''
Finds the distance between 2 points
'''
x1,y1=eval(input("Enter two co-ordinates with , in between:"))
x2,y2=eval(input("Enter two co-ordinates with , in between:"))
dist=(((x2-x1)**2) + ((y2-y1)**2))**0.5
print("Distance=",dist)
