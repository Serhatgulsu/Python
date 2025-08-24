import pandas as pd
import numpy as np
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from sklearn.preprocessing import MinMaxScaler
import pygal

pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.max_column', None)
pd.set_option('display.width', None)

Data = pd.read_excel("/Users/serhatgulsu/Desktop/Özet - Copy.xlsx", sheet_name="Ornek", header=0, index_col=0)
Data = pd.DataFrame(Data)
print(Data)


Data.shape
Data.head()
Data.describe()

print(Data["2022Q4"])

normalized_2022Q4=(Data["2022Q4"]-Data["2022Q4"].mean())/Data["2022Q4"].std()
MMS_2022Q4=(Data["2022Q4"]-Data["2022Q4"].min())/(Data["2022Q4"].max()-Data["2022Q4"].min())


print(Data["2022Q4"].std())


print(normalized_2022Q4)
print(MMS_2022Q4)

Data['normalized_2022Q4'] = normalized_2022Q4
Data['MMS_2022Q4'] = MMS_2022Q4

print(Data)



data_scaling = {'Sirket Adı':['Ak', 'Allianz', 'Anadolu', 'Ankara', 'Axa', 'Bereket', 'Doga', 'Ethica', 'Eureko', 'Generali',
                     'Groupama', 'HDI', 'Koru', 'Magdeburger', 'Mapfre', 'Neova', 'Orient', 'Ray', 'Sompo', 'Şeker',
                     'Türk Nippon', 'Unico', 'Zurich'],
             'Normal_Dist': normalized_2022Q4,
             'MMS_Dist': MMS_2022Q4}

print(data_scaling)


fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(polar=True)
ax.plot(data_scaling['Sirket Adı'] ,data_scaling['Normal_Dist'])
plt.show()

Radar_Chart = pygal.Radar()
Radar_Chart.title = 'Radar'
Radar_Chart.x_labels = ['Ak', 'Allianz', 'Anadolu', 'Ankara', 'Axa', 'Bereket', 'Doga', 'Ethica', 'Eureko', 'Generali',
                     'Groupama', 'HDI', 'Koru', 'Magdeburger', 'Mapfre', 'Neova', 'Orient', 'Ray', 'Sompo', 'Şeker',
                     'Türk Nippon', 'Unico', 'Zurich']
Radar_Chart.add('B', MMS_2022Q4)
Radar_Chart.render_to_file('Radar1.svg')

