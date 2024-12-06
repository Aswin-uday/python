#squre list
numlst=[1,2,3,4,5,6]
# [expression for i in items]
sqrlst=[i**2 for i in numlst]
print(sqrlst)

sqrlst=list(map(lambda x:x**2,numlst))
print(sqrlst)

##### i/p in range 4
input_list=[input() for i in range (4)]
print(input_list)

##even list

nulst=[1,2,3,4,5,6,7,8,9,10]
evelst=[i for i in nulst if i%2==0 ]
print(evelst)

##odd list filter function
oddlst=list(filter(lambda x:x%2!=0, nulst))
print(oddlst)

##dict comp
dctcmp = {i : i**2 for i in range(10)}
print(dctcmp)

##name in capital

people={'mini': 29, 'shan' : 20, 'jaya' : 30}
cap_people = {k.upper():v for (k,v) in people.items()}
print(cap_people)

name_dct = {k:k.upper() for k in people.keys()}
print(name_dct)

###

keys=['a','b','c','d']
values=[1,2,3,4]
a = zip(keys,values)
print(list(a))

dict_values={k:v for (k,v) in zip(keys,values)}
print(dict_values)