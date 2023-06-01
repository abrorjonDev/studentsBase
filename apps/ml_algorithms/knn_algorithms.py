"""
Importing the necessary libraries:

The pandas library is imported to load the dataset from a CSV file and manipulate it.
Various modules from the sklearn library are imported to perform data splitting, KNN
classification, and accuracy evaluation.
Loading the dataset:

The pd.read_csv() function is used to load the dataset from a CSV file. You need to
specify the correct path and filename for your dataset.
The loaded dataset is stored in a pandas DataFrame.
Splitting the dataset:

The dataset is split into features (X) and labels (y) using the drop() function from pandas.
The 'target_column' should be replaced with the actual column name in the dataset that contains the labels.
The train_test_split() function from sklearn.model_selection is used to split the dataset
into training and testing sets. It splits the data into 80% training data and 20% testing data.
You can adjust the test_size parameter to change the ratio.
The resulting X and y for both training and testing sets are stored in separate variables.
Creating and training the KNN classifier:

An instance of the KNeighborsClassifier class from sklearn.neighbors is created with n_neighbors=3.
This sets the number of neighbors to consider when making predictions.
The fit() method is called on the KNN classifier to train it using the training data (X_train and y_train).
Making predictions:

The predict() method is used to make predictions on the test set (X_test).
The predicted labels are stored in the y_pred variable.
Evaluating the accuracy:

The accuracy_score() function from sklearn.metrics is used to calculate the accuracy of the classifier
by comparing the predicted labels (y_pred) with the true labels (y_test).
The accuracy score is printed to the console.
"""
import os

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def sort_via_knn(file_path: str | os.PathLike, column_name: str, groups_count: int):
    dataset = pd.read_csv(file_path)

    X = dataset.drop(column_name, axis=1)
    y = dataset[column_name]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    knn = KNeighborsClassifier(n_neighbors=groups_count)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print("Moslik: ", accuracy)
    return accuracy
