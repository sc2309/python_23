print("\n\nhello world")

x = "pari chouksey"

print("\nx is now ",x)
print(type(x))

z,y = 'sarthak chouksey','dibbu rai'
print(type(z))
print(type (y))
print(z,"\n",y)

a = b = c = "nana ji\n"
print(a,b,c)

name = ["papa","mummy","nani"]
p,q,r = name
print(p,"\n",q,"\n",r,"\n")

print(x+y+z,"ignore this")
def test():
    global g
    g = 'new in this'
    print("\n\n",g)
def test2():
    h = 2
    print(h)
# outside this using h may throw error as it is local variable not a global variable
#print(h)
test()
test2()
u = 5
v = 10
print("\n\n",u+v)