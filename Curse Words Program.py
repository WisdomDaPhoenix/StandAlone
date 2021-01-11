#Change all curse words to '****' within a string, simulating parental controls 
s = input('Enter a string: ')
L = ['darn','dang','freakin','heck','shoot','Darn','Dang','Freakin','Heck','Shoot']
for i in range(len(s)):
    for t in L:
        if t in s:
            s = s.replace(t,len(t)*'*',-1)
print(s)


#OR
s = input('Enter a string: ')
s = s.lower()

L = ['darn','dang','freakin','heck','shoot']
for i in L:
    if 'freakin' in s:
        s = s.replace('freakin','*******',-1)
    elif 'darn' in s:
        
        s = s.replace('darn','****',-1)
    elif 'shoot' in s:
        s = s.replace('shoot','*****',-1)
    elif 'heck' in s:
        s = s.replace('heck','****',-1)
    elif 'dang' in s:
        s = s.replace('dang','*****',-1)
        
print(s)
