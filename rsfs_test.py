import numpy as np
import pandas as pd
import rsfs
from sklearn.model_selection import train_test_split

# Load the dataset from a CSV file
dataset = pd.read_csv('data3.csv')

# Split the dataset into features (X) and target variable (y)
X = dataset.iloc[:, :-1]  # Select all columns except the last one
y = dataset.iloc[:, -1]   # Select only the last column

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X.values, y.values, test_size=0.2, random_state=42)
# Print the shapes of the training and testing sets
Parameters = {
  'RSFS': {
      'Classifier': 'KNN',
      'Classifier Properties': {
          'n_neighbors': 3,
          'weights': 'distance'
      },
      'Dummy feats': 25,
      'delta': 0.05,
      'maxiters': 200,
      'fn': 'sqrt',
      'cutoff': 0.99,
      'Threshold': 10,
  },
  'Verbose': 1
}

print(rsfs.RSFS(X_train, X_test, y_train, y_test, Parameters))


