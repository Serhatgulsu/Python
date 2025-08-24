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



All = pd.read_excel("/Users/serhatgulsu/Desktop/Değerler/1.xlsx", sheet_name='All')
print(All)

Ozel = pd.read_excel("/Users/serhatgulsu/Desktop/Değerler/1.xlsx", sheet_name='Ozel')
print(Ozel)

Anlasmali = pd.read_excel("/Users/serhatgulsu/Desktop/Değerler/1.xlsx", sheet_name='Anlasmali')
print(Anlasmali)

sns.set(style="ticks")
sns.jointplot(x='ALL',y='Adet',data=All,kind='scatter', xlim= (10000, 300000))
sns.jointplot(x='SADECE Ozel',y='Adet',data=Ozel,kind='scatter', xlim= (10000, 300000))
sns.jointplot(x='SADECE ANLASMALI',y='Adet',data=Anlasmali,kind='scatter', xlim= (10000, 300000))


sns.jointplot(x='ALL',y='Adet',data=All,kind='hex', xlim= (10000, 300000))
sns.jointplot(x='SADECE Ozel',y='Adet',data=Ozel,kind='hex', xlim= (10000, 300000))
sns.jointplot(x='SADECE ANLASMALI',y='Adet',data=Anlasmali,kind='hex', xlim= (10000, 300000))


from sklearn.cluster import KMeans
X = All["ALL"]
X = X.values.reshape(-1, 1)
XX = list(X)
print(XX)
cluster = []
for i in range(1, 10):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 24)
    kmeans.fit(X)
    cluster.append(kmeans.inertia_)
plt.plot(range(1, 10), cluster)
plt.show()


deneme = linkage(All[['ALL', 'Adet']], method = 'ward', metric = 'euclidean')
All['cluster_labels'] = fcluster(deneme, 4, criterion='maxclust')
sns.scatterplot(x='ALL', y='Adet',
                hue='cluster_labels', data = All)
plt.xlim(10000, 400000)
plt.show()

a = All[(All['ALL'] < 200000)]
print(a)


from sklearn.cluster import KMeans
X = a["ALL"]
X = X.values.reshape(-1, 1)
XX = list(X)
print(XX)
cluster = []
for i in range(1, 10):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 24)
    kmeans.fit(X)
    cluster.append(kmeans.inertia_)
plt.plot(range(1, 10), cluster)
plt.show()

deneme = linkage(a[['ALL', 'Adet']], method = 'wards', metric = 'euclidean')
a['cluster_labels'] = fcluster(deneme, 5, criterion='maxclust')
sns.scatterplot(x='ALL', y='Adet',
                hue='cluster_labels', data = a)
plt.show()





deneme = linkage(Ozel[['SADECE Ozel', 'Adet']], method = 'ward', metric = 'euclidean')
Ozel['cluster_labels'] = fcluster(deneme, 4, criterion='maxclust')
sns.scatterplot(x='SADECE Ozel', y='Adet',
                hue='cluster_labels', data = Ozel)
plt.xlim(10000, 200000)
plt.show()




sns.jointplot(x='SADECE ANLASMALI',y='Adet',data=Anlasmali,kind='reg')
plt.xlim(10000, 100000)

deneme = linkage(Anlasmali[['SADECE ANLASMALI', 'Adet']], method = 'ward', metric = 'euclidean')
Anlasmali['cluster_labels'] = fcluster(deneme, 10, criterion='maxclust')
sns.scatterplot(x='SADECE ANLASMALI', y='Adet',
                hue='cluster_labels', data = Anlasmali)
plt.xlim(10000, 300000)
plt.show()



b = Anlasmali[(Anlasmali['Sadece Anlaşmalı'] < 150000)]
print(b)

from sklearn.cluster import KMeans
X = b["Sadece Anlaşmalı"]
X = X.values.reshape(-1, 1)
XX = list(X)
print(XX)
cluster = []
for i in range(1, 10):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 24)
    kmeans.fit(X)
    cluster.append(kmeans.inertia_)
plt.plot(range(1, 10), cluster)
plt.show()

sns.set(style="ticks")
deneme = linkage(b[['Sadece Anlaşmalı', 'Adet']], method = 'ward', metric = 'euclidean')
b['Sınıflar'] = fcluster(deneme, 4, criterion='maxclust')
sns.scatterplot(x='Sadece Anlaşmalı', y='Adet',
                hue='Sınıflar', data = b)
plt.xlim(0, None)
plt.title("K-means Clustering")
plt.show()


c = Ozel[(Ozel['SADECE Ozel'] < 150000)]
print(c)

from sklearn.cluster import KMeans
X = c["SADECE Ozel"]
X = X.values.reshape(-1, 1)
XX = list(X)
print(XX)
cluster = []
for i in range(1, 10):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 24)
    kmeans.fit(X)
    cluster.append(kmeans.inertia_)
plt.plot(range(1, 10), cluster)
plt.show()

deneme = linkage(c[['SADECE Ozel', 'Adet']], method = 'ward', metric = 'euclidean')
c['cluster_labels'] = fcluster(deneme, 4, criterion='maxclust')
sns.scatterplot(x='SADECE Ozel', y='Adet',
                hue='cluster_labels', data = c)
plt.show()


#Marka Yaş ve Ortalama

MarkaYas = pd.read_excel("/Users/serhatgulsu/Desktop/Değerler/hds.xlsx", sheet_name='MarkaYas')
print(MarkaYas)


sns.set(style="ticks")
sns.jointplot(x='Average of Hasar_Toplam_son',y='Marka',data=MarkaYas,kind='hist')
sns.jointplot(x='Average of Hasar_Toplam_son',y='Araç Yaş',data=MarkaYas,kind='hex')

from sklearn.cluster import KMeans
X = MarkaYas["Average of Hasar_Toplam_son"]
X = X.values.reshape(-1, 1)
XX = list(X)
print(XX)
cluster = []
for i in range(1, 10):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 24)
    kmeans.fit(X)
    cluster.append(kmeans.inertia_)
plt.plot(range(1, 10), cluster)
plt.show()


MarkaYas1 = MarkaYas[(MarkaYas['Marka']=="AUDI") | (MarkaYas['Marka']=="MERCEDES")]
print(MarkaYas1)
deneme = linkage(MarkaYas1[['Average of Hasar_Toplam_son', 'Araç Yaş']], method = 'ward', metric = 'euclidean')
MarkaYas1['cluster_labels'] = fcluster(deneme, 5, criterion='maxclust')
sns.scatterplot(x='Average of Hasar_Toplam_son', y='Araç Yaş',
                hue='cluster_labels', data = MarkaYas1, palette='RdBu')
plt.show()



a = []
x = 0
for i in range(0,10):
    x += 1
    a.append(x)
    print(a)



RandomData = pd.read_excel("/Users/serhatgulsu/Desktop/Değerler/hds.xlsx", sheet_name='Dosya')
print(RandomData)
random = RandomData.sample(n=400,replace=False)
print(random)
random.info

random["Ağırlıklı Ortalama"] = random['Hasar_Toplam_son'].expanding().mean()
print(random)

random["Adet"] = random.reset_index().index

x = random["Ağırlıklı Ortalama"]
y = random["Adet"]

print(y)
print(x)
sns.scatterplot(x='Adet', y='Ağırlıklı Ortalama', data = random)
sns.relplot(x='Adet', y='Ağırlıklı Ortalama', data = random, kind="line", color="green")
plt.ylim(12000, 40000)
plt.suptitle("Cumulative Sample Mean")








from sklearn.cluster import KMeans
X = df["Hasar Şiddet"]
X = X.values.reshape(-1, 1)
XX = list(X)
print(XX)
cluster = []
for i in range(1, 10):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 24)
    kmeans.fit(X)
    cluster.append(kmeans.inertia_)
plt.plot(range(1, 10), cluster)
plt.show()



df = pd.read_excel("/Users/serhatgulsu/Desktop/Değerler/hds.xlsx", sheet_name='Dosya1')
print(df)
deneme = linkage(df[['Marka Grup', 'Hasar Şiddet']], method = 'ward', metric = 'euclidean')
df['Marka_Clustering'] = fcluster(deneme, 4, criterion='maxclust', )
sns.scatterplot(x='Marka Grup', y='Hasar Şiddet',
                hue='Marka_Clustering', data = df, palette='Set1')
plt.title("K-means Clustering")
plt.show()



sns.jointplot(x='Ortalama',y='Marka',data=df,kind='scatter')
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.figure(figsize=(3, 3))
sns.jointplot(x='Ortalama',y='Marka',data=df,kind='scatter', hue='Marka_Clustering')
sns.xticks(fontsize=7)
sns.yticks(fontsize=7)
sns.figure(figsize=(3, 3))


print(df)

df.groupby(['Marka', 'Araç Yaş'])['Marka_Clustering'].aggregate('mean')


yeni = df.groupby(['Araç Yaş'])['Marka_Clustering'].aggregate('mean').plot(kind="bar", color="gray")
plt.xlabel("Marka")
plt.ylabel("Clustering")
plt.title("Clustering by Vehicle Year")
plt.xticks(fontsize=5)
plt.yticks(fontsize=5)
plt.ylim(1, 5)




from fitter import Fitter, get_common_distributions, get_distributions
df = result["Netkar"]
value = df.values
f = Fitter(df,
           distributions=['gamma',
                          'lognorm',
                          "beta",
                          "burr",
                          "norm"])
f.fit()












#######
kmeans = KMeans(n_clusters=4, init='k-means++', random_state=0).fit(All)
sns.scatterplot(data=All, x="ALL", y="Adet", hue=kmeans.labels_)
plt.show()


