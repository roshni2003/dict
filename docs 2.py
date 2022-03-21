a="w3resource"
b=list(a)
i=0
l={}
while i<len(b):
    c=0
    d={}
    m=0
    while m<len(b):
        if b[i]==b[m]:
            c=c+1
        m=m+1
    l.update({b[i]:c})
    i=i+1
print(l)