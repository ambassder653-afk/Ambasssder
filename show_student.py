fruits = ['Virasouk','Bounma','Ambassder','Vanalak','Kong kis']

for a in fruits:
    if a == 'Ambassder':
        break

    print(a)

print(type(fruits))    

print("===================")

fruits = ['Virasouk','Bounma','Ambassder','Vanalak','Kong kis']
for a in fruits:
    if a == 'Ambassder':
        continue

    print(a)

print(type(fruits))    