import pandas as pd
import numpy as np
import matplotlib.pyplot as mat
import statistics



DistLMC = 49590

pd.options.display.max_rows = 99999
df = pd.read_csv ('lmcdata.csv')
df.columns =['ID', 'RA', 'Decl', 'I', 'P_1', 'dP_1', 'ID_OGLE_IV', 'REMARKS']

def DMLMC(I): 
    return(I + 5*np.log10(DistLMC/10))

def LMCP(p):
    return(np.log10(p))

absM = DMLMC(df['I'])
logP = LMCP(df['P_1'])

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

