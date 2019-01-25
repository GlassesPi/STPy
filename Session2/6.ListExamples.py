lst = [10, 20, 2, 1]

lst.append(30)
lst.count(2)    #2
lst.index(20)   #1
lst.insert(1,30)
lst.pop()
lst.pop(1)  #20             Deletes value by key
lst.remove(20) #201         Deletes by value 
lst.reverse()
lst.sort(reverse=True)


############# INDEXING ###############
len(lst)

lst[-1] #1
lst[-2] #2
######################################

#############  SLICING  ##############
lst[1:3]    #20 ,2

lst = [10,20,30,5,10,15]
lst[0:6:2] #10,30,10
######################################

