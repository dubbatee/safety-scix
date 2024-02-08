import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics

DistSMC = 62440

pd.options.display.max_rows = 99999
dfsmc = pd.read_csv ('smcdata.csv')
dfsmc.columns =['ID', 'RA', 'Decl', 'I', 'P_1', 'dP_1', 'ID_OGLE_IV', 'REMARKS']

def DMSMC(Imag): 
    return(Imag - 5*np.log10(DistSMC/10))

def SMCP(p):
    return(np.log10(p))

absM = DMSMC(dfsmc['I'])
logP = SMCP(dfsmc['P_1'])

meanSMCP = statistics.mean(logP)
meanSMCI = statistics.mean(dfsmc['I'])


#plotting values using matplotlib

y = ((DMSMC(dfsmc['I'])).tolist())
x = ((SMCP(dfsmc['P_1'])).tolist())

plt.scatter(x, y)
a, b = np.polyfit(x, y, 1)
plt.xlabel('Log10 of Period(day)')
plt.ylabel('Abs I-band Mag')
LOBF = [i * a + b for i in x]
plt.plot(x, LOBF, color = "red")
plt.text(-0.8, 32, 'y = ' + format(a.round(2)) + 'x ' + format(b.round(2)))
plt.show()




