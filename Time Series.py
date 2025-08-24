#Zaman Serisi
#ortalama, varyans ve kovaryans sabit ise zaman serisi durağandır. Durağanlıktan kurtarmak istersek fark almamız gerekir.
#Trend, uzun vadede artış veya azalıştır.
#Mevsimsellik, belirli bir davranışı, belirli periyodlarda tekrarlamasına denir.
#windows size, k adet önceki değerin hareketli ortalamasını almak demektir.
#ağırlıkı ortalama, hareketli ortalamanın dönemsel olarak ağırlıklandırarak hesaplamaya dahil edilmesidir.



import itertools
import warnings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import mean_absolute_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.tsa.api as smt
import seaborn as sns
import time

warnings.filterwarnings('ignore')

data = sm.dataset.co2.load.pandas()
y = data.data

#verinin periodunu değştirmek istersek. y= y[veri9.resample('ms').mean()
# boş değerleri doldurmak istersek y.isnull().sum() bakılır. y.fillna(y.bfill()) denir.
#seriyi görselleştirmek istersek y.plot(figsize=(15,6)) plt.show()


train = y[: dönem]
test = y[dönem:]

#SES
ses_model = SimpleExpSmoothing(train).fit(smoothing_level=0.5)
y.pred = ses_model.forecast(48)
mean_absolute_error(test, Y_pred)
train.plot(title= 'SES')
test.plot()
y_pred.plot()
plt.show()


def= plot_co2(train, y_pred, title):
mae = mean_absolute_error(test, y_pred)
train[dönem:].plot(legend=True, label='TRAIN', title=f"{title}, MAE:{round(mae,2)}")
test.plot(legend=True, label='TEST', figsize=(6,4))
y_pred.plot(legend=True, label='PREDICTION')
plt.show()
plot_co2(train, test, y_pred, "SES")


ses_model.params

def ses_optimizer(train, alphas, step=48):
    alphas = np_arrange(0.8, 1, 0.01)
#yt_sapka = a*yt-1 +(1-a)*(yt-1)_sapka
ses_optimizer(train, alphas)

best_alpha, best_mae = ses_optimizer(train, alphas)
ses_model = SimpleExpSmoothing(train).fit(smoothing_level=best_alpha)
Y_pred = ses_model.forecast(48)
plot_co2 = train, test, Y_pred, 'SES')


#DES LEVEL + TREND
des_model = ExponentialSmoothing(train, trend="add").fit(smoothing_level=0.5, smoothing_trend=0.5)
y_pred = des_model.forecast(48)
plot_co2(train, test, y_pred, "DES")

def des_optimizer(train, alphas, betas, step=48):
    alphas = np.arrange(0.01, 1, 0.1)
    betas = np.arrange(0.01, 1, 0.1)

    best_alpha, best_beta, best_mae = des_optimizer(train, alphas, betas)
final_des_model = ExponentialSmoothing(train, trend?"add").fit(smoothing_level=best_alpha,
                                                               smoothing_slope=best_beta)
Y_pred = final_des_model.forecast(48)

#toplamsal değilse çarpımsal olması için add yeirne mul dememiz gerekiyor.
plot_co2(train, test, y_pred, "DES")

#TES (Holt-winters) LEVEL + TREND + MEVSİMSELLİK
tes_model = ExponentialSmoothing(train,
                                 trend="add",
                                 seasonal="add",
                                 seasonal_periods=12).fit(smoothing_level=0.5,
                                                          smoothing_slope=0.5,
                                                          smoothing_seasonal=0.5)

y_pred = tes_model.forecast(48)
plot_co2(traid, test,Y_pred, "TES")


#Ar(p) autoregression, geçmiş zaman gözlemlerinden doğrusal bir kombinasyonu ile tahmin edilir. Trend ve mevsimsellik içermeyen tek değişkenli zaman serileri için uygundur.
#p gecikme sayısıdır.
#ma(q), önceki zaman adımlarında elde edilen hataların doğrusal bir kombinasyonu ile tahmin yapılır.
#ARMA(p,q), AR + MA geçmiş değer ve geçmiş hataların linear kombinasyonu ile tahmini yapılır.
#ARIMA(p-gecikme sayısı, d- fark ifadesi, q- artıklarda kaç gecikme alınmalı, önceki zaman adımlarındaki farkı alınmış gözlemlerin ve hataların doğrusal kombinasyonu ile tahmin yapılır.

from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

warnings.filterwarnings(('ignore')


data = sm.dataset.cow.load.pandas()
y = data.data
y = y['co2'].resample('MS').mean()
y = y.fillna(7.bfill()))
train = y[: 'ddd']
test = y['ddd', :]


arima_model = ARIMA(train, order(1,1,1)).fit(disp=0)
arima_model.summary()

y_pred = arima_model.forecast(48)[0]
y_pred = pd.Series(y_pred, index=test.index)
plot_co2(train, test, y_pred, "ARIMA")

def plot_co2(train, test, y_pred, title):
    mae = mean_absolute_error(test, y_pred)
    train['donem':].plot(legend=True, label="TRAIN", title= f"{title}, MAE:{round(mae,2)}")
    test.plot(legend=True, label="TEST", figsize=(6,4))
    y_pred.plot(legend=True, label="PREDICTION")


p = d = q range(0, 4)
pdq = list(itertools.product(p, d, q))

def arima_optimizer(train, orders):
    best_aic, best_params = float("inf"), None
    for order in orders:
        try:
            arima_model_result = ARIMA(train, order).fit(disp=0)
            aic = arima_model_result.aic
            if aic < best_aic:
                best_aic, best_params = aic, order
                print('ARIMA%s AIC=%.2f' % (orders, aic))
        except:
            continue
            print('Best ARIMA%s AIC=%.2f' % (best_params, best_aic))
            return best_params

#final modeli
arima_model = ARIMA(train, best_params_aic).fit(disp=0)
y_pred = arima_model.foracast(48)[0]
y_pred = pd.Series(y_pred, index=test.index)

plot_co2(train, test, y_pred, "ARIMA")

#SARIMA

model= SARIMAX(train, order=(1,0,1), seasonal_order=(0,0,0,12))
sarima_model = model.fit(disp=0)
y_pred_test= sarima_model.get.forecast(steps=48)
y_pred = y_pred_test.predicted_mean
y_pred = pd.Series(y_pred index=test.index)
plot_cow(train test, y_pred, "SARIMA")

p = d = q = range(0,2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0],x[1], x[2], 12]) for x in list(itertools.product(p, d,q))]

def sarima_optimizer_aic(train, pdq, seasonal_pdq):
    best_aic, best_order, best_seasonal_order = float("inf"), float("inf"), None
    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                sarimax_model = SARIMAX(train, order=param, seasonal_order=param_seasonal)
                results = sarimax_model.fit(disp=0)
                aic = result_aic:
                if aic < best_aic:
                    best_aic, best_order, best_seasonal_order = aic, param, param_seasonal
                    print('SARINA{}x{}12 - AIC:{}'.formal(param, param_seasonal, aic))
            except:
                continue
                print('SARIMA{}x{}12 - AIC:{}'.format(best_order, best_seasonal_order, best_aic))
                return best_order, best_seasonal_order


model = SARIMAX(train, order=best_order, seasonal_order=best_seasonal_order)
sarima_final_model = model.fit(disp=0)
y_pred_test = sarima_final_model.get_forecast(steps=48)
y_pred = y_pred_test.predicted_mean
Y_pred = pd.Series(y_pred, index=traind.index)
plot_cow(train test, y_pred, "SARIMA")


#MAE'ye göre SARIMA
p = d = q = range(0,2)
pdq = list(itertools.product(p, d, q))
seasonal_pdq = [(x[0],x[1], x[2], 12]) for x in list(itertools.product(p, d,q))]
def sarima_optimizer_mee(train, pdq, seasonal_pdq):
    best_mae, best_order, best_seasonal_order = float("inf"), None, None
    for param in pdq:
        for param_seasonal in seasonal_pdq:
            try:
                model = SARIMAX(train, order=param, seasonal_order=param_seasonal)
                sarima_model = model.fit(disp=0)
                y_pred_test = sarima_model.get_forecast(steps=48)
                y_pred = y_pred_test.predicted_mean
                mae = mean_absolute_error(test, y-pred):
                if mae < best_mae:
                    best_mae, best_order, best_seasonal_order = mea, param, param_seasonal
                    print('SARINA{}x{}12 - MAE:{}'.formal(param, param_seasonal, mae))
            except:
                continue
                print('SARIMA{}x{}12 - MAE:{}'.format(best_order, best_seasonal_order, best_mae))
                return best_order, best_seasonal_order


df = pd.read_csv('path', index_col='month', parse_dates=True)

df[['column']].plt(title='başlık')
plt.show()


pd.DataFrame({'sales': df['sales']. values[0,10],
              "leg": df['sales'].shit(1).values[0,10],
              "leg2": df['sales'].shit(1).values[0,10],
              "leg3": df['sales'].shit(1).values[0,10],
              "leg4": df['sales'].shit(1).values[0,10]})

#hareketli ortalama
pd.DataFrame({"sales": df["sales"].values[0:10],
              "rol12": df["sales"].shift(1).rolling(windows=2).mean().values[0:10],
              "rol13": df["sales"].shift(1).rolling(windows=3).mean().values[0:10],
              "rol15": df["sales"].shift(1).rolling(windows=5).mean().values[0:10]})

def roll_mean_feature(daraframe, window):
    for window in windows:
        dataframe['sales_roll_mean_' + str(window)] = dataframe.groupby(["store", "item"])['sales'].\
            transform(lambda x: x.shift(1).rolling(window=window, win_periods=10, win_type="train").mean())
        return daraframe

    #üssel ağırlıklı ortalam

##############################################################################################################

import itertools
import warnings
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import mean_absolute_error
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.seasonal import seasonal_decompose
import statsmodels.tsa.api as smt
import seaborn as sns
import time
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX


df = pd.read_excel(r"/Users/serhatgulsu/Desktop/Time Series/Hit.xlsx", sheet_name="Genel")
pd.set_option('display.float_format', lambda x: '%.2f' % x)
df.head()
df.shape



train = df[:109]['Hit Ratio']
test = df[109:]['Hit Ratio']
train.tail()
test.head()

ses_model = SimpleExpSmoothing(train).fit(smoothing_level=0.5)
y_pred = ses_model.forecast(20)
mean_absolute_error(test, y_pred)
train.plot(title= 'Single Exponential Smoothing')
test.plot(label="Test")
y_pred.plot(label="PREDICTION")
train.plot(label="TTRAIN")
plt.legend()
plt.show()

tes_model = ExponentialSmoothing(train, trend="add", seasonal="add", seasonal_periods=12).fit(smoothing_level=0.5, smoothing_trend=0.5, smoothing_seasonal=0.5)
y_pred = tes_model.forecast(20)
test.plot(label="Test")
y_pred.plot(label="Prediction")
train.plot(label="Test")
plt.legend()
plt.show()

alphas = betas = gammas = np.arange(0.1, 1, 0.1)
abg = list(itertools.product(alphas, betas, gammas))

def TES_optimizer(train, abg, step=20):
    best_alpha, best_beta, best_gamma, best_mae = None, None, None, float("inf")
    for comb in abg:
        tes_model = ExponentialSmoothing(train, trend="add", seasonal="add", seasonal_periods=12).fit(smoothing_level=comb[0], smoothing_trend=comb[1], smoothing_seasonal=comb[2])
        y_pred = tes_model.forecast(step)
        mae = mean_absolute_error(test, y_pred)
        if mae < best_mae:
            best_alpha, best_beta, best_gamma, best_mae = comb[0], comb[1], comb[2], mae
            print("alpha", round(comb[0],2), "beta", round(comb[1], 2), "gamma", round(comb[2], 2),"mae", round(mae,2))
        print("best_alpha", round(best_alpha, 2), "best_beta", round(best_beta, 2), "best_gamma", round(best_gamma, 2), "best_mae", round(best_mae, 2))
            return best_alpha, best_beta, best_gamma, best_mae

best_alpha, best_beta, best_gamma, best_mae = TES_optimizer(train, abg)

model= ExponentialSmoothing(train, trend="add", seasonal="add", seasonal_periods=12).\
    fit(smoothing_level=best_alpha, smoothing_trend=best_beta, smoothing_seasonal=best_gamma)
y_pred = tes_model.forecast(20)
test.plot(label="Test")
y_pred.plot(label="Prediction")
train.plot(label="Train")
plt.legend()
plt.show()

#ARIMA
arima_model = SARIMAX(train, order=(12,1,12)).fit(disp=0)
y_pred = arima_model.forecast(20)
test.plot(label="Test")
y_pred.plot(label="Prediction")
train.plot(label="Train")
plt.legend()
plt.show()


pd.DataFrame({"Gerçek Deger": df["Hit Ratio"].values[0:10],
              "mean": df["Hit Ratio"].shift(1).rolling(window=2).mean().values[0:10],
              "ewm099": df["Hit Ratio"].shift(1).ewm(alpha=0.99).mean().values[0:10],
              "ewm095": df["Hit Ratio"].shift(1).ewm(alpha=0.95).mean().values[0:10],
              "ewm07": df["Hit Ratio"].shift(1).ewm(alpha=0.7).mean().values[0:10],
              "ewm02": df["Hit Ratio"].shift(1).ewm(alpha=0.2).mean().values[0:10]})

def ewm_features(dataframe, alphas, lags):
    for alpha in alphas:
        for lag in lags:
            dataframe['hit_ratio_ewm_alpha_' +str(alpha).replace(".", "") + "_lag_" + str(lag)] = \
                dataframe['Hit Ratio'].transform(lambda x: x.shift(lag).ewm(alpha=alpha).mean())
            return dataframe, alphas

alphas = [0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
lags = [1]

deneme2 = ewm_features(df, alphas, lags)
print(deneme2)

