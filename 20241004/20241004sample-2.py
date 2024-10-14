s = ['a','b','c','d','e','f','g']
print (s[0])
s[0] = 'X'
print (s)
print (s[2:5])
s[2:5] = ['C','D','E']
print (s)
s[2:5] = []
print (s)
s[:] = []
print (s)
n = [1,2,3,4,5,6,7,8,9,10]
n.append(100)
print (n)
n.insert(0,200)
print (n)
n.pop()
print (n)

n = [1,2,2,2,3]
n.remove(2)
print (n)

a = [1,2,3,4,5]
b = [6,7,8,9,10]
print (a)
print (b)
a += b
print (a)