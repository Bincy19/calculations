from matplotlib import pyplot as plt 
x=[1990,1995,2000,2005,2010,2015,2020]
y=[1000,1750,3000,4000,7500,15000,30000]


plt.xlabel("year")
plt.ylabel("income")

plt.plot(x,y)
plt.show()