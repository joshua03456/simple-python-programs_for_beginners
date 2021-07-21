a =int(input("ENTER THE VALUE"))
b =int(input("ENTER THE VALUE"))
c =int(input("ENTER THE VALUE"))


# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is',area)
