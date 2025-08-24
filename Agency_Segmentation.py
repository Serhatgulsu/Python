import pandas as pd
import numpy as np
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from scipy.stats import iqr
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from sklearn.preprocessing import MinMaxScaler
import pygal
from sklearn.metrics import silhouette_score
from sklearn import preprocessing
from scipy.cluster.hierarchy import fcluster, linkage
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering


pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.max_column', None)
pd.set_option('display.width', None)



Input = pd.read_excel("/Users/serhatgulsu/Desktop/Input.xlsx", header=0)
ınput_Scatter = pd.DataFrame({ 'Partaj': Input["ACENTE_PARTAJI"],
             'Trafik Payı': Input["Trafik Payı"],
             'Non-MTPL Oranı': Input["Non-MTPL Oranı"] } )

print(ınput_Scatter)
print(Input["Non-MTPL Oranı"])




Input.shape
Input.head()
Input.info()


ınput_St = pd.DataFrame({ 'Partaj': Input["ACENTE_PARTAJI"],
             'Trafik Payı': Input["Trafik Payı"],
             'Tenür': Input["Tenür"],
             'Toplam GWP': Input["Toplam GWP"],
             'Çalışılan Şirket Adedi (HDI Hariç) ': Input["Çalışılan Şirket Adedi (HDI Hariç)"],
             'Çalışılan Şirket ilk 10 Adedi (HDI Hariç) ': Input["Çalışılan ilk Şirket Adedi (HDI Hariç)"],
             'Acente Bölge Payı (Prim) ': Input["Acente Bölge Payı (Prim)"],
             'SEGE SKOR ': Input["SEGE SKOR"],
             'Kişibaşı Araç': Input["Kişibaşı Araç"],
             'Kişibaşı Konut': Input["Kişibaşı Konut"],
             'Non-MTPL K/Z ': Input["Non-MTPL K/Z"],
             'KASKO HP': Input["KASKO HP"],
             'Hit Rasyo': Input["Hit Rasyo"],
             '1.PLATINUM': Input["1.PLATINUM"],
             '2.GOLD': Input["2.GOLD"],
             '3.SILVER': Input["3.SILVER"],
             '4.BRONZE': Input["4.BRONZE"],
             '5.WATCHLIST POTENTIAL': Input["5.WATCHLIST POTENTIAL"],
             '6.WATCHLIST': Input["6.WATCHLIST"],
             '7.NEGATIVE': Input["7.NEGATIVE"],
             'Non-MTPL Oranı': Input["Non-MTPL Oranı"]} )

print(ınput_St)

plt.scatter(ınput_Scatter["Non-MTPL Oranı"], ınput_Scatter["Trafik Payı"])
plt.show()

ınput_St.hist('Non-MTPL Oranı', bins=35);
plt.title('Non-MTPL Oranı');
plt.xlabel('Non-MTPL Oranı');


ınput_St.hist('Trafik Payı', bins=35);
plt.title('Trafik Payı');
plt.xlabel('Trafik Payı');


ınput_St.plot(kind="scatter", x="Non-MTPL Oranı",   y="Trafik Payı")
plt.show()


Cluster = linkage(ınput_St[['Partaj', 'KASKO HP']], method = 'ward', metric = 'euclidean')
ınput_St['cluster_labels_Kasko_HP'] = fcluster(Cluster, 9, criterion='maxclust')
sns.scatterplot(x='Partaj', y='KASKO HP',
                hue='cluster_labels_Kasko_HP', data = ınput_St)
plt.xlim()
plt.show()

fig = px.scatter(data_frame=ınput_St, x="Toplam GWP",
                 y="Tenür",
                 title="GWP vs Tenür",
                height=500,
                color_discrete_sequence = px.colors.qualitative.G10[1:])
fig.show()

####

kume = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
kume.fit(ınput_St)

print(ınput_St)

ınput_St.describe().T

plt.figure(figsize=(10, 7))
plt.scatter(ınput_St["Trafik Payı"], ınput_St["Non-MTPL Oranı"], c=cluster.labels_, cmap='jet')
plt.xlabel("Trafik Payı", fontsize=20)
plt.ylabel("Non-MTPL Oranı", fontsize=20)
plt.show()



##############
print(ınput_St)
ınput_St.describe().T

ınput_St.fillna(ınput_St.median(), inplace=True)

X = ınput_St.iloc[:, [1,2,4,5,6]].values
y = ınput_St.iloc[:, 3].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

classifier = ExtraTreesRegressor(criterion = 'entropy', random_state=0)
classifier.fit(X_train, y_train)


Input = pd.read_excel("/Users/serhatgulsu/Desktop/Input.xlsx", header=0)