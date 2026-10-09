import pandas as pd
import bambi as bmb
import arviz as az
import matplotlib.pyplot as plt
import numpy as np

priors = {
    "Intercept":bmb.Prior("Normal",mu=5_000,sigma=1_000),
    "temp_feel":bmb.Prior("Normal",mu=100,sigma=40),
    "sigma":bmb.Prior("Exponential",lam=0.0008)

}

data = pd.read_csv("bikes.csv")

model = bmb.Model("rides ~ temp_feel",data=data,family="gaussian",priors=priors)
inference_data = model.fit(draws = 5_000*2,chains=4,random_seed=84735)
print(az.summary(inference_data,hdi_prob=0.95))
intercept_examples = az.extract(inference_data,var_names="Intercept").values
x1_examples = az.extract(inference_data,var_names="temp_feel").values
sigma_examples = az.extract(inference_data,var_names="sigma").values
intercept_split = intercept_examples.reshape(4,-1)
x1_split = x1_examples.reshape(4,-1)
sigma_split = sigma_examples.reshape(4,-1)

for t,n in zip([intercept_split,x1_split,sigma_split],["Intercept",'temp_feel','sigma']):
    for i,row in enumerate(t):
        plt.plot(np.arange(1,5001),row[5_000:],label=f"Chain {i}")
        mean = row[5_000:].mean()
        plt.axhline(mean,xmin=0,xmax=5_000,linestyle='--')
    plt.title(f"{n} Chains")
    plt.show()



