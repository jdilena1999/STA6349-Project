import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
from data_cleaning import data__particles_per_quad
from matplotlib.ticker import MultipleLocator,NullFormatter,FuncFormatter


print(data__particles_per_quad)

data_groupby_beach_tide = data__particles_per_quad.groupby(["Beach",'Tide']).agg(variance=('plastics per quadrat (0.09m square)',np.var)).reset_index()

print(data_groupby_beach_tide)


data_groupby_beach = data__particles_per_quad.groupby(["Beach"]).agg(variance=('plastics per quadrat (0.09m square)',np.var)).reset_index()

print(data_groupby_beach)

fig,ax = plt.subplots()
sns.barplot(data=data_groupby_beach_tide,x="Beach",y="variance",hue="Tide",ax=ax)
for container in ax.containers:
    ax.bar_label(
        container,
        fmt=lambda x: f"{x:,.0f}",
        padding=3
    )
ax.yaxis.set_major_locator(MultipleLocator(100_000))
ax.yaxis.set_minor_locator(MultipleLocator(25_000))
ax.yaxis.set_minor_formatter(NullFormatter())
ax.yaxis.set_major_formatter(FuncFormatter(lambda x,pos:f"{x/10_000:,.0f}"))


#plt.savefig("Plastic Counts Variance by Beach and Tide.png",dpi=300, bbox_inches="tight")
#plt.show()

fig,ax = plt.subplots()
sns.barplot(data= data_groupby_beach,x="Beach",y='variance',ax=ax)
for container in ax.containers:
    plt.bar_label(
        container,
        fmt=lambda x:f"{x:,.0f}",
        padding=3
    )
ax.yaxis.set_major_locator(MultipleLocator(100_000))
ax.yaxis.set_minor_locator(MultipleLocator(25_000))
ax.yaxis.set_minor_formatter(NullFormatter())
ax.yaxis.set_major_formatter(FuncFormatter(lambda x,pos:f"{x/10_000:,.0f}"))
#plt.savefig("Plastic Counts Variance by Beach.png",dpi=300, bbox_inches="tight")
#plt.show()

'''with pd.ExcelWriter("./Plastic Counts Variance.xlsx",engine='openpyxl',mode='w') as writer:
    data_groupby_beach_tide.to_excel(writer,sheet_name="Partitioned By Beach and Tide",index=False)
    data_groupby_beach.to_excel(writer,sheet_name="Partitioned By Beach",index=False)'''