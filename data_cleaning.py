import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns



data__particles_per_quad = pd.read_excel("./oahu_windward_beaches_microplastics_survey.xlsx",sheet_name="Particles per Quad")
data__sand_mass = pd.read_excel("./oahu_windward_beaches_microplastics_survey.xlsx",sheet_name="Sand Mass")
data__beach_location = pd.read_excel("./oahu_windward_beaches_microplastics_survey.xlsx",sheet_name="Beach Location")
data__percent_particles_per_size_class = pd.read_excel("./oahu_windward_beaches_microplastics_survey.xlsx",sheet_name="Percent Particles per Size Clas")
'''
#print(data__particles_per_quad)

# Exploratory Visuals
## Microplastic Abundance

data__particles_per_quad_groupby_beach_tide = data__particles_per_quad.groupby(["Beach","Tide"],as_index=False)["plastics per quadrat (0.09m square)"].agg(mean="mean",median='median',n='count',total='sum').sort_values(by=["Beach","Tide"],ascending=False)
data__particles_per_quad_groupby_beach = data__particles_per_quad.groupby(["Beach"],as_index=False)["plastics per quadrat (0.09m square)"].agg(mean="mean",median='median',n='count',total='sum').sort_values(by=["Beach"],ascending=False)

print(data__particles_per_quad_groupby_beach_tide)

bars_total = plt.bar(np.arange(1,7),"total",data=data__particles_per_quad_groupby_beach)
bars_high = plt.bar(np.arange(1,7),"total",label="High Tide",data=data__particles_per_quad_groupby_beach_tide[data__particles_per_quad_groupby_beach_tide["Tide"].isin(["high"])],color="#2D7BC8")
storm_starts = data__particles_per_quad_groupby_beach_tide["total"][data__particles_per_quad_groupby_beach_tide["Tide"].isin(["high"])].to_numpy()
bars_storm = plt.bar(np.arange(1,7),"total",label="Storm Tide",bottom=storm_starts,data=data__particles_per_quad_groupby_beach_tide[~data__particles_per_quad_groupby_beach_tide["Tide"].isin(["high"])],color="#26B481")
plt.bar_label(bars_storm,label_type="center",fmt='{:,.0f}')#,data__particles_per_quad_groupby_beach_tide.index.to_numpy())
plt.bar_label(bars_high,label_type="center",fmt='{:,.0f}')#,data__particles_per_quad_groupby_beach_tide.index.to_numpy())
plt.bar_label(bars_total,label_type="edge",fmt="{:,.0f}")
plt.title("Total Particles by Beach")
plt.legend()
plt.xticks(np.arange(1,7),sorted(list(set(data__particles_per_quad_groupby_beach["Beach"].to_numpy())),reverse=True))
plt.show()'''

'''
## Distribution
data__percent_particles_per_size_class = data__percent_particles_per_size_class.sort_values(by=["Beach","Tide"],ascending=False)
print(data__percent_particles_per_size_class)
high_large = plt.bar(np.arange(10,250,40),"4-5 mm",width=10,label="4-5mm",data=data__percent_particles_per_size_class[data__percent_particles_per_size_class["Tide"].isin(['high'])])
high_med_start = data__percent_particles_per_size_class["4-5 mm"][data__percent_particles_per_size_class["Tide"].isin(['high'])].to_numpy()
high_med = plt.bar(np.arange(10,250,40),"2-4 mm",bottom=high_med_start,width=10,label="2-4mm",data=data__percent_particles_per_size_class[data__percent_particles_per_size_class["Tide"].isin(['high'])])
high_small_start = data__percent_particles_per_size_class["2-4 mm"][data__percent_particles_per_size_class["Tide"].isin(['high'])].to_numpy().__add__(high_med_start)
high_small = plt.bar(np.arange(10,250,40),"0.5-2 mm",bottom=high_small_start,width=10,label="0.5-2mm",data=data__percent_particles_per_size_class[data__percent_particles_per_size_class["Tide"].isin(['high'])])

low_large = plt.bar(np.arange(30,270,40),"4-5 mm",width=10,label="4-5mm",data=data__percent_particles_per_size_class[data__percent_particles_per_size_class["Tide"].isin(['low'])])
low_med_start = data__percent_particles_per_size_class["4-5 mm"][data__percent_particles_per_size_class["Tide"].isin(['low'])].to_numpy()
low_med = plt.bar(np.arange(30,270,40),"2-4 mm",bottom=low_med_start,width=10,label="2-4mm",data=data__percent_particles_per_size_class[data__percent_particles_per_size_class["Tide"].isin(['low'])])
low_small_start = data__percent_particles_per_size_class["2-4 mm"][data__percent_particles_per_size_class["Tide"].isin(['low'])].to_numpy().__add__(low_med_start)
low_small = plt.bar(np.arange(30,270,40),"0.5-2 mm",bottom=low_small_start,width=10,label="0.5-2mm",data=data__percent_particles_per_size_class[data__percent_particles_per_size_class["Tide"].isin(['low'])])



plt.bar_label(high_large,label_type="center")
plt.bar_label(low_large,label_type="center")
plt.bar_label(high_med,label_type="center")
plt.bar_label(low_med,label_type="center")
plt.bar_label(high_small,label_type="center")
plt.bar_label(low_small,label_type="center")
plt.legend()
plt.xticks(np.arange(20,260,40),sorted(list(set([f" |High|{x}|Low| " for x in data__percent_particles_per_size_class["Beach"].to_numpy()])),reverse=True))
#plt.xticks(np.arange(1.5,7.5,1),['Low']*6)
for x in np.arange(4,270,40):
    plt.axvline(x,ymin=0,ymax=80,linestyle='--',color='black')
plt.show()
'''




