# -*- coding: utf-8 -*-
"""Raksha_S_FinalV1 (1).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MNVCWAMObvGAsmvRZ0KLStL1pi6WilLL
"""

#Raksha, Pl run the code step by step. Dont Run whole code at once.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

df = pd.read_csv('Product_Dataset.csv')
df

df.head() #if require

df.tail() #if require

df.shape #if require

df.info() #if require

df["Sales_Percentage"].mean() #change

df2= df["Sales_Percentage"].fillna(df["Sales_Percentage"]) #fill empty cell

X = df.drop("Price", axis = "columns")
y = df.drop("Sales_Percentage", axis = "columns")
print ("Shape of X = ", X.shape)
print ("Shape of y = ", y.shape)

df.describe() #if require

df.columns #if require

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = 'white'

plt.title('Car Seat Sales Data Visuals')
sns.histplot(x='Sales_Percentage', data = df, kde = False, bins = 10, color = 'Red')
plt.xlabel('Sales_Percentage')
plt.ylabel('Day')
plt.show()



plt.title('Distribution of Price')
sns.histplot(x='Price', data = df, kde = True, bins = 10, color = 'red')
plt.xlabel('SPrices')
plt.ylabel('Sales_Percentage')
plt.show()

sns.lmplot(x='Price', y='Sales_Percentage', data =df, scatter_kws = {'color' : 'red', 's':80}, aspect = 1.5)
plt.show()

X = df.drop("Price", axis = "columns")
y = df.drop("Sales_Percentage", axis = "columns")
print ("Shape of X = ", X.shape)
print ("Shape of y = ", y.shape)

#Raksha Pl read the below instruction carefully. Whole code is exectuted and validated hence follow the below instructions.

# Raksha, [25] Block Code will not be executed immediatly due to some internet / long procedure issue. Hence, keep / try to running the code more than 2 to 3 time it will be only executed after sucessfule execution of above  block code of [68]

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Let's assume 'df' is your DataFrame containing the dataset

# If the 'Brand Name' column is not present, you can create it as follows
# Replace the column name 'Brand Name' with your actual column name if different
# Here, I'm generating random brand names for demonstration purposes
df['Brand_Name'] = np.random.choice(['Graco', 'Evenflo', 'Britax', 'Maxi-Cosi', 'Safety 1st', 'Chicco'], size=len(df))

# One-hot encode the 'Brand Name' column
df = pd.get_dummies(df, columns=['Brand_Name'])

# Generate random dates as an example
start_date = pd.to_datetime('2010-01-01')
end_date = pd.to_datetime('2020-12-31')
num_records = len(df)
df['Date'] = np.random.choice(pd.date_range(start_date, end_date), num_records)

# Sort the DataFrame by date
df.sort_values('Date', inplace=True)

# Calculate the number of days since a reference date
reference_date = df['Date'].min()  # Choose the minimum date as reference
df['Days_Since_Reference'] = (df['Date'] - reference_date).dt.days

# Drop the original 'Date' column as it's no longer needed
df.drop(columns=['Date'], inplace=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and fit the model
car = LinearRegression()
car.fit(X_train, y_train)

y_pred = car.predict(X_test)
y_pred
X_test

from sklearn.model_selection import train_test_split

train_df, val_df = train_test_split(df, test_size = 0.25, random_state = 0 ) #42

print ('train_df.shape : {}'.format(train_df.shape))
print ('val_df.shape : {}'.format(val_df.shape))

#separate and assign input and target columns
input_col = 'Sales_Percentage'
target_col = 'Price'

#create separate variables to store inputs and target values for training and validation dataset
train_inputs = train_df[[input_col]] #inputs should be always 2D
train_targets = train_df[target_col]
val_inputs = val_df[[input_col]] #inputs should be always 2D
val_targets = val_df[target_col]

#import LinearRegression class from linear_model in scikit-learn
from sklearn.linear_model import LinearRegression

#Invoke of LR
model = LinearRegression()

#train our model using train_inputs and train_targets by using fit method
model.fit(train_inputs, train_targets)
print('Training Completed Successfully')

print ('Slope of the linear model is {:.2f}'.format(model.coef_[0]))

print ('Intercept of the linear model is {:.2f}'.format(model.intercept_))

m= 6.28
c= 37.17

y= m * 10.5 + c
y

#predict the values of target column with our trained model
train_preds = model.predict(train_inputs)
train_preds

from sklearn.metrics import mean_squared_error

def rmse(targets, preds):
    ''' rmse() is a helper function used to determine the root mean squared error.
        It accepts only 2 arguments:
        targets : actual output value
        preds   : predicted output value
    '''
    rmse = mean_squared_error(targets, preds, squared = False)
    return rmse

rmse(train_targets, train_preds)

pd.DataFrame({'train_inputs' : train_inputs.Sales_Percentage,'train_targets' : train_targets, 'train_preds' : train_preds})

plt.title('Predictions vs Actuals(Training Data)')
plt.plot(train_inputs.Sales_Percentage, train_preds, color = 'red')
sns.scatterplot(x=train_inputs.Sales_Percentage, y=train_targets, color = 'slateblue', s = 200)
plt.legend(['Predictions', 'Actuals'], loc = 4)
plt.show()
print(f'RMSE Loss in training dataset : {rmse(train_targets, train_preds):.2f}')

#Validation
val_preds = model.predict(val_inputs)
rmse(val_targets, val_preds)

pd.DataFrame({'val_inputs' : val_inputs.Sales_Percentage, 'val_targets' : val_targets, 'val_preds' : val_preds})

plt.title('Predictions vs Actuals(Validation Data)')
plt.plot(val_inputs.Sales_Percentage, val_preds, color = 'red')
sns.scatterplot(x=val_inputs.Sales_Percentage, y=val_targets, color = 'slateblue', s = 200)
plt.legend(['Predictions', 'Actuals'], loc = 4)
plt.show()
print(f'RMSE Loss in validation dataset : {rmse (val_targets, val_preds):.2f}')

