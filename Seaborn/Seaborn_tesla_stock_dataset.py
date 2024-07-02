import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

tesla_df = pd.read_csv("C:\Machine Learning\DataSets\Tasla_Stock_Updated_V2.csv")

print(tesla_df.head())

sns.lineplot(data=tesla_df, x='Date', y='Close')
plt.xticks(fontsize=6)
# rotates the x labels by 45 deg
plt.gca().xaxis.set_major_locator(plt.MaxNLocator(10))  
# gca => get current axes, then select xaxis, MaxNLocator => maximum labels to be shown 
plt.show()