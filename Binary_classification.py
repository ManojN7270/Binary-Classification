"""
➢ Decision Tree 
➢ Random Forest 
➢ SVM/kernel SVM
"""
# Import of relevant libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, classification_report

# Loading the dataset for training and testing
df = pd.read_csv("dataset_assignment1.csv")

# Print the appropriate dataset values.
print(df.info())

# Print the number of samples values for each class
print(df['class'].value_counts())

# Plot the feature histogram
df.drop(['class'], axis=1).hist(figsize=(10, 10))
plt.show()

for c in df['class'].unique():
    print(f"Class: {c}")
    print(df[df['class']==c].describe())

# Datasets for training and testing should be separated.
X = df.drop(['class'], axis=1)
y = df['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print()

# Describing the function for testing and training a Decision Tree classifier.
def decision_tree_classifier(X_train, X_test, y_train, y_test):
    clf = DecisionTreeClassifier(random_state=42)
    param_grid = {'max_depth': [3, 5, 7]}
    cv = KFold(n_splits=10, shuffle=True, random_state=42)
    grid_search = GridSearchCV(clf, param_grid=param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    best_params = grid_search.best_params_
    print(f"Best parameters: {best_params}")

    clf = grid_search.best_estimator_
    y_pred = clf.predict(X_test)
    print(f"Decision Tree Classifier:\n{classification_report(y_test, y_pred)}\n")
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='g')
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.title("Confusion Matrix - Decision Tree Classifier")
    plt.show()
    print()

# Describing the function for testing and training a Random Forest classifier.
def random_forest_classifier(X_train, X_test, y_train, y_test):
    clf = RandomForestClassifier(random_state=42)
    param_grid = {'n_estimators': [100, 200, 300], 'max_depth': [3, 5, 7]}
    cv = KFold(n_splits=10, shuffle=True, random_state=42)
    grid_search = GridSearchCV(clf, param_grid=param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    best_params = grid_search.best_params_
    print(f"Best parameters: {best_params}")

    clf = grid_search.best_estimator_
    y_pred = clf.predict(X_test)
    print(f"Random Forest Classifier:\n{classification_report(y_test, y_pred)}\n")
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='g')
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.title("Confusion Matrix - Random Forest Classifier")
    plt.show()
    print()

# Describing the function for testing and training a SVM classifier.
def svm_classifier(X_train, X_test, y_train, y_test):
    clf = SVC(random_state=42)
    param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
    cv = KFold(n_splits=10, shuffle=True, random_state=42)
    grid_search = GridSearchCV(clf, param_grid=param_grid, cv=5, scoring='accuracy')
    grid_search.fit(X_train, y_train)
    best_params = grid_search.best_params_
    print(f"Best parameters: {best_params}")

    clf = SVC(C=1, kernel='linear', random_state=42)
    clf.fit(X_train, y_train)
    clf = grid_search.best_estimator_
    y_pred = clf.predict(X_test)
    print(f"SVM Classifier:\n{classification_report(y_test, y_pred)}\n")
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='g')
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.title("Confusion Matrix - svm_classifier")
    print()

    
    
decision_tree_classifier(X_train, X_test, y_train, y_test)
random_forest_classifier(X_train, X_test, y_train, y_test)
svm_classifier(X_train, X_test, y_train, y_test)
clf = RandomForestClassifier(n_estimators=300, max_depth=7, random_state=42)
clf.fit(X_train, y_train)
importances = clf.feature_importances_
indices = np.argsort(importances)[::-1]
feature_names = X_train.columns
plt.figure(figsize=(10, 5))
plt.title("Feature Importances")
plt.bar(range(X_train.shape[1]), importances[indices], color="b", align="center")
plt.xticks(range(X_train.shape[1]), feature_names[indices], rotation=90)
plt.tight_layout()
plt.show()
