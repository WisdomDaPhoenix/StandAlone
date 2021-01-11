d = {}
for i in range(7):
    p = input('Enter product name: ')
    p = p.lower()
    price = eval(input('Enter price: '))
    d[p] = price
total = sum([d[p] for p in d])
print('The total price of the inventory is ', total)
#Searches for a product
t = input('Search for a product: ')
t = t.lower()
if t in d:
    print('The product\'s price is', d[t])
else:
    print('The product entered -', t ,'is not in the inventory or list')

print('Complete product inventory - ', d)
print('\n'*3)
#All products less than your specified amount
amt = eval(input('Enter an amount in your currency: '))
j = ','
query = [x[0]+j for x in d.items() if x[1] < amt]
q = [c.title() for c in query]
sub_less_amt = ' '.join(q)
sub_less_amt = sub_less_amt[:-1]
print('Products less than', amt, 'include ',end='')
print(sub_less_amt,end='')
print('.')
