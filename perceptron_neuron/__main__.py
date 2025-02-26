import random
import numpy as np

x = np.array([[0,0], [0,1], [1,0], [1,1]])
#y = [0,0,0,1] # results OR
y = np.array([0,0,0,1]) # results AND

D = x.shape[1]
print(D)

w = [2*random.random()-1 for i in range(D)]
b = 2*random.random()-1

learning_rate = 1e-1

for step in range(101):
    cost = 0
    for x_n, y_n in zip(x,y):
        y_pred = sum([x_i*w_i for x_i,w_i in zip(x_n, w)]) + b
        y_pred = 1 if y_pred > 0 else 0
        error = y_n - y_pred
        w = [w_i + learning_rate*error*x_i for x_i, w_i in zip(x_n, w)]
        b = b+learning_rate*error
        cost += error**2
    
    if step % 10 == 0:
        print('step {0}: {1}'.format(step, cost))

print('w:', w)
print('b:', b)
print('y_pred: {0}'.format(np.dot(x, np.array(w))+b))