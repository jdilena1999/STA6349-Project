import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
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

for b in sorted(list(set(data__particles_per_quad["Beach"].to_numpy()))):
    #for t in sorted(list(set(data__particles_per_quad["Tide"].to_numpy()))):    
    fig,ax = plt.subplots()    
    sns.histplot(data=data__particles_per_quad[(data__particles_per_quad["Beach"].isin([b]))],x="plastics per quadrat (0.09m square)", 
                 bins=bins,hue="Tide",multiple="dodge",palette="Set1",edgecolor='black')#, color="#93A8BF")

    ticks = np.arange(0,4_000,100)
    y_ticks = np.arange(0,10)
    plt.xticks(ticks,[f"{x/100:,.0f}" for x in ticks])
    plt.yticks(y_ticks,[f"{x:,}" for x in y_ticks])
    plt.xlabel("plastics per quadrat (0.09m square)\n(in 100s)")
    plt.title(f"Distribution of Plastic Counts for {b} Beach")
    #plt.legend()
    #plt.savefig(f"plastics_hist_{b}_High_vs_Storm.png", dpi=300, bbox_inches="tight")
    plt.show()