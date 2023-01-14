def insertion_sort(mylist):
    for i in range(1,len(mylist)):
        key=mylist[i]
        j=i-1
        while j>=0 and key < mylist[j]:
            mylist[j+1]=mylist[j]
            j=j-1
        mylist[j+1]=key
    return mylist

mylist=[5,4,3,2,1]
ans=insertion_sort(mylist)
print(ans)
 
