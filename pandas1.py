import pandas as ps
data=ps.read_csv('studentdetail.csv')
dv=ps.DataFrame(data)
# print(dv)

print(data.tail(n=2))