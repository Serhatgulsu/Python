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

pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.max_column', 100)
pd.set_option('display.width', 100)



Girdi = pd.read_excel("/Users/serhatgulsu/Desktop/Girdi.xlsx", header=0)

Input = Girdi[Girdi["Acente Segmenti"] != "CUSTOMER FOCUSED"]

Input.describe().T

ınput_S = pd.DataFrame({ 'Partaj': Input["ACENTE_PARTAJI"],
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
             'Konut Yenileme': Input["Konut Yenileme"],
             'Kasko Yenileme': Input["Kasko Yenileme"],
             'Non-MTPL Payı': Input["Non-MTPL Oranı"]} )
###
#ınput_S1 = pd.DataFrame({
#             'Konut Yenileme': Input["Konut Yenileme"],
#             'Kasko Yenileme': Input["Kasko Yenileme"] } )
#
#ınput_S2 = ınput_S1[ınput_S1["Konut Yenileme"] != "Yok"]



ınput_S.describe().T

#Histogram
ınput_S.hist('Non-MTPL Payı', bins=35);
plt.title('Non-MTPL Payı');
plt.xlabel('Non-MTPL Payı');

ınput_S.hist('Trafik Payı', bins=35);
plt.title('Trafik Payı');
plt.xlabel('Trafik Payı');

#Kümülatif Yüzdesel Değerler
ınput_S['Trafik Payı %'] = ınput_S['Trafik Payı'].rank(pct = True)
ınput_S['Non-MTPL Payı %'] = ınput_S['Non-MTPL Payı'].rank(pct = True)

print(ınput_S['Trafik Payı %'])

ınput_S.describe().T

ınput_S.plot(kind="scatter", x="Trafik Payı",   y="Non-MTPL Payı")
plt.show()

ınput_S.plot(kind="scatter", x="Trafik Payı %",   y="Non-MTPL Payı %")
plt.show()


deneme = linkage(ınput_S[['Trafik Payı %', 'Non-MTPL Payı %']], method = 'ward', metric = 'euclidean')
ınput_S['Clustering10'] = fcluster(deneme,10 , criterion='maxclust', )
sns.scatterplot(x='Non-MTPL Payı %', y='Trafik Payı %',
                hue='Clustering10', data = ınput_S, palette='Set1')
plt.title("K-means Clustering10")
plt.show()


DecisionTree = ınput_S[ınput_S["Clustering2"] == 2]

print(DecisionTree)



DecisionTree.describe().T

Potansiyel_Param = pd.DataFrame({ 'Partaj': DecisionTree["Partaj"],
             'Non-MTPL Payı %': DecisionTree["Non-MTPL Payı %"],
             'SegeSkor': DecisionTree["SEGE SKOR "],
             'KişiBaşıAraç': DecisionTree["Kişibaşı Araç"],
             'KişiBaşıKonut': DecisionTree["Kişibaşı Konut"]} )

Potansiyel_Param.describe().T

plt.figure(figsize=(12,9))
sns.heatmap(Potansiyel_Param.corr(),annot=True,cmap='RdBu')
plt.title('Correlation Heatmap',fontsize=14)
plt.yticks(rotation =0)
plt.show()





