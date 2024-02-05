import pandas as pd
import numpy as np
import matplotlib as mat

pd.options.display.max_rows = 99999
df = pd.read_csv ('gbdata.csv')
df.columns =['ID', 'RA', 'Decl', 'I', 'P_1', 'dP_1', 'ID_OGLE_IV', 'REMARKS']
print(df.head(10))