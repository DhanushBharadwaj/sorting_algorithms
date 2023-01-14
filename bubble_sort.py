def bubble_sort(mylist):
    for i in range(len(mylist)):
        for j in range(len(mylist)-i-1):
            if mylist[j] > mylist[j+1]:
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
    return mylist

mylist = [5,4,3,2,1,0]
new=bubble_sort(mylist)
print(new)
