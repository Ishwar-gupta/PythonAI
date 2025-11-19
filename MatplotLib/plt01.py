"""import matplotlib.pyplot as plt
x=['sun','mon','tue','wed','thu','fri','sat']
y=[10,20,5,25,15,45,23]
plt.plot(x,y)
plt.title("total sales ")
plt.xlabel("Days of the week")
plt.ylabel('Total sales per day')
plt.grid("True")
plt.show()"""

import matplotlib.pyplot as plt
months=[1,2,3,4]
sales=[1000,1500,1200,1800]
plt.title("Monthly Sales Data Report")
plt.grid("True",color='gray',linestyle=':',linewidth=1)
plt.plot(months,sales,color='blue',linewidth=2,linestyle='--',marker='o',label='2025 Sales data')
plt.legend(loc='upper left',fontsize=10)  # it will work iff label attr is used in plot method
plt.xlabel("Months")
plt.ylabel("Sales per month")
plt.xlim(1,4)
plt.ylim(0,2000)
# changing numeric ticks into string ticks using plt.xticks() and plt.yticks()
plt.xticks([1,2,3,4],["M1",'M2','M3',"M4"]) # it is used with list value to its corresponding specific data as we want to put

plt.show()


