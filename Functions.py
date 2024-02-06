import numpy as np

#Distances to the Galactic Bulge, Small Megallanic Cloud, Large Megallanic Cloud --- GB, SMC, LMC {parsecs}

DistSMC = 62440
DistLMC = 49590

#Distance MODULUS for SMC Delta Scuti - uses log(Period) and I mag of delta scuti variables in SMC to derive linear relationship, 
#average logP of BG and LMC delta scuti variables plugged into the derived relationship to calculate the average absolute magnitude M, which is then plugged into the Distance MODULUS (alongside average Imag) to calculate the distance

def DMSMC(Imag): 
    print(Imag + 5*np.log10(DistSMC/10))

def DMLMC(Imag): 
    print(Imag + 5*np.log10(DistLMC/10))

