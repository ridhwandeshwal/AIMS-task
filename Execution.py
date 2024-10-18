import pandas as pd
import numpy as np
from OneHot_Encoder import OneHotEncoder
from Ordinal_Encoder import OrdinalEncoder

trial=pd.read_csv('trial.csv')

print(trial,"\n")

ohe=OneHotEncoder()
trial_ohe=ohe.fit_transform(trial)
print(trial_ohe,"\n")

oe=OrdinalEncoder()
trial_oe=oe.fit_transform(trial)
print(trial_oe,"\n")

