import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.ticker import MultipleLocator,NullFormatter,FuncFormatter
import seaborn as sns
from data_cleaning import data__particles_per_quad
#data__particles_per_quad = pd.read_excel("./oahu_windward_beaches_microplastics_survey.xlsx",sheet_name="Particles per Quad")
#data__sand_mass = pd.read_excel("./oahu_windward_beaches_microplastics_survey.xlsx",sheet_name="Sand Mass")
#data__beach_location = pd.read_excel("./oahu_windward_beaches_microplastics_survey.xlsx",sheet_name="Beach Location")
#data__percent_particles_per_size_class = pd.read_excel("./oahu_windward_beaches_microplastics_survey.xlsx",sheet_name="Percent Particles per Size Clas")


bins = np.arange(0,3501,50)
#for i,b in enumerate(sorted(list(set(data__particles_per_quad["Beach"].to_numpy())))):
    
    #plt.hist("plastics per quadrat (0.09m square)",bins=bins,data=data__particles_per_quad[(data__particles_per_quad["Tide"].isin(["high"])) & (data__particles_per_quad["Beach"].isin([b]))],label=b,edgecolor='black')
    #plt.hist("plastics per quadrat (0.09m square)",bins=np.arange(0,3501,50),data=data__particles_per_quad[(data__particles_per_quad["Tide"].isin(["high"])) & (data__particles_per_quad["Beach"].isin([b]))],label=b)
    #plt.hist("plastics per quadrat (0.09m square)",bins=np.arange(0,3501,50),data=data__particles_per_quad[(data__particles_per_quad["Tide"].isin(["high"])) & (data__particles_per_quad["Beach"].isin([b]))],label=b)
    #plt.hist("plastics per quadrat (0.09m square)",bins=np.arange(0,3501,50),data=data__particles_per_quad[(data__particles_per_quad["Tide"].isin(["high"])) & (data__particles_per_quad["Beach"].isin([b]))],label=b)
    #plt.hist("plastics per quadrat (0.09m square)",bins=np.arange(0,3501,50),data=data__particles_per_quad[(data__particles_per_quad["Tide"].isin(["high"])) & (data__particles_per_quad["Beach"].isin([b]))],label=b)
    #plt.hist("plastics per quadrat (0.09m square)",bins=np.arange(0,3501,50),data=data__particles_per_quad[(data__particles_per_quad["Tide"].isin(["high"])) & (data__particles_per_quad["Beach"].isin([b]))],label=b)
    #plt.hist("plastics per quadrat (0.09m square)",bins=np.arange(0,3501,50),data=data__particles_per_quad[(data__particles_per_quad["Tide"].isin(["high"])) & (data__particles_per_quad["Beach"].isin([b]))],label=b)

for t in sorted(list(set(data__particles_per_quad["Tide"].to_numpy()))):
    #sns.histplot(data=data__particles_per_quad[(data__particles_per_quad["Tide"].isin([t]))],x="plastics per quadrat (0.09m square)", bins=bins,hue="Beach",multiple="dodge",palette="Set1",edgecolor='black')#, color="#93A8BF")
    fig,ax = plt.subplots()
    sns.scatterplot(data=data__particles_per_quad[(data__particles_per_quad["Tide"].isin([t]))],x="Beach",y="plastics per quadrat (0.09m square)",ax=ax,hue="Beach",palette="Set1")
    #ticks = np.arange(0,4_000,100)
    #y_ticks = np.arange(0,4_000,100)
    ax.yaxis.set_major_locator(MultipleLocator(200))
    ax.yaxis.set_minor_locator(MultipleLocator(50))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x,pos:f"{x/100:,.0f}"))
    ax.yaxis.set_minor_formatter(NullFormatter())
    ax.tick_params(axis='y',which='major',length=7)
    ax.tick_params(axis='y',which='minor',length=3)
    #plt.xticks(ticks,[f"{x/100:,.0f}" for x in ticks])
    #plt.yticks(y_ticks,[f"{x/100:,}" for x in y_ticks])
    #plt.xlabel("plastics per quadrat (0.09m square)\n(in 100s)")
    plt.title(f"Distribution of Plastic Counts by Beach at {t} Tide\nI")
    #plt.legend()
    plt.savefig(f"Distribution of Plastic Counts at {t} Tide by Beach.png",dpi=300, bbox_inches="tight")
    #plt.show()
'''fig,ax = plt.subplots()
    
#for t in sorted(list(set(data__particles_per_quad["Tide"].to_numpy()))):
    #sns.histplot(data=data__particles_per_quad[(data__particles_per_quad["Tide"].isin([t]))],x="plastics per quadrat (0.09m square)", bins=bins,hue="Beach",multiple="dodge",palette="Set1",edgecolor='black')#, color="#93A8BF")
sns.scatterplot(data=data__particles_per_quad,x="Beach",y="plastics per quadrat (0.09m square)",ax=ax,hue="Tide",palette="Set1")
ax.yaxis.set_major_locator(MultipleLocator(200))
ax.yaxis.set_minor_locator(MultipleLocator(50))
ax.yaxis.set_minor_formatter(NullFormatter())
ax.yaxis.set_major_formatter(FuncFormatter(lambda x,pos:f"{x/100:,.0f}"))
ax.tick_params(axis='y',which='major',length=7)
ax.tick_params(axis='y',which='minor',length=3)
    #ticks = np.arange(0,4_000,100)
#y_ticks = np.arange(0,4_000,100)
    #plt.xticks(ticks,[f"{x/100:,.0f}" for x in ticks])
#plt.yticks(y_ticks,[f"{x/100:,.0f}" for x in y_ticks])
plt.ylabel(f"plastics per quadrat (0.09m square)\nin 100s")
#plt.xlabel("Beach")
plt.title(f"Distribution of Plastic Counts by Beach and Tide")
#plt.legend()
plt.savefig(f"Distribution of Plastic Counts by Beach and Tide.png",dpi=300, bbox_inches="tight")
#plt.show()'''

'''for b in sorted(list(set(data__particles_per_quad["Beach"].to_numpy()))):
    sns.scatterplot(data=data__particles_per_quad[data__particles_per_quad["Beach"]==b],x="Beach",y="plastics per quadrat (0.09m square)",hue="Tide",palette="Set1")
    y_ticks = np.arange(0,4_000,100)
    #plt.xticks(ticks,[f"{x/100:,.0f}" for x in ticks])
    plt.yticks(y_ticks,[f"{x/100:,.0f}" for x in y_ticks])
    plt.ylabel(f"plastics per quadrat (0.09m square)\nin 100s")
    #plt.xlabel("Beach")
    plt.title(f"Distribution of Plastic Counts at {b} Beach")
    #plt.legend()
    plt.savefig(f"Distribution of Plastic Counts at {b} Beach.png",dpi=300, bbox_inches="tight")
    #plt.show()'''