import pandas as pd
data=pd.read_csv('empdetail.csv')
df=pd.DataFrame(data)

#print(df)

print(data.head(n=3)) 