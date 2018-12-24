import numpy
import pandas as pd

from root.riskutil import woeInfoValue
from root.riskutil import mysqlDemo

a = 1
while(a <= 20):
    woe_dict, iv, event_percent = woeInfoValue.woe_single_x(mysqlDemo.getlist1("X" + str(a)), numpy.array(mysqlDemo.getlist2("X" + str(a))))
    print(event_percent)
    woeInfoValue.plot_woe(event_percent)
    a = a+1
