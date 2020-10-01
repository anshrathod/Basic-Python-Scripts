import sys

p = int(sys.argv[1])
r = int(sys.argv[2])
y = int(sys.argv[3])

cmpi = p * (pow((1 + r / 100), y))
print("Compound Interest = ",
      cmpi);
