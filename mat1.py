from matplotlib import pyplot as plt

sem=[]
s1=int(input("enter the sem"))
sem.append(s1)
s2=int(input("enter the sem"))
sem.append(s2)
s3=int(input("enter the sem"))
sem.append(s3)
s4=int(input("enter the sem"))
sem.append(s4)
mark=[]
m1=int(input("enter the mark"))
mark.append(m1)
m2=int(input("enter the mark"))
mark.append(m2)
m3=int(input("enter the mark"))
mark.append(m3)
m4=int(input("enter the mark"))
mark.append(m4)


plt.xlabel("sem")
plt.ylabel("mark")
plt.plot(sem,mark)
plt.show()