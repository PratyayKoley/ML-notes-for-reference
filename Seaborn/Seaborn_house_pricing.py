from sklearn.datasets import fetch_california_housing
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

california_dataset = fetch_california_housing()

california_df = pd.DataFrame(california_dataset.data, columns=california_dataset.feature_names)
california_df['Price'] = california_dataset.target

print(california_df.head())
sns.set_theme()

# Displot (Plots only the distribution)
sns.displot(data=california_df['Price'])
plt.show()

# Distplot (Plots the distribution as well as the kernel density estimation kde but it is deprecated)
sns.distplot(california_df['Price'])
plt.show()

# Histplot (Plots the distribution as well as the kernel distribution estimation kde)
sns.histplot(data=california_df['Price'], kde=True)
plt.show()

# Finding the correlation of this dataframe
california_correlate = california_df.corr()
print(california_correlate)

# Heatmap without any params doesn't give any understanding 
sns.heatmap(data=california_correlate)
plt.show()

# Heatmap using params provided by seaborn

# Adjusting the figure size to fit 
fig,ax = plt.subplots(figsize=(9,8))

# cbar makes the bar show with different colors, square makes the size of the cells as square, annot makes the annotations inside the cells true, annot_kws helps to style the annotation keywords (color,size,etc.), cmap is used for colormappping of the cells and fmt is used for formatting the annot keywords .3f means till 3 decimal places.

sns.heatmap(data=california_correlate, cbar=True, annot=True, annot_kws={'size':8}, cmap='Blues', square=True, fmt= '.3f')
plt.show()