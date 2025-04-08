gig_user = ['sallyface','bm_lulu','scallywag','faalengoose','admin']
for user in gig_user:
	if user == '':
		print("no one here")
	elif user == 'admin':
		print("Hello Overlord")
	else:
		print(f"What we jerkin' it too today, {user}?")

gig_user = []
if gig_user:
	for user in gig_user:
		if user == 'admin':
			print("Hello Overlord")
		else:
			print(f"What we jerkin' it too today, {user}?")
else:
	print('no one here bruv')
