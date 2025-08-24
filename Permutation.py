import itertools
numbers = [0, 0.02, 0.04, 0.08, 0.16, 0.20,
         0.24, 0.28, 0.32, 0.36, 0.40, 0.44,
        0.48, 0.52, 0.56, 0.60, 0.64, 0.68,
         0.72, 0.76, 0.80, 0.84, 0.88, 0.92, 0.94, 0.96, 1]
target_sum = 1
number = 6
df = [c for c in itertools.product(numbers, repeat=number) if sum(c) == target_sum]
print(df)

import pandas as pd
permutation = pd.DataFrame(df, columns= ["w1", "w2", "w3", "w4", "w5", "w6"])
print(permutation)

samples = pd.read_excel('/Users/serhatgulsu/Desktop/Değerler/Values - asof22107.xlsx', sheet_name='HOzel0')
print(samples)

sample1 = samples.T
print(sample1)
import numpy as np
expected = np.dot(permutation, sample1)
print(expected)

targetscore = pd.read_excel('/Users/serhatgulsu/Desktop/Değerler/Targets - asof202107.xlsx', sheet_name='HOzel0')
print(targetscore)

expected.shape
targetscore.shape

expectedt = expected.T


diff = np.abs(np.array(expectedt) - np.array(targetscore))
print(diff)

diff.shape

difft= diff.T

finalresult = sum(diff)
print(finalresult)

forappend = finalresult
print(forappend)

forappend.shape

appendt = forappend.T

permutation['diff'] = np.array(forappend)
print(permutation)

result = permutation.sort_values(by='diff', ascending=True)
print(result)

