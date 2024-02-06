import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
from SMC import meanSMCP, meanSMCI, a, b
from LMC import c, d, meanLMCI, meanLMCP

DistSMC = 62440
DistLMC = 49590

#results from LMC PL relations

def LMCdist(meanI, meanlogP):
    var1 = ((np.float64(c) * np.float64(meanlogP)) + np.float64(d))
    var2 = ((meanI) - var1) / 5
    var3 = 10 * 10 ** var2
    return(var3)

#print(LMCdist(meanSMCI, meanSMCP))

#results from SMC PL relations

def SMCdist(meanI, meanlogP):
    var1 = ((np.float64(a) * np.float64(meanlogP)) + np.float64(b))
    var2 = ((meanI) - var1) / 5
    var3 = 10 * 10 ** var2
    return(var3)



#results from GB PL relations


#result % error

def SMCperror(dist):
    print(dist)
    print(((dist - 62440) / 62440)*100)

def LMCperror(dist):
    print(dist)
    print(((dist - 49590) / 49590)*100)

SMCperror(SMCdist(meanLMCI, meanLMCP))
LMCperror(LMCdist(meanSMCI, meanSMCP))
