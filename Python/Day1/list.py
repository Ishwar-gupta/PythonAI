
# Lists are mutuable i.e changable
# list=["Apple",4 ,8 ,9.95,"orange","grapes","banana","Siddhu","Junnu"]
# print(list[0])
# list[0]="Strawberry"# Unlike Strings ,lists are mutable
# print(list[0])
# print(list[2:6])
# list.append("Suman")
# list.insert(8,"loves")
# print(list)

lst=[1,5,2,43,5,67,99,33]
# lst.sort()
# print(lst)
# lst.reverse()
# print(lst)
lst.insert(3,"Siddhu")# Insert Siddhu such that its index in the list
print(lst)
lst.pop(4)# it will delete that index item
print(lst)
lst.remove("Siddhu")
print(lst)
lst.remove(99)# it will remove the particular value from the list
print(lst)