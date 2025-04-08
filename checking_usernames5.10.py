current_users = ['scallywag','jonahHILL', 'sallyface','buttersrum','batman']
new_users = ['Scallywag', 'aprilshower','roalddahl','sallyface','bob']
for member in new_users:
	if member.lower() in current_users:
		print("username taken")
	else:
		print(f"Welcome, {member}")