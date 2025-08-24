import itertools
numbers = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1]
target_sum = 1
number = 6
df = [c for c in itertools.product(numbers, repeat=number) if sum(c) == target_sum]
print(df)

import pandas as pd
permutation = pd.DataFrame(df, columns= ["w1", "w2", "w3", "w4", "w5", "w6"])
print(permutation)
permutation.shape


samples = pd.read_excel('/Users/serhatgulsu/Desktop/Değerler/konut1.xlsx', sheet_name='konut02575')
print(samples)

sample1 = samples.T
import numpy as np
expected = np.dot(permutation, sample1)


endekszammı = pd.read_excel('/Users/serhatgulsu/Desktop/Değerler/Konut1.xlsx', sheet_name='endeks02575')
print(endekszammı)
endekszammıt = endekszammı.T
skorezammı = (100/expected)
skorezammıfinal = (skorezammı)
endekszammıfinal = (1+endekszammı)
skorezammıfinal.shape
endekszammıfinal.shape

x = pd.DataFrame(skorezammıfinal)
y = pd.DataFrame(endekszammıfinal)
x.shape
y.shape

q = (np.matrix(x))
w = (np.matrix(y)).T
q.shape
w.shape
e = (np.multiply(q, w))
print(e)
e.shape

modelinHpTahmini = e*0.55
print(modelinHpTahmini)
modelinHpTahmini.shape

targetscore = pd.read_excel('/Users/serhatgulsu/Desktop/Değerler/konut1.xlsx', sheet_name='konuthp02575')

modelinHpTahmini.shape
targetscore.shape

target = np.matrix(targetscore).T
calculatedscore = np.matrix(modelinHpTahmini)

diff = np.mean(abs(target - calculatedscore), axis=1)

print(diff)
finalresult = diff
finalresult.shape

forappend = finalresult
permutation['diff'] = forappend
print(forappend)

permutation.shape
finalresult.shape
pd.set_option('display.float_format', lambda x: '%.4f'% x)
result = permutation.sort_values(by='diff', ascending=True)
print(result)

