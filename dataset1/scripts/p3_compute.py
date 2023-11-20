import pandas as pd
import pickle
import joblib


from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score, classification_report, confusion_matrix

from sklearn.dummy import DummyClassifier

from xgboost import XGBClassifier, XGBRegressor

df = pd.read_csv('dataset1/data//processed/nypd_100k.csv')
len(df)

# drop rows with missing values
df.dropna(inplace=True)
len(df)

X = df.drop('vic_race', axis=1)  # Features (all columns except 'arrest')
y = df['vic_race']

scaler = StandardScaler()
scaler.fit(X)  # Fit the scaler to the data

X_scaled = scaler.transform(X)

X_train, X_temp, y_train, y_temp = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Check the size of each set
(X_train.shape, X_val.shape, X_test.shape)

##### Create a baseline model using DummyClassifier
# Initialize the DummyClassifier
dummy = DummyClassifier(strategy='most_frequent')
# Train the model on the training set
dummy.fit(X_train, y_train)
dummy_acc = dummy.score(X_val, y_val)

# Initialize the Logistic Regression model
log_reg = LogisticRegression()
# Train the model on the training set
log_reg.fit(X_train, y_train)
# Predict on the validation set
y_val_pred = log_reg.predict(X_val)
# Evaluate the model
log_reg_acc = log_reg.score(X_val, y_val)
log_reg_mse = mean_squared_error(y_val, y_val_pred)
log_reg_r2 = r2_score(y_val, y_val_pred)
# Print confusion matrix
print(confusion_matrix(y_val, y_val_pred))
# Display the classification report
print(classification_report(y_val, y_val_pred))
# Print the results
print('Baseline accuracy:', dummy_acc)
print('Logistic Regression accuracy:', log_reg_acc)
print('Logistic Regression MSE:', log_reg_mse)
print('Logistic Regression R2:', log_reg_r2)

pickle.dump(X_train, open('dataset1/models/X_train.sav', 'wb'))
# Pkle X.columns for later use in explanation
pickle.dump(X.columns, open('dataset1/models/X_columns.sav', 'wb'))
pickle.dump(scaler, open('dataset1/models/scaler_100k.sav', 'wb'))