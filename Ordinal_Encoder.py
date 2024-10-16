import numpy as np
import pandas as pd

class OrdinalEncoder():
    def __init__(self):
        pass
    
    def fit(self,df:pd.DataFrame):
        categorical_cols=[x for x in df.columns if df[x].dtype=="object"]
        self.dict={}
        for x in categorical_cols:
            d={}
            for a,b in enumerate(df[x].unique()):
                d[b]=a
            self.dict[x]=d

    def transform(self,df:pd.DataFrame):
        for x in self.dict.keys():
            df[x]=df[x].apply(lambda a: self.dict[x][a])
        return df
    
    def fit_transform(self,df:pd.DataFrame):
        self.fit(df)
        return self.transform(df)
    
    