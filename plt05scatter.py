"""import matplotlib.pyplot as plt
# plt.scatter(x,y ,color='colorName', marker='marker_style', label='label_name')
credit_hours=[1,2,3,4,5,6,7,8]
exam_scores=[50,55,60,65,70,75,80,85]
plt.scatter(credit_hours,exam_scores, color='green', marker='s', label='Student Data')
# markers are o->circle,s->square,^->triangle,d->diamond,+->+sign
plt.xlabel("Hours Studies")
plt.ylabel("Exam Scores")
plt.title("Relation between study hour and results")
plt.grid("True" ,color='gray',linestyle=':')
plt.legend(loc='upper left',fontsize=10)
plt.show()"""
import matplotlib.pyplot as plt

plt.scatter([1,2,3], [50,60,70], color='blue',label='Class A') #grp1
plt.scatter([1,2,3],[40,50,52], color='orange',label='Class B') #grp2

plt.title('Comparison of Two Classes.')
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.legend(loc='upper left',fontsize=10)
plt.grid("True",color='gray',linestyle=':')
plt.show()