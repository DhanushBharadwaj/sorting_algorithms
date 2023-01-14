def merge_sort(mylist):
    if len(mylist)>1:
        left_part=mylist[:len(mylist)//2]
        right_part=mylist[len(mylist)//2:]

        merge_sort(left_part)
        merge_sort(right_part)

        #merge
        i=0
        j=0
        k=0

        while i< len(left_part) and j<len(right_part):
            if left_part[i]<right_part[j]:
                mylist[k]=left_part[i]
                i=i+1
            else:
                mylist[k]=right_part[j]
                j=j+1
            k=k+1
        
        while i < len(left_part):
            mylist[k]=left_part[i]
            i=i+1
            k=k+1
        
        while j< len(right_part):
            mylist[k]=right_part[j]
            j=j+1
            k=k+1
    
        
mylist=[5,4,3,2,1]
merge_sort(mylist)
print(mylist)
