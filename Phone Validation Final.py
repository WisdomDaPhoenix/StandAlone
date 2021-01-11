#Phone Number Validation 
s = input('Enter a phone number: ')  
if '-' in s: 
    p=list(s)  
    for c in p: 
         if c.isalpha():
             print('Invalid number')
         break  
    s = ''.join(p)  
    L = s.split('-')
    if L[0] == '1' and len(L[1])==3 and len(L[2])==3 and len(L[3])==4: 
        print('Valid number')  
    elif len(L[0])== 3 and len(L[1])==3 and len(L[2])==4:
        print('Valid number')
    else:
        print('Invalid number')
      
else: 
    print('Invalid number')  


# ALTERNATIVE CODE (Phone Validation)
s = input('Enter a phone number: ')  
if '-' in s: 
    p=list(s)  
    for c in p: 
         if c.isalpha():
             print('Invalid number')
         break  
    s = ''.join(p)  
    L = s.split('-')
    countL = [len(c) for c in L] 
    d = [1,3,3,4]
    f = [3,3,4]
    if countL==d or countL==f:
       print('Valid number')
    else:
        print('Invalid number')
      
else: 
    print('Invalid number')
