################### LIST Examples##################
myList = [1, 2, 3, 4, "Manu", 6, "TiVO", 8, 9, 10]

def print_blank_line():
    print("--------------------------------------------------------------------")

print_blank_line()
print("myList = {}".format(myList))
print_blank_line()


#Adding and Removing Elements from List
# Inserting element at the end
myList.append("Sony")
myList.pop(0)
myList.insert(1, "MANU")
print("myList = {}".format(myList))

# #Loop through and print myList elements Example-1
# for n in myList:
#     print(n)

# #Loop through and print myList elements Example-2
# for i in range(0, len(myList)):
#     print(myList[i])


# Sorting List
myList2 = [15,1,4,2,6,2,8,3,99]
sorted(myList2)
print("Sorted List is = {}".format(myList2))
print("Sorted List is = {}".format(sorted(myList2)))

myList2.sort()
print("Sorted List is = {}".format(myList2))


# ######################################################### List Slicing ################################################
# # elements 3rd to 5th
# print("List Slicing Examples")
# print("elements 3rd to 5th")
# print(myList[2:5])
#
# # elements beginning to 4th
# print("elements beginning to 4th")
# print(myList[:-5])
#
# # elements 6th to end
# print("elements 6th to end")
# print(myList[5:])
#
# # elements beginning to end
# print("elements beginning to end")
# print(myList[:])

