######################################################### Dictionaries Examples #####################################
# 1. Dictionaries are not ordered
# 2. Dictionaries are Mutable
myDictionary = {"Name": "Manu", "Age": 42, "Company": "TiVO"}
######## Accessing Dictionary Items Example-1 #############
# for k,v in myDictionary.items():
#     print("myDictionary[{}] = {}".format(k,v))

for k, v in myDictionary.items():
    print("myDictionary[{}] = {}".format(k, myDictionary[k]))


