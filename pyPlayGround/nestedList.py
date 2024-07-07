alist = [["1", "2", "3"], ["fruit", "apple", "banana"]]
blist = ["mang0", "apple", "banana"]
clist = ["0", "1", "2"]
maplist = [clist, blist]
size_blist = len(blist)
size_alist = len(alist)

##Ways of printing list length.
# print(size_blist)   
# print(len(alist))   

#P#rinting list length of letters and contents
# for key in blist:
#     print (f"{len(key)}: {key[0:]}")


##Mapping 2 lists
# print(f"{maplist[0]}::", maplist[1])

##Print specific item for each list
# print(f"{maplist[0][0]} ::", maplist[1][0])

##Map the number to specific fruit in order
# print(f"{maplist[0][0]} ==>", maplist[1][0])
# print(f"{maplist[0][1]} ==>", maplist[1][1])
# print(f"{maplist[0][2]} ==>", maplist[1][2])

##Another way to Map the number to specific fruit in order
# cnt=0
# for map in (maplist):
#     print(len(map))
#     print(f"{maplist[0][cnt]} ==>", maplist[1][cnt])
#     cnt=+1
# print(f"{maplist[0][cnt+1]} ==>", maplist[1][cnt+1])


##Another way to Map the number to specific fruit in order
Dlist=["coke", "juice", "water"]
for index, val in enumerate(Dlist):
    print(index, val)
##Output
#0 coke
#1 juice
#2 water


# my_list = [21, 44, 35, 11]
# for index, val in enumerate(my_list):
#     print(index, val) 
##ouput: 
#0 21
#1 44
#2 35
#3 11



# new_list = [1,1,1,1,2,2,3,3,3,3,4,5]
# new_list = list(dict.fromkeys(new_list))
# print(new_list)
##ouput: "[1, 2, 3, 4, 5]"


# numbers = [5,6] 
# numbers.clear()
# print(numbers)
##output []


# numbers = [5,6,7,8]
# while numbers:
#    numbers.pop(0)
#    print(numbers)
##output:
##[6, 7, 8]
##[7, 8]
##[8]
##[]