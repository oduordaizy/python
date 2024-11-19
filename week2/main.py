
my_list = []

my_list.append(10, 20, 30, 40)

#Inserting the value 15 at the second position.
my_list.append(1, 15)

list2 = [50, 60, 70]

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

