import numpy as np

def orGate(inputs):
    weights = np.ones_like(inputs)
    net = np.inner(inputs,weights)
    if net >=1:
        output = 1
    else:
        output = 0
    return output

def andGate(inputs):
    weights = np.ones_like(inputs)
    net = np.inner(inputs,weights)
    threshold = inputs.shape[0]
    if net >= threshold:
        output = 1
    else: 
        output = 0
    return output

print("OUTPUT FOR OR GATE")

print("x1   x2  y")
print("0     0   ",orGate(np.array([0,0])))
print("0     1   ",orGate(np.array([0,1])))
print("1     0   ",orGate(np.array([1,0])))
print("1     1   ",orGate(np.array([1,1])))

print("OUTPUT FOR AND GATE")

print("x1   x2  y")
print("0    0  ",andGate(np.array([0,0])))
print("0    1  ",andGate(np.array([0,1])))
print("1    0  ",andGate(np.array([1,0])))
print("1    1  ",andGate(np.array([1,1])))