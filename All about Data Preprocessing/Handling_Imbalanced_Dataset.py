import numpy as np
import pandas as pd

# Loading the dataset
credit_card_data = pd.read_csv('DataSets/credit_data.csv')

# Printing the first five rows
print(credit_card_data.head())

# Counting the number of values of the column 'Class'
print(credit_card_data['Class'].value_counts())

# Seperating the Legit and Fraudulent Transactions
legit_transac = credit_card_data[credit_card_data['Class'] == 0]
fraud_transac = credit_card_data[credit_card_data['Class'] == 1]

# legit_transac contains 2,84,315 datapoints and fraud_transac contains 492 datapoints

# Creating a new dataset of legit_transac with random 492 points out of the old dataset of legit_transac
new_legit_transac = legit_transac.sample(n=492)     

# Printing the shape of the new dataset
print(new_legit_transac.shape)

# Creating the new credit_card dataset with mixed datapoints of 492 new_legit and 492 old_fraud transactions
# axis = 0 means combine in terms of rows not in columns
new_credit_card_data = pd.concat([new_legit_transac,fraud_transac],axis=0)

# Printing the first five rows of data
print(new_credit_card_data.head()) 

# Printing the last five rows of data
print(new_credit_card_data.tail())

# Counting the number of values of the column 'Class' in new dataset
print(new_credit_card_data['Class'].value_counts())