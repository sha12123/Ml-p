import pandas as pd 
import numpy as np   
def thresholdOR(x):     
    if x >= 1:
        return 1 
    else:
        return 0   
    
def thresholdAND(x):     
    if x > 1:
        return 1 
    else:
         return 0
def fireOR(data, weights, output):     
        for x in data:         
            weighted_sum = np.inner(x, weights)         
            output.append(thresholdOR(weighted_sum))  

def fireAND(data, weights, output1):     
        for x in data:         
            weighted_sum = np.inner(x, weights)         
            output1.append(thresholdAND(weighted_sum))  
data = [[0,0], [0,1], [1,0], [1,1]]   

weights = [1, 1] 
output = []   
output1 = []

fireOR(data, weights, output)   
fireAND(data, weights, output1)
print("M-P model for OR gate")
t = pd.DataFrame(index=None) 
t['X1'] = [0, 0, 1, 1] 
t['X2'] = [0, 1, 0, 1] 
t['y'] = pd.Series(output)  
print(t)

print("M-P model for AND gate")
t1 = pd.DataFrame(index=None) 
t1['X1'] = [0, 0, 1, 1] 
t1['X2'] = [0, 1, 0, 1] 
t1['y'] = pd.Series(output1)  

print(t1)