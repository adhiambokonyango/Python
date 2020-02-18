import pandas
import matplotlib

df = pandas.read_csv('top50.csv')
print(df)  # data frame
print(df['Beats.Per.Minute'])
print(df['Energy'])
print(df.describe())

import matplotlib.pyplot as plt
print(plt.style.available)
plt.style.use('fivethirtyeight')
figure, ax = plt.subplots()
ax.hist(df['Beats.Per.Minute'], color='green')
ax.set_xlabel('Energy')
ax.set_ylabel('freq')
ax.set_title('Beats Per Minute vs Energy')
plt.show()

# method 2
df['Beats.Per.Minute'].plot(kind='hist', color='red')
plt.xlabel('Beats.Per.Minute')
plt.ylabel('freq')
plt.title('Beats.Per.Minute')
plt.show()

# scatter needs two variables
figure, ax = plt.subplots()
ax.scatter(df['Beats.Per.Minute'],df['Danceability'], color='green')
ax.set_xlabel('Beats.Per.Minute')
ax.set_ylabel('Danceability')
ax.set_title('Beats.Per.Minute vs Danceability')
plt.show()
# scatter needs two variables
figure, ax = plt.subplots()
ax.scatter(df['Length.'],df['Popularity'], color='green')
ax.set_xlabel('Length.')
ax.set_ylabel('Popularity')
ax.set_title('Length. vs Popularity')
plt.show()

figure, ax = plt.subplots()
ax.scatter(df['Loudness..dB..'],df['Popularity'], color='green')
ax.set_xlabel('Loudness..dB..')
ax.set_ylabel('Popularity')
ax.set_title('Loudness..dB.. vs Popularity')
plt.show()


# barh
df.groupby('Beats.Per.Minute')['Liveness'].mean().plot(kind='barh')  # or do barh
plt.title('Beats.Per.Minute and Liveness %')
plt.xlabel('Beats.Per.Minute')
plt.ylabel('Liveness %')
plt.show()




print(df.corr())

# subset the df
subset = df[['Beats.Per.Minute', 'Danceability']]
print(subset.corr())


# MACHINE LEARNING
print('Confirming empties')
print(df.isnull().sum())
print('data types')
print(df.dtypes)

array = df.values  # read all data into an array
# split features from target
features = array[:, 0:9]  # full colon means all rows. eleven not counted
target = array[:, 9]  # 11th column which is loan status is counted here

from sklearn import model_selection

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(features, target,
                                                                    test_size=0.3,
                                                                    random_state=42)
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()
model.fit(X_train, Y_train)
print('Model finished training...')
# MODEL
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier()
model.fit(X_train, Y_train)
print('Model finished training...')

# ask model to predict x_test features(popularity)
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
newMember = [[93, 45, 70, -7, 16, 14, 261, 12, 15]]
observation = model.predict(newMember)
print(observation)









