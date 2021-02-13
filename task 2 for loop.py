variable = [1, 1.0, '123', ('456', 1), {'789': 1}, ['000', 1]]

for val in variable:
    if type(val) == int:
        print('Converting int to other datatypes.')
        print(val, type(val))
        a = float(val); print(a, type(a))
        b = str(val); print(b, type(b))
        c = list(map(int, str(val))); print(c, type(c))
        d = tuple(map(int, str(val))); print(d, type(d))
        e = dict(enumerate(b)); print(e, type(e))
        print('---------')
    elif type(val) == float:
        print('Converting float to other datatypes.')
        print(val, type(val))
        a = int(val); print(a, type(a))
        b = str(val); print(b, type(b))
        c = list(b); print(c, type(c))
        d = tuple(b); print(d, type(d))
        e = dict(enumerate(b)); print(e, type(e))
        print('---------')
    elif type(val) == str:
        print('Converting string to other datatypes.')
        print(val, type(val))
        a = int(val); print(a, type(a))
        b = float(val); print(b, type(b))
        c = list(val); print(c, type(c))
        d = tuple(val); print(d, type(d))
        e = dict(enumerate(val)); print(e, type(e))
        print('---------')
    elif type(val) == tuple:
        print('Converting tuple to other datatypes.')
        print(val, type(val))
        for x in val:
            a = int(x)
            print(a, type(a))
            b = float(x)
            print(b, type(b))
            c = str(x)
            print(c, type(c))
        l = list(val); print(l, type(l))
        v = dict(enumerate(val)); print(v, type(v))
        print('---------')
    elif type(val) == dict:
        print('Converting dict to other datatypes.')
        print(val, type(val))
        s = list(val.items())
        for j in s:
            u = list(j); print(u, type(u))
        for y in u:
            a = int(y)
            print(a, type(a))
            b = float(y)
            print(b, type(b))
            c = str(y)
            print(c, type(c))
        t = tuple(val.items()); print(t, type(t))
        print('---------')
    elif type(val) == list:
        print('Converting list to other datatypes.')
        print(val, type(val))
        for x in val:
            a = int(x)
            print(a, type(a))
            b = float(x)
            print(b, type(b))
            c = str(x)
            print(c, type(c))
        s = tuple(val); print(s, type(s))
        t = dict(enumerate(val)); print(t, type(t))
        print('---------')



print('The End')
