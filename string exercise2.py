a="North dakotha"
print(a.rjust(17))
print(a)
print(a.ljust(17,"*"))

c=a.center(16,"+")
print(c)
m=c.rstrip("+")
print(m)

k=a.lstrip("North")
print(k)

fk=a.replace("North","south")
print(fk)