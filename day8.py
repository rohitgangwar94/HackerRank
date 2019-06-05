n = int(input())

d = {}
lst = []
for i in range (n):
    inpt = input()
    key,value = inpt.split()
    d[key] = value
    
for l in range(n):
    a = input()
    lst.append(a)


for j in lst:
    if j in d:
        print('{}={}'.format(j,d[j]))
    else:
        print('Not found')
