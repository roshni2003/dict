dict={'x':500,'y':584,'z':560}
max=max(dict.keys(),key=(lambda k:dict[k]))
min=min(dict.keys(),key=(lambda k:dict[k]))
print('maximum value:',dict[max])
print('minimum value:',dict[min])