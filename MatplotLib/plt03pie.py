import matplotlib.pyplot as  plt
# %1.1f means for 45.5 or 54.5
# if we want to display percentage symbol also then we use %%1f
# plt.pie(values,labels=label_list,color=color_list,autopct="%1.1f%%")
regions=['North','South','East','West']
revenue=[3000,2000,1500,1000]
plt.pie(revenue,labels=regions,autopct='%1.1f%%',colors=['gold','skyblue','lightgreen','coral'])
plt.title("Revenue Contributions by Regions")
plt.show()
