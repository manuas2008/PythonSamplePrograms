#Examples for for, while, if-elif-else


myList = [1, 'Manu', 3, 'TiVO', 5, 'Sony', 7, 8, 9, 10]

##############  for loop example   ###############
# for n in myList:
#     print(n)

##############  while loop ###############
############### while example-1 ##########
i=0
while i < len(myList):
    print(myList[i])
    i+=1

############### while example-2 ##########
# i = 0
# try:
#     while myList[i]:
#         print(myList[i])
#         i += 1
# except IndexError:
#     pass

##############  if-elif-else ###############
# i = 1
# for n in myList:
#     if i % 2:
#         print(n)
#     else:
#         pass
#     i+=1