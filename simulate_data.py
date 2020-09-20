import pandas as pd
import numpy as np

data = pd.read_csv('C:\\Users\\5stev\\Downloads\\generic_time.csv')
draws =  np.round(np.random.normal(25, 2, 44))
draws.astype(int)
data['Count'] = pd.Series(draws)
data.to_csv('C:\\Users\\5stev\\Downloads\\monday.csv')
