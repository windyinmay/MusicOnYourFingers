import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler


import joblib
import pickle
import seaborn as sns


# Step 1: Training the Model
# Load the labeled data
labeled_data = pd.read_csv('./Data/training_dataset.csv', delimiter=",")

# Split the data into features (X) and target variable (y)
X = labeled_data.drop('Label', axis=1)
y = labeled_data['Label']

#Normalize data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

parameters = {'n_estimators':[100, 200], 'max_depth':[10, 20]}
clf1 = GridSearchCV(RandomForestClassifier(), parameters)
# Create a Random Forest Classifier
# clf = RandomForestClassifier(n_estimators=100, random_state=42)
# Advanced Modeling Techniques
#Combine RandomForest with other models like SVM, KNN and use a VotingClassifier.
clf2 = SVC(probability=True)
clf3 = KNeighborsClassifier(n_neighbors=5)

eclf = VotingClassifier(estimators=[('rf', clf1), ('svm', clf2), ('knn', clf3)], voting='soft')
# Train the classifier
# clf.fit(X_train, y_train)
eclf.fit(X_train, y_train)

# Evaluate the model (optional)
# y_pred = clf.predict(X_test)
y_pred= eclf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
# scores = cross_val_score(clf, X, y, cv=5)
scores = cross_val_score(eclf, X, y, cv=5)
conf_matrix = confusion_matrix(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print("Confusion Matrix:\n", conf_matrix)

# Save the trained model for later use
model_filename = 'finger_bent_model.pkl'
joblib.dump(eclf, model_filename)

print(f"Model trained and saved as {model_filename}")

with open('finger_bent_model.pkl', 'rb') as f:
    model_loaded_1= pickle.load(f)

sns.set_style('darkgrid')
sns.pairplot(X)