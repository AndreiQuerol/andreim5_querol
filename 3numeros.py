from yogi import read

a = read(int)
b = read(int)
c = read(int)
if a>b and a>c:print("Es mes grant el numero ",a)
elif b>a and b>c:print("Es mes grant el numero ",b)
else:print("Es mes grant el numero ",c)
