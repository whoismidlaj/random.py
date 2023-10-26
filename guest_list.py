guest = ['John', 'Dave', 'Mario', 'Franklin']

print(f'hi {guest[0]}, join our party')
print(f'hi {guest[1]}, join our party')
print(f'hi {guest[2]}, join our party')
print(f'hi {guest[3]}, join our party')

print(f'{guest[2]} cant make it')

guest[2] = 'Johny'

print(f'hi {guest[0]}, join our party')
print(f'hi {guest[1]}, join our party')
print(f'hi {guest[2]}, join our party')
print(f'hi {guest[3]}, join our party')

print('dinner left, wanna join?')

guest.insert(0,'Mary')
guest.insert(3,'Morgan')
guest.append('Angel')

print(f'hi {guest[0]}, join our party')
print(f'hi {guest[1]}, join our party')
print(f'hi {guest[2]}, join our party')
print(f'hi {guest[3]}, join our party')
print(f'hi {guest[4]}, join our party')
print(f'hi {guest[5]}, join our party')
print(f'hi {guest[6]}, join our party')

print ('im sorry, i can only invite two')

removed_guest = guest.pop()
print(f'im sorry {removed_guest}')
removed_guest = guest.pop()
print(f'im sorry {removed_guest}')
removed_guest = guest.pop()
print(f'im sorry {removed_guest}')
removed_guest = guest.pop()
print(f'im sorry {removed_guest}')
removed_guest = guest.pop()
print(f'im sorry {removed_guest}')

print(f'you can still come {guest[0]}')
print(f'you can still come {guest[1]}')

del guest[0]
del guest[0]

print(guest)