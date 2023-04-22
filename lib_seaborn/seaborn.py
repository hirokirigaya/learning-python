import seaborn as sns

sns.barplot([1,2,3,4,5,6,7,8,9,10])
sns.scatterplot([1,2,3,4,5,6,7,8,9,10])


titanic = [200, 300, 500]
df = sns.load_dataset('titanic')
sns.countplot(x=df['class'])