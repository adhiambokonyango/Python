import pandas
import sklearn
import matplotlib as plt
# modcom.co.ke/datascience; banksdata.csv
df = pandas.read_csv('banksdata.csv')
print(df)
print(df.isnull().sum())
# machine learning models don't work with empties
# ml does not work with text
df['Gender'].fillna('N', inplace=True)  # first rule of no empty
df['Gender'].replace({'Male':0, 'Female': 1, 'N': 2}, inplace=True)  # rule 2; no texts

df['Married'].fillna('N', inplace=True)  # first rule of no empty
df['Married'].replace({'No': 0, 'Yes': 1, 'N': 2}, inplace=True)  # rule 2; no texts

# no empties for education
# df('Gender').fillna('N', inplace=True)  # first rule of no empty
df['Education'].replace({'Not Graduate': 0, 'Graduate': 1}, inplace=True)  # rule 2; no texts

# self employed
df['Self_Employed'].fillna('N', inplace=True)  # first rule of no empty
df['Self_Employed'].replace({'Yes': 0, 'No': 1, 'N': 2}, inplace=True)  # rule 2; no texts

# Credit_History
df['Credit_History'].fillna(2, inplace=True)

# Property_Area
df['Property_Area'].replace({'Rural': 0, 'Urban': 1, 'Semiurban': 2}, inplace=True)  # rule 2; no texts

# dependants
df['Dependents'].fillna(4, inplace=True)

# loan amount
medianLoan = df['LoanAmount'].median()
df['LoanAmount'].fillna(medianLoan, inplace=True)

# term
medianTerm = df['Loan_Amount_Term'].median()
df['Loan_Amount_Term'].fillna(medianTerm, inplace=True)

print('Confirming empties')
print(df.isnull().sum())
print('data types')
print(df.dtypes)

# loan status not replaced /converted because its the outcome ie target var
# we split
array = df.values  # read all data into an array
# split features from target
features = array[:, 0:11]  # full colon means all rows. eleven not counted
target = array[:, 11]  # 11th column which is loan status is counted here

# we will use only 70% of data tp train our model, 2100
# use 30% to test the model

from sklearn import model_selection

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(features, target,
                                                                    test_size=0.3,
                                                                    random_state=42)
# MODEL
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()
model.fit(X_train, Y_train)
print('Model finished training...')

# ask model to predict x_test features(loan status)
predictions = model.predict(X_test)
print(predictions)

# compare prediction and y tes
from sklearn.metrics import accuracy_score
print(accuracy_score(Y_test, predictions))

from sklearn.metrics import classification_report
print(classification_report(Y_test, predictions))

# read diagonally
from sklearn.metrics import confusion_matrix
print(confusion_matrix(Y_test, predictions))

# form new member
newMember = [[0, 1, 2, 1, 0, 3500, 2000, 250, 360, 1, 1]]
observation = model.predict(newMember)
print(observation)

# we classified a new member to 'N'
# bank updated one
