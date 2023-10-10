from calendar import month
from datetime import datetime

now=datetime.now()
y,m=now.year,now.month

print(month(theyear=y,themonth=m))

#linear search
array=[3,6,4,1,8,9,7]
n=len(array)
x=8
def linearsearch(array,n,x):
    for i in range(0,n):
        if array[i]==x:
            return i
    return -1

result=linearsearch(array,n,x)
if result==-1:
    print("Element is not found in the array")
else:
    print(f'Element is found at index:{result}')
    
'''normally if u keep your file in stash mode so to come out of stash we can use the command is git stash pop or git stash apply
Git stash is a useful feature in git that allows you to temporarily save changes that you don't want to commit yet.it's like a "save point" for
your work.you can use "git stash save" to stash your changes,and then use "git stash apply" or "git stash pop" to retrieve them later.it's great
for switching branches or temporarily setting aside unfinished work'''