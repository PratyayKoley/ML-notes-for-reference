import seaborn as sns
import matplotlib.pyplot as plt

# Importing 'tips' dataset from seaborn

tips = sns.load_dataset('tips')

# shows the first five rows of dataset
print(tips.head())

# Gives a grid format to the plot
sns.set_theme()

# data: Specifies the DataFrame containing the dataset to be used for plotting. Here, it is tips.
# x: Defines the variable to be plotted on the x-axis, which in this case is total_bill.
# y: Defines the variable to be plotted on the y-axis, which in this case is tip.
# col: Splits the plot into multiple columns based on the unique values of the specified column. Here, col='time' creates separate plots for lunch and dinner.
# hue: Uses the specified column to differentiate data points by color. Here, hue='smoker' colors points differently based on whether the customer is a smoker or not.
# style: Uses the specified column to differentiate data points by marker style. Here, style='smoker' assigns different marker styles to smokers and non-smokers.
# size: Uses the specified column to determine the size of the data points. Here, size='size' adjusts the size of the points based on the size of the dining party.

# Creates a relational plot

sns.relplot(data=tips, x='total_bill', y='tip',col='time',hue='smoker',style='smoker',size='size')
plt.show()