z = 100

class CustomError(Exception):
    pass

try:
    while z > 22:
        z-=1
    raise CustomError()
except:
    print('EXCEPTION HAS BEEN THROWN')