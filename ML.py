import pandas as pd
from sklearn.preprocessing import RobustScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix, classification_report, plot_roc_curve

def outlier_threshold(df, col_name, q1=0.05, q3=0.95):
    quartile1= df[col_name].quantile(q1)
    quartile3= df[col_name].quantile(q3)
    interquantile_range= quartile3 - quartile1
    up_limit = quartile3 + 1.5*interquantile_range
    low_limit = quartile1 - 1.5 * interquantile_range
    return low_limit, up_limit

def check_outlier(df, col_name):
def replace_with_threshold(df, variable)

# virgülden sonra basamak ayarı:
pd.set_option('display.float_format', lambda x: '%.3f'% x)

#lojistik regresyon

y = df["x"]
x = df.drop([])

log_model = LogisticRegression().fit(x, y)
log_normal.intercept_
log_model.coef_

y_pred = log_model.predict(x)

def plot_confusion_matrix(y, y_pred)
    plt.xlabel('y_pred')
    plt.ylabel('y')
    plt.title('Accuracy Score: {0}'format(acc), size=10)
    plt.show()

#Model Validation: Holdout

x_train, X_test, y_train, y_test = train_test_split(X,
                                                    y,test_size=0.20, random_state=17)


#KNN
x_scaled = StandardScaler().fit_transform(x)
x = pd.DataFrame(x_scaled, columns=X.columns)

knn_model = KNeighborsClassifier().fit(x,y)
random_user = X.sample(1, random_state=45)
knn_model.predict(random_user)

y_pred = knn_model.predit(x)
y_prob = knn_modekçoredşct_proba(y, y_pred)

#CART

