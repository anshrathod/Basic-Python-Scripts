import cmath

print("For ax^2 + bx + c")

a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
#Calculating Discriminant
d = (b**2) - (4*a*c)  
  
# find two solutions  
sol1 = (-b-cmath.sqrt(d))/(2*a)  
sol2 = (-b+cmath.sqrt(d))/(2*a)  

print('Solutions\n{0} and \n{1}'.format(sol1,sol2))
