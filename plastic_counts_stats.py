import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from data_cleaning import data__particles_per_quad


print(data__particles_per_quad)

data_groupby_beach_tide = data__particles_per_quad.groupby(["Beach",'Tide']).agg(variance=('plastics per quadrat (0.09m square)',np.var)).reset_index()

print(data_groupby_beach_tide)


data_groupby_beach = data__particles_per_quad.groupby(["Beach"]).agg(variance=('plastics per quadrat (0.09m square)',np.var)).reset_index()

print(data_groupby_beach)


with pd.ExcelWriter("./Plastic Counts Variance.xlsx",engine='openpyxl',mode='w') as writer:
    data_groupby_beach_tide.to_excel(writer,sheet_name="Partitioned By Beach and Tide",index=False)
    data_groupby_beach.to_excel(writer,sheet_name="Partitioned By Beach",index=False)