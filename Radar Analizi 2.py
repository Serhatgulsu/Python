
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
plt.style.use('ggplot')

import pygal
import plotly.express as px
import pandas as pd

pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.max_column', None)
pd.set_option('display.width', None)

CoR = pd.read_excel("/Users/serhatgulsu/Desktop/Python.xlsx", sheet_name="a", header=0, index_col=0)
YatirimGetirisi = pd.read_excel("/Users/serhatgulsu/Desktop/Python.xlsx", sheet_name="b", header=0, index_col=0)
FonOzsermaye = pd.read_excel("/Users/serhatgulsu/Desktop/Python.xlsx", sheet_name="c", header=0, index_col=0)
PrimOzsermaye = pd.read_excel("/Users/serhatgulsu/Desktop/Python.xlsx", sheet_name="d", header=0, index_col=0)


sers/serhatgulsu/Desktop/Python.xlsx", sheet_name=1, header=0, index_col=0)
YatirimGetirisi = pd.read_excel("/Users/serhatgulsu/Desktop/Python.xlsx", sheet_name=2, header=0, index_col=0)
FonOzsermaye = pd.read_excel("/Users/serhatgulsu/Desktop/Python.xlsx", sheet_name=3, header=0, index_col=0)
PrimOzsermaye = pd.read_excel("/Users/serhatgulsu/Desktop/Python.xlsx", sheet_name=4, header=0, index_col=0)




CoR = pd.DataFrame(CoR)
OzsermayeKarliligi = pd.DataFrame(OzsermayeKarliligi)
YatirimGetirisi = pd.DataFrame(YatirimGetirisi)
PrimOzsermaye = pd.DataFrame(PrimOzsermaye)
FonPrim = pd.DataFrame(FonPrim)

CoR.shape
CoR.head()
CoR.describe()

print(CoR["2022Q4"])

#MMS_2022Q4=(CoR["2022Q4"]-CoR["2022Q4"].min())/(CoR["2022Q4"].max()-Cor["2022Q4"].min())
#print(MMS_2022Q4)
#CoR['MMS_2022Q4'] = MMS_2022Q4/

data_Q4 = pd.DataFrame({'CoR': CoR["2022Q4"],
             'OzsermayeKarliligi': OzsermayeKarliligi["2022Q4"],
             'YatirimGetirisi': YatirimGetirisi["2022Q4"],
             'PrimOzsermaye': PrimOzsermaye["2022Q4"],
             'FonPrim': FonPrim["2022Q4"] } )

Q4 = data_Q4.transpose()

print(Q4)

print(Q4['HDI Sigorta AŞ'])

print(Q4['HDI Sigorta AŞ'])

data_2022Q4= pd.DataFrame({'Sirket Adı':['Ak', 'Allianz', 'Anadolu', 'Ankara', 'Axa', 'Eureko', 'Groupama',
                              'HDI', 'Mapfre', 'Ray', 'Sompo', 'Seker', 'Zurich'],
             'CoR': CoR["2022Q4"],
             'OzsermayeKarliligi': OzsermayeKarliligi["2022Q4"],
             'YatirimGetirisi': YatirimGetirisi["2022Q4"],
             'PrimOzsermaye': PrimOzsermaye["2022Q4"],
             'FonPrim': FonPrim["2022Q4"] } )


print(data_2022Q4)


print(Q4['Sompo Sigorta AŞ'])

fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(polar=True)
ax.plot(Q4['Sompo Sigorta AŞ'])
plt.show()

Q4['Sompo Sigorta AŞ'][0]


Radar_Chart = pygal.Radar(fill=True)
Radar_Chart.title = 'Radar'
Radar_Chart.x_labels = ['CoR', 'OzsermayeKarliligi', 'YatirimGetirisi', 'PrimOzsermaye', 'FonPrim']
Radar_Chart.add('Allianz', Q4['Allianz Sigorta AŞ'])
Radar_Chart.render_to_file('Allianz.svg')

print(Q4['Sompo Sigorta AŞ'])