
my_list = [1, 30, 19000]

my_list.append(15)

list2 = [50, 60]

my_list.extend(list2)
print("Orginal list: ", my_list)

#removing the last element from the list2
my_list.pop()
print("List after removing the last element: ", my_list)

#Sorting in ascending order
my_list.sort()
print("Sorted list: ",my_list)

#Finding and printing the index of the value 30
index_30 = my_list.index(30)
print("Index of the value 30: ", index_30)

