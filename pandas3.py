import pandas as pd
data=pd.read_csv('stafflist.csv')
df=pd.DataFrame(data)
#print(df)
print(data.tail(n=2)) 