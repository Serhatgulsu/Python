import pandas as pd
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

pd.set_option('display.float_format', lambda x: '%.4f' % x)
pd.set_option('display.max_column', None)
pd.set_option('display.width', None)


myk = pd.read_excel("/Users/serhatgulsu/Desktop/MYK/MYK.xlsx")
print(myk)

myk.shape
myk.head()
myk.describe().T



myk_table = pd.pivot_table(myk,
                        index='Sipariş No',
                        columns='Sipariş Kategori',
                        values='Miktar').replace(np.nan, 0).applymap(
    lambda x: True if x > 0 else False)

aaa = myk_table.head(100)
print(aaa)


# df = True-False array ya da One Hot Encoding ile dönüştürülmüş dataframe
# min_support = Tüm kombinasyonların support değerini istemiyorum bu yüzden belirli bir eşik değerini supporta göre getir.
# use_colnames = True, sutün isimlerini göster.
# verbose = 1, Toplam kombinasyon sayısını verir.
support = apriori(myk_table, min_support=0.0025, use_colnames = True, verbose=1).sort_values(by=['support'], ascending=False)
print(support)

confidence = association_rules(support, metric = "confidence", min_threshold = 0.1)
print(confidence)

confidence.to_excel("/Users/serhatgulsu/Desktop/MYK/MYKoutput3.xlsx")