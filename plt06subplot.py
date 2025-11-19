"""import matplotlib.pyplot as plt

# plt.subplot(nrows,ncols,index)

x=[1,2,3,4]
y=[10,20,15,25]
plt.subplot(1,2,1) #1st row,2nd column,1st subplot
plt.plot(x,y)
plt.title('line Chart')

plt.subplots(1,2,2)# 1st row ,2nd column,2nd subplot
plt.bar(x,y)
plt.title("Bar Chart")

# plt.tight_layout()
plt.show()"""


import matplotlib.pyplot as plt

# fig,ax=plt.subplots(nrows,ncols,figsize=(width,height))
fig,ax=plt.subplots(1,2,figsize=(4,8))

x=[1,2,3,4]
y=[10,20,15,25]

ax[0].plot(x,y,color='blue')
ax[0].set_title("line Plot")

ax[1].bar(x,y,color='green')
ax[1].set_title("Bar Chart")

plt.suptitle("Comparison of line and Bar charts")
plt.tight_layout() #automatic adjustment .this is always used just above show() method
plt.show()


