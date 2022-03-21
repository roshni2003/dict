a =  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
b=sorted(a.items(),key=lambda x:x[1])
print("asscending",b)