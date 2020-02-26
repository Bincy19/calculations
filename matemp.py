from matplotlib import pyplot as plt

empid=[]
e1=int(input("enter the empid"))
empid.append(e1)
e2=int(input("enter the empid"))
empid.append(e2)
e3=int(input("enter the empid"))
empid.append(e3)
e4=int(input("enter the empid"))
empid.append(e4)
salary=[]
s1=int(input("enter the salary"))
salary.append(s1)
s2=int(input("enter the salary"))
salary.append(s2)
s3=int(input("enter the salary"))
salary.append(s3)
s4=int(input("enter the salary"))
salary.append(s4)
plt.xlabel("empid")
plt.ylabel("salary")
plt.plot(empid,salary)
plt.show()