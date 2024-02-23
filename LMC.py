import pandas as pd
import numpy as np
import matplotlib.pyplot as mat
import statistics
from SMC import dfsmc, g, h


DistLMC = 49590

pd.options.display.max_rows = 99999
df = pd.read_csv ('lmcdata.csv')
df.columns =['ID', 'RA', 'Decl', 'I', 'P_1', 'dP_1', 'ID_OGLE_IV', 'REMARKS']

def DMLMC(I): 
    return(I - 5*np.log10(DistLMC/10))

def LMCP(p):
    return(np.log10(p))

absMLMC = DMLMC(df['I'])
logPLMC = LMCP(df['P_1'])

df['absM'] = absMLMC
df['logP'] = logPLMC

meanLMCP = statistics.mean(logPLMC)
meanLMCI = statistics.mean(df['I'])


#plotting values using matplotlib

y = ((DMLMC(df['I'])).tolist())
x = ((LMCP(df['P_1'])).tolist())

mat.xlabel('Log10 of Period')
mat.ylabel('Absolute I-Band Magntude')

mat.scatter(x, y)
c, d = np.polyfit(x, y, 1) 
mat.xlabel('Log10 of Period(day)')
mat.ylabel('Abs I-band Mag')
LOBF = [i * c + d for i in x]
mat.plot(x, LOBF, color = "red")
mat.text(-0.8, 32, 'y = ' + format(c.round(2)) + 'x ' + "+ " + format(d.round(2)))
mat.show()


#bolometric correction calculations


bc = 0

def Mbol(M):
    return (bc + M)

df['Mbol'] = Mbol(df['absM'])

def LMCmbol(Mbol):
    return ((Mbol + (5*np.log10(DistLMC/10))))

df['mbol'] = LMCmbol(df['Mbol'])

#print(df['absM'])
#print(df['Mbol'])
#print(df['mbol'])

z = ((DMLMC(df['mbol'])).tolist())
w = ((LMCP(df['P_1'])).tolist())

mat.scatter(w, z)
e, f = np.polyfit(w, z, 1)
mat.xlabel('Log10 of Period(day)')
mat.ylabel('Abs I-band Mag')
LOBF = [i * e + f for i in w]
mat.plot(w, LOBF, color = "red")
mat.text(-0.8, 32, 'y = ' + format(e.round(2)) + 'x ' + format(f.round(2)))
mat.show()

print(c, d)
print(e, f)

def bolodistlmc(mbol, logP):
    var1 = (((g) * logP) + h)
    var2 = ((mbol) - var1) / 5
    var3 = 10 * 10 ** var2
    return statistics.mean(var3)

print(bolodistlmc(df['mbol'], LMCP(dfsmc['P_1'])))
