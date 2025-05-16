print("hello")

a=10
print(id(a))
print(type(a))

b='python'
print(len(b))
print(b[1])
print(b[-4])

c=[1,2,3,4]
print(c)
print(len(c))
c.append(5)
print(c)
c.insert(0,100)
print(c)
c.remove(100)
print(c)
c[1]='heterogenous list'
print(c)

d=[1,2,3,4,[10,20],5]
print(d[4][1])

e={1,2,3,4,1,2,3,5}
print(e)

fruits={'orange','mango'}
fruits.add('apple')
fruits.remove('apple')
fruits.pop()
print(fruits)

g={1:'apple',2:'orange'}
print(g)
print(g[2])
print(g.get(1))
print(g.keys())
print(g.values())
print(g.items())
g[3]='mango'
print(g)

h=[8,7,5]
h.sort()
print(h)
h.reverse()
print(h)

i='STRING'
print(i.lower())

j='StriNG'
print(j.swapcase())

my_value=("j","h","k")
x='#'.join(my_value)
print(x)

my='company'
print(my.isalnum())
print(my.isdigit())

#passing marks example

number=int(input('enter your marks:'))

if number > 90:
    print('excellent')
elif number > 80 and number < 90:
    print('very good')
elif number > 70 and number < 80:
    print('good')
elif number > 40 and number < 70:
    print('average')
else:
    print('fail')

#vote elgibility

age=int(input('enter your age:'))

if age > 18:
    print('eligible for voting')
else:
    print('not elgible for voting')    