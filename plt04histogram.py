"""import matplotlib.pyplot as plt
# it is used to show the distribution of the continuos data by dividing into ranges called also bins
# plt.hist(data,bins=number_of_bins,color='colorName',edgeColor='black)
# Whenever you want to see patterns, spread, or frequency of data, a histogram is the best tool.
scores=[45,67,89,56,78,56,89,23,45,56,90,85,70,73,68,77,50]
plt.hist(scores,bins=5,color='purple',edgecolor='green')
plt.show()"""


import matplotlib.pyplot as plt
import numpy as np

data = np.random.normal(70, 10, 200)  # Example: students' marks

plt.hist(data, bins=10, edgecolor='black')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.title('Distribution of Student Scores')
plt.show()
