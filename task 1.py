a = 10
b = 154.22
c = "155"
d = ['abc', 456, 23.5]
e = ('def', 123)
f = {'name': 'hello', 'code': '456'}
z = True

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))
print(z, type(z))
print('----------')

print('INT to others')
print(a, type(a))
g = float(a); print(g, type(g))
h = str(a); print(h, type(h))
i = list(map(int, str(a))); print(i, type(i))
j = tuple(map(int, str(a))); print(j, type(j))
Z = dict(enumerate(h)); print(Z, type(Z))
print('----------')

print('FLOAT to others')
print(b, type(b))
k = int(b); print(k, type(k))
l = str(b); print(l, type(l))
m = list(l); print(m, type(m))
n = tuple(l); print(n, type(n))
z = dict(enumerate(l)); print(z, type(z))
print('----------')

print('STRING to others')
print(c, type(c))
o = int(c); print(o, type(o))
p = float(c); print(p, type(p))
q = list(c); print(q, type(q))
r = tuple(c); print(r, type(r))
y = dict(enumerate(c)); print(y, type(y))
print('----------')

print('LIST to others')
print(d, type(d))
s = tuple(d); print(s, type(s))
t = dict(enumerate(d)); print(t, type(t))
print('----------')

print('TUPLE to others')
print(e, type(e))
u = list(e); print(u, type(u))
v = dict(enumerate(e)); print(v, type(v))
print('----------')

print('DICT to others')
print(f, type(f))
w = list(f.items()); print(w, type(w))
x = tuple(f.items()); print(x, type(x))