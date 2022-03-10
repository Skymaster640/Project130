import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

print(df.columns)

df.drop(['Unnamed: 0','Unnamed: 6','Luminosity','Star_name.1','Distance.1','Mass.1','Radius.1'],axis=1,inplace=True)

finaldata= df.dropna()

finaldata.reset_index(drop=True,inplace=True)


print(finaldata.columns)


finaldata.to_csv("total_stars_final.csv")