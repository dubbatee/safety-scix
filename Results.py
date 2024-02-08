import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
from SMC import meanSMCP, meanSMCI, a, b, dfsmc
from LMC import c, d, meanLMCI, meanLMCP, df

DistSMC = 62440
DistLMC = 49590

#results from LMC PL relations

def LMCdist(meanI, meanlogP):
    var1 = ((np.float64(c) * np.float64(meanlogP)) + np.float64(d))
    var2 = ((meanI) - var1) / 5
    var3 = 10 * 10 ** var2
    return(var3)


def LMCdist2(I, P):
    var1 = ((np.float64(a) * np.float64(np.log10(P))) + np.float64(b))
    var2 = ((I) - var1) / 5
    var3 = 10 * 10 ** var2
    return var3

dfsmc['dists'] = LMCdist2(dfsmc['I'], dfsmc['P_1'])
meanSMCdist = statistics.mean(dfsmc['dists'])


#results from SMC PL relations

def SMCdist(meanI, meanlogP):
    var1 = ((np.float64(a) * np.float64(meanlogP)) + np.float64(b))
    var2 = ((meanI) - var1) / 5
    var3 = 10 * 10 ** var2
    return(var3)

def SMCdist2(I, P):
    var1 = ((np.float64(a) * np.float64(np.log10(P))) + np.float64(b))
    var2 = ((I) - var1) / 5
    var3 = 10 * 10 ** var2
    return var3

df['dists'] = SMCdist2(df['I'], df['P_1'])
meanLMCdist = statistics.mean(df['dists'])



#results from GB PL relations


#result % error

def SMCperror(dist):
    print(dist)
    print(((dist - 62440) / 62440)*100)

def LMCperror(dist):
    print(dist)
    print(((dist - 49590) / 49590)*100)



SMCperror(meanSMCdist)  #distance + error of the average calculated SMC distances
LMCperror(meanLMCdist)  #distance + error of the average calculated LMC distances
print(SMCperror(LMCdist(meanSMCI, meanSMCP))
print(SMCperror(SMCdist(meanLMCI, meanLMCP))

