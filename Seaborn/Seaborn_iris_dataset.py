# Loading iris datatset using pandas and sklearn

# import pandas as pd
# from sklearn.datasets import load_iris
# iris_dataset = load_iris()
# iris_df = pd.DataFrame(iris_dataset.data, columns=iris_dataset.feature_names)
# print("\n", iris_df.head())

# Loading the iris dataset
import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')
print(iris.head())

sns.scatterplot(data=iris, x='sepal_length', y='petal_length', hue='species', style='species')
plt.show()