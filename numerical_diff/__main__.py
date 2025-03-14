x,y = -2,3
h = 0.0001
passo = 0.01

def multi(x, y):
    return x*y

out = multi(x,y)
outX = multi(x+h,y)
outY = multi(x, y+h)

derivada_x = (outX - out)/h
derivada_y = (outY - out)/h

x = x + passo * derivada_x
y = y + passo * derivada_y
out_new = multi(x,y)

print(out_new)

