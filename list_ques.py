a = [1,1,2,3,4,5,6,1,3,4,8,9,4,4,2]


search = 1

cnt = a.count(search)
start = 0 
result = []
for i in range(cnt):
    idx = a.index(search, start)
    start = idx + 1
    result.append(idx)
print(result)



fib = [0,1]
for i in range(20):
    fib.append(fib[-1] + fib[-2])
print(fib)


num = 200
f = 1 
for i in range(1, num+1):
    f = f * 1
print(f)


color = ['red','green','blue','cyan','white','purple','gray','brown']

filter_opt = []
for c in color:
    if c.endswith('e'):
        filter_opt.append(c)
print(filter_opt)


filter_opt_ane = []
for c in color:
    if 'a' in c or 'e' in c:
        filter_opt_ane.append(c)
print(filter_opt_ane)


#mapping

a = [1,2,3,4,5,6,7,8,9,10]
a2 = []
for num in a:
    a2.append(num+2)
print(a2)


fullname = ['Amar kumar', 'Vijay kumar', 'Rajesh sing', 'Amar patel']

shortname = []

for nm in fullname:
    words = nm.split()
    shortname.append(words[0][0] + words[-1][0])
print(shortname)


