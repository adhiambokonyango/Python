import pandas
import matplotlib


df = pandas.read_csv('school.csv', parse_dates=['enrolldate'])
print(df)
print(df.isnull().sum())
# imputation // process of dealing with missing records or remove them
df['Gender'].fillna(2, inplace=True)
df['Smoking'].fillna(3, inplace=True)
df['Major'].fillna('unknown', inplace=True)

# if missing is numeric
median = df['Reading'].median()
df['Reading'].fillna(median, inplace=True)
median = df['StudyTime'].median()
df['StudyTime'].fillna(median, inplace=True)
print(df.isnull().sum())

# pie charts and bar charts
import matplotlib.pyplot as plt
df.groupby('Smoking').size().plot(kind='pie', autopct='%2.2f%%',
                                  explode=(0, 0, 0.2, 0))
plt.title('Smoking proportion in %')
plt.xlabel('')
plt.ylabel('')
plt.show()

# bar chart
df.groupby('Gender')['Math'].mean().plot(kind='barh')  # or do barh
plt.title('Smoking and math score %')
plt.xlabel('Gender')
plt.ylabel('Math Score %')
plt.show()

df.groupby('Gender')['StudyTime'].mean().plot(kind='barh')  # or do barh
plt.title('Gender and SudyTime %')
plt.xlabel('Gender')
plt.ylabel('StudyTime %')
plt.show()

# histogram of writing and study time
# scatter of math and english
# pie chart for rank
# bar chart of math performance by rank
# line plot of enroll date and math performance
# machine learning
