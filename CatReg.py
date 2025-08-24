
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
import seaborn as sns
from sklearn.model_selection import train_test_split
from statsmodels.formula.api import ols
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.float_format', lambda x: '.2f' % x)
pd.set_option('display.max_column', 100)
pd.set_option('display.width', 100)


Reg = pd.read_excel("/Users/serhatgulsu/Desktop/Exposure_Verisi - 1.xlsx", header=0)
tips = sns.load_dataset("Reg")


Reg.describe().T

Reg["Tvar"]




model = ols('Reg["Tvar"] ~ Reg["Bedel"] + C(Reg["LOC_ADRESS _ opt"]) + C(Reg["PORTFOY_TIPI"]) + C(Reg["CONBLDG"]) + '
            'C(Reg["OCC"]) + C(Reg["POLUSERLOB"]) + Reg["Bedel"]', data=Reg)
fitted_model = model.fit()
fitted_model.summary()

abs = fitted_model.summary()

print(abs)

abs.to_excel("/Users/serhatgulsu/Desktop/PythonReg.xlsx")


