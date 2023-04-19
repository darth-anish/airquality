import pandas as pd
import numpy as np 

airquality_df = pd.read_csv('airquality.csv')
sites_df = pd.read_csv('sites.csv')

merged_df = airquality_df.merge(sites_df,how='left',on='site')
merged_df.to_csv('data/merged.csv')