import numpy as np
import pandas as pd

class OneHotEncoder():
    def __init__(self):
        pass

    def fit(self, df:pd.DataFrame):
        self.categorical_cols=[x for x in df.columns if df[x].dtype == "object"]
        self.dict={}
        for x in self.categorical_cols:
            uniquevals=[a for a in df[x].unique()]
            self.dict[x]=uniquevals
    
    def transform(self, df:pd.DataFrame):
        for col in self.dict:
            for unqval in dict[col]:
                for row in range(len(df[col])):
                    if df.loc[row, col] == unqval:
                        df.loc[row, unqval]=1
                    else:
                        df.loc[row,unqval]=0
        df.drop(self.categorical_cols,axis=1,inplace=True)
        return df
    
    def fit_transform(self, df:pd.DataFrame):
        self.fit(df)
        return self.transform(df)