import numpy as np
import pandas as pd

from root.riskutil import woeInfoValue
from root.riskutil import mysqlDemo


# print(woeInfoValue.woe_single_x(pd.Series(mysqlDemo.getlist1("X1")), np.array(mysqlDemo.getlist2())))

y = np.array([0, 1, 1, 0, 1, 0, 1])
a = np.array([2, 3, 4, 31, 20, 2, 40])
# y = numpy.array([1,1,0,0])
# for a1 in a:
#     print(y[numpy.where(a1 == 30)[0]])
b = np.array([2, 31, 4, 6])

c = np.array(0)

for b1 in b:
    c = np.append(c, np.where(a == b1))

print(c)
c = np.unique(c)
y[c]
print(y[c])