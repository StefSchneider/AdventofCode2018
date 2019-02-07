import numpy as np
def three_steps(n):
    return step(n, steps=[1, 0.5, 0.25])

B = np.linspace(0.1, 1.0, 10)
print(B)
B = np.array(three_steps(100))
print ("A = ", A)

for i, value in enumerate(B):
    A[i:int(value*100)] = 0
    print (A)
list = [np.append(A, i) for k in range(i + 1)]
print (list)