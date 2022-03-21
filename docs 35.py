dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
a=0
for i in dict:
    for j in dict[i]:
        a=a+1
print(a)