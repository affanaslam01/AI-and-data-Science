#Write a function to compute the area and circumference of the circle and return the computed results.
def function(r):
    area=3.14*r**2
    circumference=2*3.14*r
    return area,circumference

area,circumference=function(4)
print("Area of circle:",area)
print("Circumference of circle:",circumference)
