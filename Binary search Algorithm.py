'''--->Binary search is a searching algorithm for finding an elements's position in a sorted array(it is only applicable for an soretd array if the array is unsorted firstly we have to sort the array after sorting the array we can use binary search for that array)
---->Binary search algorithm can be implemented in two ways
1)Iterative method
2)Recursive method

--->Binary Search Algorithm(iterative)
do until the pointers low and high meet each other.
   mid=(low+high)/2
   if(x==arr[mid])
       return mid
   else if(x>arr[mid]) //x is on the right side
       low=mid+1
   else       //x is on the left side
       high=mid-1
       
---->BINARY EARCH ALGORITHM(RECURSIVE METHOD)
    binarysearch(arr,x,low,high)
       if low>high
        return false
       else
           mid=(low+high)/2
           if x == arr[mid]
             return mid
           else if x>arrr[mid]
              return binarysearch(arr,x,mid+1,high)
            else
               return binarysearch(arr,x,low,mid-1)
               
---->here we take one example for better to understand
    ex-1 arr[5,7,9,13,32,334,42,54,56,88]
          key=33
          
here mid value formula low+high/2
mid=(0+9/2)-->here 0 and 9 are the index numbers of low and start where low has oth index and high has 9th index
so here we get mid value as 4th index approximate so 32 is our mid value
33>A[mid]--->here 33 is greater than 32(if the mid value is less than our key value we have to consider the right side part means we ger mid+1 (if the mid value is greater  than key value we have to consider left side part mid-1)
--->we skip left side part because 33>32(in this case we consider the right side part)
   we get array as[33,42,54,56,88] then again we have to do midvalue start and end we get mid value as 54(here 33<mid(54) in this case we consider mid-1 means the left side part)
   we get array as[33,42] find mid value is 5 so mid is 33
   33=mid(33=33) we have to do until upto this condition ur index is 5'''
   
   #code for binary search
#(iterative method)
array=[3,4,5,6,7,8,9,10,11,12]
x=8#searching element
def binarysearch(array,x,low,high):
    while low<=high:
        mid=low+(high-low)//2
        if array[mid]==x:
            return mid
        elif array[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1

result=binarysearch(array,x,0,len(array)-1)

if result==-1:
    print("Element is not found in the array")
else:
    print(f'Element found at index: {result}')
    
#using recursive method

array=[3,4,5,6,7,8,9,10,11,12]
x=8
def binarysearch(array,x,low,high):
    if high>=low:
        mid=low+(high-low)//2
        if array[mid]==x:
            return mid
        elif array[mid]<x:
            return binarysearch(array,x,mid+1,high)
        else:
            return binarysearch(array,x,low,mid-1)
    return -1

result=binarysearch(array,x,0,len(array)-1) 

if result==-1:
    print("Element is not found in array")
else:
    print(f'Element is found at index:{result}')
       