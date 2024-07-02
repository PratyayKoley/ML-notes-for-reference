import seaborn as sns
import matplotlib.pyplot as plt

# Loading the titanic dataset
titanic = sns.load_dataset('titanic')

print(titanic.head())

# Countplot => shows the number of people in each class
sns.countplot(data=titanic, x='class')
plt.show()

# shows the number of people survived
sns.countplot(data=titanic, x='survived')
plt.show()

# shows the number of people alive 
sns.countplot(data=titanic, x='alive')
plt.show()

# shows the number of people who are male or female
sns.countplot(data=titanic, x='sex')
plt.show()

# Barplot => using different bars to plot a data
sns.barplot(data=titanic, x="sex", y='survived',hue='class')
plt.show()