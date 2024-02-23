import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
#from LMC import logPLMC

DistSMC = 62440

pd.options.display.max_rows = 99999
dfsmc = pd.read_csv ('smcdata.csv')
dfsmc.columns =['ID', 'RA', 'Decl', 'I', 'P_1', 'dP_1', 'ID_OGLE_IV', 'REMARKS']

def DMSMC(Imag): 
    return(Imag - 5*np.log10(DistSMC/10))

def SMCP(p):
    return(np.log10(p))

absMSMC = DMSMC(dfsmc['I'])
logPSMC = SMCP(dfsmc['P_1'])

dfsmc['absM'] = absMSMC
dfsmc['logP'] = logPSMC

meanSMCP = statistics.mean(logPSMC)
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

#bolometric correction calculations

#bolometric corrections in the I-Band

bc = 0

def Mbol(M):
    return (bc + M)

dfsmc['Mbol'] = Mbol(dfsmc['absM'])

def SMCmbol(Mbol):
    return ((Mbol + (5*np.log10(DistSMC/10))))

dfsmc['mbol'] = SMCmbol(dfsmc['Mbol'])
#print(dfsmc['mbol'])
#print(dfsmc['I'])

z = ((DMSMC(dfsmc['mbol'])).tolist())
w = ((SMCP(dfsmc['P_1'])).tolist())

plt.scatter(w, z)
g, h = np.polyfit(w, z, 1)
plt.xlabel('Log10 of Period(day)')
plt.ylabel('Abs I-band Mag')
LOBF = [i * g + h for i in w]
plt.plot(w, LOBF, color = "red")
plt.text(-0.8, 32, 'y = ' + format(g.round(2)) + 'x ' + format(h.round(2)))
plt.show()
#print(a, b)
#print(g, h)

def bolodistsmc(mbol, logP):
    var1 = (((-2.3571554842287554) * logP) + -0.9260058642992806)
    var2 = ((mbol) - var1) / 5
    var3 = 10 * 10 ** var2
    return statistics.median(var3)

print(bolodistsmc(dfsmc['mbol'], logPSMC))


