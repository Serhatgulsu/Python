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
from scipy.cluster.hierarchy import fcluster, linkage
from mlxtend.preprocessing import minmax_scaling
from sklearn.cluster import KMeans
from pandas.plotting import scatter_matrix


pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.max_column', 100)
pd.set_option('display.width', 100)

Girdi = pd.read_excel("/Users/serhatgulsu/Desktop/Girdi.xlsx", header=0)

Input = Girdi[Girdi["Acente Segmenti"] != "CUSTOMER FOCUSED"]


Input.describe().T

Girdi_adj = pd.DataFrame({ 'Partaj': Input["ACENTE_PARTAJI"],
             'MTPL Payı': Input["Trafik Payı"],
             'Tenür': Input["Tenür"],
             'Toplam GWP': Input["Toplam GWP"],
             'Çalışılan Şirket Adedi (HDI Hariç) ': Input["Çalışılan Şirket Adedi (HDI Hariç)"],
             'Çalışılan Şirket ilk 10 Adedi (HDI Hariç) ': Input["Çalışılan ilk Şirket Adedi (HDI Hariç)"],
             'Acente Bölge Payı (Prim) ': Input["Acente Bölge Payı (Prim)"],
             'SEGE SKOR': Input["SEGE SKOR"],
             'SEGE SKOR2': Input["SEGE SKOR2"],
             'Kişibaşı Araç': Input["Kişibaşı Araç"],
             'Kişibaşı Konut': Input["Kişibaşı Konut"],
             'Non-MTPL K/Z ': Input["Non-MTPL K/Z"],
             'KASKO HP': Input["KASKO HP"],
             'Hit Rasyo': Input["Hit Rasyo"],
             'ilk 4 Segment Payı': Input["ilk 4 Segment"],
             'Bölge Payı': Input["Acente Bölge Payı (Prim)"],
             'Konut Yenileme': Input["Konut Yenileme"],
             'Kasko Yenileme': Input["Kasko Yenileme"],
             'Non-MTPL Payı': Input["Non-MTPL Oranı"]} )

Input.describe().T

#Histogram
Girdi_adj.hist('Non-MTPL Payı', bins=35);
plt.title('Non-MTPL Payı');
plt.xlabel('Non-MTPL Payı');

Girdi_adj.hist('MTPL Payı', bins=35);
plt.title('MTPL Payı');
plt.xlabel('MTPL Payı');

Girdi_adj.plot(kind="scatter", x="Non-MTPL Payı",   y="MTPL Payı")
plt.title('Üretim Dağılımı');
plt.show()

deneme = linkage(Girdi_adj[['MTPL Payı', 'Non-MTPL Payı']], method = 'ward', metric = 'euclidean')
Girdi_adj['Clusteringpre'] = fcluster(deneme,3 , criterion='maxclust', )
sns.scatterplot(x='Non-MTPL Payı', y='MTPL Payı',
                hue='Clusteringpre', data = Girdi_adj, palette='Set1')
plt.title("K-means Clusteringpre")
plt.show()


def flag_girdi(Girdi_adj):
    if (Girdi_adj['Clusteringpre'] == 1):
        return 'A'
    elif (Girdi_adj['Clusteringpre'] == 2):
        return 'C'
    elif (Girdi_adj['Clusteringpre'] == 3):
        return 'B'
        return np.nan


Girdi_adj['Pre-Clustering'] = Girdi_adj.apply(flag_girdi, axis=1)
print(Girdi_adj['Pre-Clustering'])

#Girdi_adj['Non-MTPL Payı %_ilk'] = Girdi_adj['Non-MTPL Payı'].rank(pct = True)
#Girdi_adj['MTPL Payı %_ilk'] = Girdi_adj['MTPL Payı'].rank(pct = True)
#Girdi_adj.to_excel("/Users/serhatgulsu/Desktop/Girdi_adj4.xlsx")





Girdi_adj_2 = Girdi_adj[Girdi_adj["Pre-Clustering"] == "B"]

Girdi_adj.groupby(['Clusteringpre','Pre-Clustering'])['Pre-Clustering'].count()

Girdi.shape
Girdi_adj.shape
Girdi_adj_2.shape


Girdi_adj_2.describe().T


#Kümülatif Yüzdesel Değerler
Girdi_adj_2['Non-MTPL Payı %'] = Girdi_adj_2['Non-MTPL Payı'].rank(pct = True)
Girdi_adj_2['Bölge Payı %'] = Girdi_adj_2['Bölge Payı'].rank(pct = True)
Girdi_adj_2['Kişibaşı Araç %'] = Girdi_adj_2['Kişibaşı Araç'].rank(pct = True)
Girdi_adj_2['Kişibaşı Konut %'] = Girdi_adj_2['Kişibaşı Konut'].rank(pct = True)
Girdi_adj_2['SEGE SKOR2'] = Girdi_adj_2['SEGE SKOR2'].rank(pct = True)




Girdi_adj_2.to_excel("/Users/serhatgulsu/Desktop/Girdi_adj2.xlsx")

Girdi_adj_3 = pd.DataFrame({ 'Partaj': Girdi_adj_2["Partaj"],
             'Non-MTPL Payı %': Girdi_adj_2['Non-MTPL Payı %'],
             'Bölge Payı %': Girdi_adj_2['Bölge Payı %'],
             'Kişibaşı Araç %': Girdi_adj_2['Kişibaşı Araç %'],
             'Kişibaşı Konut %': Girdi_adj_2['Kişibaşı Konut %'],
             'SEGE SKOR %': Girdi_adj_2['SEGE SKOR2']} )

#
Girdi_adj.to_excel("/Users/serhatgulsu/Desktop/Girdi_adj1.xlsx")


minmax_scaling(Girdi_adj_3, columns=['Non-MTPL Payı %', 'Bölge Payı %', 'Kişibaşı Araç %', 'Kişibaşı Konut %', 'SEGE SKOR %'])

Girdi_adj_3.describe().T

Girdi_adj_3.shape
Girdi_adj_4 = Girdi_adj_3.dropna()

kmeans = KMeans(n_clusters=7)
y = kmeans.fit_predict(Girdi_adj_3[['Non-MTPL Payı %', 'Bölge Payı %', 'Kişibaşı Araç %', 'Kişibaşı Konut %', 'SEGE SKOR %']])
Girdi_adj_3['Cluster7'] = y
print(Girdi_adj_3.head())


scatter_1 = pd.DataFrame({ 'Non-MTPL Payı %': Girdi_adj_3['Non-MTPL Payı %'],
             'Bölge Payı %': Girdi_adj_3['Bölge Payı %'],
             'Kişibaşı Araç %': Girdi_adj_3['Kişibaşı Araç %'],
             'Kişibaşı Konut %': Girdi_adj_3['Kişibaşı Konut %'],
             'SEGE SKOR %': Girdi_adj_3['SEGE SKOR %'],
             'Cluster3': Girdi_adj_3['Cluster3'] } )

scatter_3 = pd.DataFrame({ 'Non-MTPL Payı %': Girdi_adj_3['Non-MTPL Payı %'],
             'Bölge Payı %': Girdi_adj_3['Bölge Payı %'],
             'Kişibaşı Araç %': Girdi_adj_3['Kişibaşı Araç %'],
             'Kişibaşı Konut %': Girdi_adj_3['Kişibaşı Konut %'],
             'SEGE SKOR %': Girdi_adj_3['SEGE SKOR %'],
             'Cluster7': Girdi_adj_3['Cluster7'] } )


sns.set_theme(style="ticks")
sns.pairplot(scatter_3, hue='Cluster7')

