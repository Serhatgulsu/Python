import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn import preprocessing
import seaborn as sns
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import fcluster, linkage
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score


data = pd.read_csv("/Users/serhatgulsu/Desktop/Carseats.csv", sep =';')
print(data)

data.shape
data.describe().T


ornek = sns.PairGrid(data)
ornek.map(sns.scatterplot);


sns.pairplot(data, vars = ['Price', 'Education', 'Age'], hue = 'ShelveLoc')
sns.jointplot(x='Income',y='CompPrice',data=data,kind='scatter')

from sklearn.cluster import KMeans
X = data["CompPrice"]
X = X.values.reshape(-1, 1)
XX = list(X)
print(XX)
cluster = []
for i in range(1, 7):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 24)
    kmeans.fit(X)
    cluster.append(kmeans.inertia_)
plt.plot(range(1, 7), cluster)
plt.show()





deneme = linkage(data[['Income', 'CompPrice']], method = 'median', metric = 'euclidean')
data['cluster_labels'] = fcluster(deneme, 3, criterion='maxclust')
sns.scatterplot(x='Income', y='CompPrice',
                hue='cluster_labels', data = data)
plt.show()

print(data[['Age', 'Income', 'Education', 'CompPrice']].groupby(data['ShelveLoc']).mean())
print(data.groupby(data['ShelveLoc']).mean().T)



reg = LinearRegression()
X = data["Age"]
X = X.values.reshape(-1,1)
y = data["Income"]
reg.fit(X, y)
predictions = reg.predict(X)
print(predictions[:4])


plt.scatter(X, y, color="green")
plt.plot(X, predictions, color="red")
plt.xlabel("Age")
plt.ylabel("Income")
plt.show()


#Hatalı
from sklearn.metrics import mean_squared_error
r_squared = reg.score(X, predictions)
print("R^2: {}".format(r_squared))



random = KFold(n_splits=6, shuffle=True, random_state=5)
reg = LinearRegression()
scores = cross_val_score(reg, X, y, cv=random)
print(scores)


def ecdf(data):
    n = len(data)
    x = np.sort(data)
    print(x)
    y = np.arange(1, n + 1) / n
    return x, y
x, y = ecdf(data["Age"])
_ = plt.plot(x, y, marker='.', linestyle='none')
plt.show()


__=sns.boxplot(data["ShelveLoc"], x, data=data["Age"])
plt.show()

var = data["Age"]
def def1(var):
    mean = np.mean(var)
    std = np.std(var)
    size = len(var.index)
    samples = norm.rvs(mean, std, size =size)
    sns.distplot(var)


import scipy.stats as s
df = data["Education"]
def weib(x,n,a):
    return (a / n) * (x / n)**(a - 1) * np.exp(-(x / n)**a)
(loc, scale) = s.exponweib.fit_loc_scale(df, 1, 1)
print(loc, scale)
c = len(df)
x = np.linspace(df.min(), df.max(), df.max())
plt.plot(x, weib(x, loc, scale))
plt.hist(df, df.max(), density=True)
plt.show()


from fitter import Fitter, get_common_distributions, get_distributions
df = data["Age"]
value = df.values
f = Fitter(df,
           distributions=['gamma',
                          'lognorm',
                          "beta",
                          "burr",
                          "norm"])
f.fit()
f.summary()
f.get_best(method = 'sumsquare_error')



get_distributions()
f = Fitter(df,
           distributions= get_common_distributions())
f.fit()
f.summary()




******
fit_alpha, fit_loc, fit_beta=stats.gamma.fit(df_outlier['deger'])
print(fit_alpha, fit_loc, fit_beta)

scipy.stats.gamma.pdf(df_outlier['deger'], fit_alpha, fit_loc, fit_beta)


x = np.linspace (0, 20, 100)
y = stats.gamma.pdf(x, a=fit_alpha, scale=fit_beta)
plt.plot(x, y)
plt.show()
