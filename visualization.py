import pandas
import matplotlib

df = pandas.read_csv('power.csv', parse_dates=['Date'])
print(df)  # data frame
print(df['Solar'])
print(df['Wind'])
print(df.describe())
# positive correlation ; greater than zero all the way to one. Towards one is stong positove correlation negative
# correlation. less than zero all the way to negative one. when one goes up the other goes down. towards negative one
# is strong . zero no correlation
print(df.corr())

# subset the df
subset = df[['Solar', 'Consumption']]
print(subset.corr())

# scatter, histogram
import matplotlib.pyplot as plt
print(plt.style.available)
plt.style.use('fivethirtyeight')
figure, ax = plt.subplots()
ax.hist(df['Consumption'], color='green')
ax.set_xlabel('Consumption')
ax.set_ylabel('freq')
ax.set_title('consumption distribution')
plt.show()

# method 2
df['Consumption'].plot(kind='hist', color='red')
plt.xlabel('Consumption')
plt.ylabel('freq')
plt.title('consumption distribution using kind')
plt.show()
# scatter needs two variables
figure, ax = plt.subplots()
ax.scatter(df['Consumption'],df['Solar'], color='green')
ax.set_xlabel('Consumption')
ax.set_ylabel('Solar')
ax.set_title('consumption vs Solar distribution')
plt.show()

# scatter with method two, kind
df.plot(kind='scatter', x='Consumption', y='Solar', color='pink')
plt.xlabel('Consumption')
plt.ylabel('Solar')
plt.title('consumption vs solar')
plt.show()

# line graph/ time series
df = df.set_index('Date')  # make date starting column
df.loc['2015', ['Consumption', 'Solar', 'Wind']].plot(kind='line')
plt.xlabel('Year 2015')
plt.ylabel('Consumption')
plt.title('power usage over time in 2017')
plt.show()
# by month

df.loc['2015-05', ['Consumption', 'Solar', 'Wind']].plot(kind='line')
plt.xlabel('Year 2015 May')
plt.ylabel('Consumption, solar and wind')
plt.title('power usage over time in 2015 May')
plt.show()

# range

df.loc['2015-05-01':'2015-05-12', ['Consumption', 'Solar', 'Wind']].plot(kind='line')
plt.xlabel('Year 2015')
plt.ylabel('Consumption')
plt.title('power usage over time in 2015')
plt.show()

df.loc['2017-05-01':'2017-05-12', ['Solar', 'Wind']].plot(kind='line')
plt.xlabel('Year 2017')
plt.ylabel('Solar and Wind')
plt.title('power usage over time in 2009')
plt.show()

# modcom.co.ke/datascience



