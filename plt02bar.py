import matplotlib.pyplot as plt
product=['A','B','C','D']
sales=[1000,1500,800,2000]
plt.bar(product,sales,color='orange',label='Sales 2025')
plt.xlabel("Product")
plt.ylabel("Sales")
plt.title("Product Sales Comparison")
plt.legend(loc='upper left',fontsize=10)
plt.show()