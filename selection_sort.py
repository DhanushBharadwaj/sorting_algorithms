def selection_sort(mylist):
    for i in range(len(mylist)):
        min_index=i
        for j in range(min_index+1,len(mylist)):
            if mylist[min_index]>mylist[j]:
                min_index=j
        mylist[i],mylist[min_index]=mylist[min_index],mylist[i]
    return mylist

mylist=[5,4,3,2,1]
ans=selection_sort(mylist)
print(ans)