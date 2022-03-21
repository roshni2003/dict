from heapq import nlargest


dic={'a':3,'b':2,'c':9,'d':6,'e':5}
three_largest = nlargest (3,dic,key=dic.get)
print(three_largest)
    
