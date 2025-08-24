import pandas as pd
import openturns as ot
import openturns.viewer as otv
from fitter import Fitter, get_common_distributions, get_distributions
from scipy.stats import gamma
from scipy.stats import kurtosis
from scipy.stats import skew
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import scipy.integrate
import scipy.special
import pymc3 as pm
import arviz as az
import scipy.stats as st
import seaborn as sns
from scipy.stats import norm
from scipy.cluster.hierarchy import fcluster, linkage
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import fcluster, linkage
from sklearn.decomposition import PCA
from sklearn.linear_model import  LogisticRegression
import os
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from collections import Counter
import plotly.express as px
from sklearn import preprocessing
from sklearn import utils
from sklearn import metrics
from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
from sklearn.tree import DecisionTreeClassifier as dtc
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
from sklearn import datasets
from sklearn.tree import DecisionTreeRegressor
from dtreeviz.trees import dtreeviz






df1  = pd.read_csv("/Users/serhatgulsu/Desktop/segmentasyon/1.tsv", encoding='utf-16', sep="\t")
df2  = pd.read_csv("/Users/serhatgulsu/Desktop/segmentasyon/2.tsv", encoding='utf-16', sep="\t")
df3  = pd.read_csv("/Users/serhatgulsu/Desktop/segmentasyon/3.tsv", encoding='utf-16', sep="\t")
df4  = pd.read_csv("/Users/serhatgulsu/Desktop/segmentasyon/4.tsv", encoding='utf-16', sep="\t")
df5  = pd.read_csv("/Users/serhatgulsu/Desktop/segmentasyon/5.tsv", encoding='utf-16', sep="\t")
df6  = pd.read_csv("/Users/serhatgulsu/Desktop/segmentasyon/6.tsv", encoding='utf-16', sep="\t")
df7  = pd.read_csv("/Users/serhatgulsu/Desktop/segmentasyon/7.tsv", encoding='utf-16', sep="\t")
df8  = pd.read_csv("/Users/serhatgulsu/Desktop/segmentasyon/8.tsv", encoding='utf-16', sep="\t")
df9  = pd.read_csv("/Users/serhatgulsu/Desktop/segmentasyon/9.tsv", encoding='utf-16', sep="\t")
df10 = pd.read_csv("/Users/serhatgulsu/Desktop/segmentasyon/10.tsv", encoding='utf-16', sep="\t")

pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.max_column', None)
pd.set_option('display.width', None)

df = pd.DataFrame({ 'mevcutsegment' : df3['CUSTOMER_SEGMENT'],
'pvkar' : df1['PV_NET_KAR'],
'tenur' : df2['TENUR'],
'partaj' : df9['ACENTE_NO'],
'bolgeadi' : df9['BOLGE_AD'],
'iladi' : df9['ILAD'],
'arac_marka' : df4['ARAC_MARKA'],
'arac_model' :df4['ARAC_MODEL'],
'aracyas' : df8['ARAC_YAS'],
'suresonuadet' : df3['SURESONU'],
'yururlulukadet' : df3['YURURLULUKTE'],
'iptaladet' : df3['IPTAL'],
'zorunlutrafik' : df7['ZORUNLU_TRAFIK'],
'zorunludeprem' : df7['ZORUNLU_DEPREM'],
'pvnetprim' : df6['PVNETPRIM'],
'nethp' : df5['NET_HP_ORANI'],
'Net1yilhp' : df6['SON1YIL_NET_HP'],
'ultbedel' : df5['MAX_BEDEL'],
'ultbedelgrup' : df5['BEDEL_GRUP'],
'kaskokademe' : df2['KASKO_KADEME'],
'kaskodurum' : df2['KASKO_ADET'],
'kaskoyenileme' : df3['KASKO_YENILEME'],
'kaskobedel' : df3['KASKO_BEDEL'],
'kasko_onceki_sirketadi': df10['KASKO_ONCEKI_SIRKETAD'],
'trafik_kademe' : df10['TRAFIK_KADEME'],
'trafik_yenileme' : df10['TRAFIK_YENILEME'],
'trafik_onceki_sirketadi':  df10['TRAFIK_ONCEKI_SIRKETAD'],
'kaskoyenilemeadet' : df5['KASKO_YENILEME_ADET'],
'osaglıkyenilemeadet' : df6['OSAGLIK_YENILEME_ADET'],
'dotoyenilemeadet' : df6['DOTO_YENILEME_ADET'],
'yangınyenilemeadet' : df7['YANGIN_YENILEME_ADET'],
'ysaglikyenilemeadet' : df7['YSAGLIK_YENILEMEADET'],
'tssyenilemeadet' : df7['TSS_YENILEME_ADET'],
'nakliyatyenilemeadet' : df7['NAKLIYAT_YENILEME_ADET'],
'muhendisliktenilemeadet' : df8['MUHENDISLIK_YENILEME_ADET'],
'yatyenilemeadet' : df8['YAT_YENILEME_ADET'],
'saglikyenilemeadet' : df8['SAGLIK_YENILEME_ADET'],
'tarimyenilemeadet' : df8['TARIM_YENILEME_ADET'],
'trafikyenilemeadet' : df8['TRAFIK_YENILEME_ADET'],
'doto_bedel' : df8['DOTO_BEDEL'],
'yat_bedel' : df8['YAT_BEDEL'],
'ss_bedel' : df8['SS_BEDEL'],
'nakliyat_bedel' : df8['NAKLIYAT_BEDEL'],
'muhendislik_bedel' : df8['MUHENDISLIK_BEDEL'],
'havacılık_bedel': df8['HAVACILIK_BEDEL'],
'saglık_bedel': df8['SAGLIK_BEDEL'],
'tarım_bedel' : df8['TARIM_BEDEL'],
'kritik_bedel' : df8['KRITIK_BEDEL'],
'yabaci_bedel' : df8['YABANCI_BEDEL'],
'tss_bedel': df8['TSS_BEDEL'],
'yangin_bedel' : df10['YANGIN_BEDEL'],
'doto_adet' : df10['DOTO_ADET'],
'trafik_adet' :df10['TRAFIK_ADET'],
'kaza_adet' : df10['KAZA_ADET'],
'yat_adet' : df10['YAT_ADET'],
'ssaglik_adet' : df10['SSAGLIK_ADET'],
'nakliyat_adet' : df10['NAKLIYAT_ADET'],
'muhendislik_adet' : df10['MUHENDISLIK_ADET'],
'havacilik_adet' : df10['HAVACILIK_ADET'],
'saglik_adet' : df10['SAGLIK_ADET'],
'tarim_adet' : df10['TARIM_ADET'],
'tss_adet' : df10['TSS_ADET'],
'kritiksaglik_adet' : df10['KRITIKSAGLIK_ADET'],
'yabancisaglik_adet' : df10['YABANCISAGLIK_ADET'] })


df.head

print(df5)


df = pd.DataFrame({
'pvkar' : df1['PV_NET_KAR'],
'tenur' : df2['TENUR'],
'aracyas' : df8['ARAC_YAS'],
'zorunlutrafik' : df7['ZORUNLU_TRAFIK'],
'zorunludeprem' : df7['ZORUNLU_DEPREM'],
'kaskodurum' : df2['KASKO_ADET'],
'yat_adet' : df10['YAT_ADET'],
'nethp' : df5['NET_HP_ORANI'],
'ultbedel' : df5['MAX_BEDEL'],
'suresonuadet' : df3['SURESONU'],
'yururlulukadet' : df3['YURURLULUKTE'],
'iptaladet' : df3['IPTAL'],
'yangınyenilemeadet' : df7['YANGIN_YENILEME_ADET'],
'kaskoyenilemeadet' : df5['KASKO_YENILEME_ADET']})
df.replace(np.nan, 0)

plt.figure(figsize=(12,9))
sns.heatmap(df.corr(),annot=True,cmap='RdBu')
plt.title('Correlation Heatmap',fontsize=14)
plt.yticks(rotation =0)
plt.show()


df.shape
df.describe().T


q_lowkar = df['pvkar'].quantile(0.01)
q_hikar  = df['pvkar'].quantile(0.99)

df_outlierkar = df[(df['pvkar'] < q_hikar) & (df['pvkar'] > q_lowkar)]

df_outlierkar1 = df_outlierkar.replace(np.nan, 0)
df_outlierkar.shape
df.shape

df01 = df_outlierkar1.sample(40000)


aa = df01.describe().T
bb = df_outlierkar1.describe().T
print(aa)

karsilastirma = pd.DataFrame({'smean': aa['mean'],
             'bmean': bb['mean'],'smedian': aa['50%'],
             'amedian': bb['50%'], 'smin': aa['min'],
             'amin: bb['min'], 'smax': aa['max'],
             'amax': bb['max'], 'sstd': aa['std'],
             'astd': bb['std']})
print(karsilastirma)

df_outlierkar1 = df_outlierkar.replace(np.nan, 0)
print(df_outlierkar1)

X = df_outlierkar1.drop(["tenur", "zorunlutrafik", "zorunlutrafik", "zorunludeprem", "kaskodurum", "yat_adet", "nethp",
                         "ultbedel", "yangınyenilemeadet", "kaskoyenilemeadet"], axis=1)
y = df_outlierkar1["pvkar"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


model = DecisionTreeRegressor(random_state=42, max_leaf_nodes=10)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(predictions)


plt.figure(figsize=(10,8), dpi=150)
plot_tree(model, feature_names=X.columns)


from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(max_leaf_nodes=10)
classifier = classifier.fit(X_train,y_train)

y_pred = classifier.predict(X_test)

from sklearn import metrics
print('Accuracy Score:', metrics.accuracy_score(y_test,y_pred))

from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
from IPython.display import Image
import pydotplusdot_data = StringIO()
export_graphviz(classifier, out_file=dot_data,
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())







q_low = df['deger'].quantile(0.01)
q_hi  = df['deger'].quantile(0.99)

df_outlier = df[(df['deger'] < q_hi) & (df['deger'] > q_low)]

sns.displot(data=df_outlier, x='deger', kind='ecdf')


f = Fitter(df_outlierkar['pvkar'],
           distributions=['gamma',
                          'lognorm',
                          "beta",
                          "burr",
                          "norm"])
f.fit()
f.summary()

get_distributions()
f = Fitter(df_outlierkar['pvkar'],
           distributions= get_common_distributions())
f.fit()
f.summary()




dist1 = [st.norm,st.uniform,st.expon,st.logistic,st.lognorm,st.gamma]
mles1 = []

for distribution in dist1:
    pars = distribution.fit(df_outlierkar['pvkar'])
    mle = distribution.nnlf(pars, df_outlierkar['pvkar'])
    mles1.append(mle)

results1 = [(distribution.name, mle) for distribution, mle in zip(dist1, mles1)]
results1


dist2 = [st.norm,st.uniform,st.expon,st.logistic,st.lognorm,st.gamma]
mles2 = []

for distribution in dist2:
    pars = distribution.fit(df_outlier['deger'])
    mle = distribution.nnlf(pars, df_outlier['deger'])
    mles2.append(mle)

results2 = [(distribution.name, mle) for distribution, mle in zip(dist2, mles2)]
results2

sns.distplot(df_outlier['deger'])
plt.show()

print(df_outlier)


df2 = df_outlier[~pd.isnull(df_outlier['ultbedelgrup'])]
print(df2)

df2.copy


df3 = df2.sample(n = 40000)

print(df3)

des = pd.DataFrame({'orneklem' : df3['deger'].describe().T,
              'Veri' : df2['deger'].describe().T})

print(des)

bedelcluster = df3.groupby(['ultbedelgrup'], as_index=False).agg(deger =('deger', 'mean'))

print(bedelcluster)

label_encoder = preprocessing.LabelEncoder()
bedelcluster['ultbedelgrup'] = label_encoder.fit_transform(bedelcluster['ultbedelgrup'].sort_values(ascending = True))

print(bedelcluster['ultbedelgrup'])

print(df3)

ultbedelgrup = linkage(bedelcluster[['ultbedelgrup', 'deger']], method = 'median', metric = 'euclidean')
bedelcluster['cluster_ultbedelgrup'] = fcluster(ultbedelgrup, 7, criterion='maxclust')
sns.scatterplot(x='ultbedelgrup', y='deger',
                hue='cluster_ultbedelgrup', data = bedelcluster)
plt.show()

ultbedelgrup = linkage(df3[['deger', 'ultbedel']], method = 'median', metric = 'euclidean')
df3['cluster_ultbedelgrup'] = fcluster(ultbedelgrup, 7, criterion='maxclust')
sns.scatterplot(x='deger', y='ultbedel',
                hue='cluster_ultbedelgrup', data = df3)
plt.show()








label_encoder = preprocessing.LabelEncoder()
df3['ultbedelgrup'] = label_encoder.fit_transform(df3['ultbedelgrup'].sort_values(ascending = True))

print(df3['ultbedelgrup'])

ultbedelgrup = linkage(df3[['ultbedelgrup', 'deger']], method = 'median', metric = 'euclidean')
df3['cluster_ultbedelgrup'] = fcluster(ultbedelgrup, 7, criterion='maxclust')
sns.scatterplot(x='ultbedelgrup', y='deger',
                hue='cluster_ultbedelgrup', data = df3)
plt.show()

print(df2)






