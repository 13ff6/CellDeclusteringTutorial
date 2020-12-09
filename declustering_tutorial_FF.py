


import geostatspy.geostats as geostat

import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


dataframe = pd.read_csv('Synthetic_Arsenic_Data_FF.csv')    


W, Csize, Dmean = geostat.declus(dataframe,'East','North','Arsenic',iminmax = 1, noff= 25, ncell=200,cmin=1,cmax=750)


