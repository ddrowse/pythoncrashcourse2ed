guests = ['shauna','mauri','misty','tai']
for guest in guests:
	guest = guest.title()
	print(f"Hey, {guest} let's do dinner?")
print('Mauri cannot come.')
guests.remove('mauri')
guests.append('melissa')
for guest in guests:
	guest = guest.title()
	print(f"Let's do breakfast instead, {guest}")
