# analyse data using plots
# install package to acquire data
# clean
# analyse
# pandas and matplotlib
# degrade to 3.6
# http://justpaste.it/4p2xa
import pandas  # acquire data and leaning
import matplotlib  #plot/visualize
# modcom.co.ke/datascience
data = pandas.read_csv('power.csv')
print(data)
print(data['Solar'])
print(data['Consumption'])
print(data.describe())  # give basic stat
print(data.shape)  # gives how many rows and columns
print(data.isnull().sum())  # sum of missing data

import matplotlib.pyplot as plt
fig, object = plt.subplots()
object.hist(data['Consumption'], color='orange')
plt.title('distribution of consumption')
plt.xlabel('Consumption GWh')
plt.ylabel('freq')
plt.show()

fig, object = plt.subplots()
object.hist(data['Wind'], color= 'orange')
plt.title("Distribution of Wind")
plt.xlabel("Wind GWh")
plt.ylabel("Freq.")
plt.show()


fig, object = plt.subplots()
object.scatter(data['Consumption'], data['Wind'], color= 'gray')
plt.title("Distribution of Consumption vs Wind")
plt.xlabel("Consumption GWh")
plt.ylabel("Wind GWh.")
plt.show()

fig, object = plt.subplots()
object.scatter(data['Consumption'], data['Wind+Solar'], color= 'red')
plt.title("Distribution of Consumption vs Wind+Solar")
plt.xlabel("Consumption GWh")
plt.ylabel("Wind+Solar GWh.")
plt.show()
