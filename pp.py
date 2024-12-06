string="abccccdef" #duplicatew
s=""
for i in string:
    if not i in s:
        s+=i
print(s)        