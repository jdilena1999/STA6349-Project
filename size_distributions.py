import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.ticker import MultipleLocator,NullFormatter,FuncFormatter
import seaborn as sns
from data_cleaning import data__percent_particles_per_size_class

data = data__percent_particles_per_size_class.melt(["Beach",'Tide'])
data.rename(columns={"variable":"Size","value":"Percent"},inplace=True)
data.sort_values(by=["Beach","Tide"],inplace=True)
data.reset_index()
print(data)

fig,ax = plt.subplots()

sns.barplot(data=data,x="Beach",y="Percent",hue="Size",errorbar=None)
plt.title("Particle Size Distributions by Beach")
ax.yaxis.set_major_locator(MultipleLocator(10))
ax.yaxis.set_minor_locator(MultipleLocator(5))
ax.yaxis.set_major_formatter(FuncFormatter(lambda x,pos:f"{x:,.0f}%"))
ax.yaxis.set_minor_formatter(NullFormatter())
plt.savefig("Particle Size Distributions by Beach.png",dpi=300, bbox_inches="tight")
plt.show()