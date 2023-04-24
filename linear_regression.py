import numpy as nm  
import matplotlib.pyplot as mtp  
import pandas as pd  
data_set= pd.read_csv(r'C:\Users\Administrator\Downloads\ML\salary_data.csv')

x= data_set.iloc[:, :-1].values  #for x variable, we have taken -1 value since we want to remove the last column from the dataset.
y= data_set.iloc[:, 1].values   #For y variable, we have taken 1 value as a parameter, since we want to extract the second column and indexing starts from the zero.

print(x)
print("\n",y)

# Splitting the dataset into training and test set.  
from sklearn.model_selection import train_test_split  
x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 1/3, random_state=0)

print("\nX_train",x_train)
print("\nX_test",x_test)
print("\ny_train",y_train)
print("\ny_test",y_test)

#Fitting the Simple Linear Regression model to the training dataset  
from sklearn.linear_model import LinearRegression  
regressor= LinearRegression()  
regressor.fit(x_train, y_train)  

#Prediction of Test and Training set result  
y_pred= regressor.predict(x_test)  
x_pred= regressor.predict(x_train)  

print("\ny_pred",y_pred)
print("\nx_pred",x_pred)


mtp.scatter(x_train, y_train, color="green")   
mtp.plot(x_train, x_pred, color="red")    
mtp.title("Salary vs Experience (Training Dataset)")  
mtp.xlabel("Years of Experience")  
mtp.ylabel("Salary(In Rupees)")  
mtp.show()   

