t = [1,23,4,5,6,7,8]
r = []
n= 3
for i in range(n):
    r.append(t[i])
print(r)

t[0:n]
prj = [i for i in t[0:n]]
print(prj)
print( t[0:n])