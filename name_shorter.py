fullname = ['Aditya Gupta', 'Vijay kumar gupta', 'Ajay patel', 'Vimal pandey', 'Sachin yadav', 'Kunal rai', 'Golu maurya']

shortname = []

for names in fullname:
    print(names)
    sn = names.split()
    shortname = sn[0][0] + sn[-1][0]
    print(shortname, end=' \n \n')



