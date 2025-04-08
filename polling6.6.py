favorite_languages = {'breana':'japanese', 'autumn': "french", 'caleb':'german', 'seth':'spanish'}
friends = {'breana','autumn'}
for name, language in favorite_languages.items():
	print(f"Hey, {name.title()}!")
	if name in friends:
		print(f"\tI see you prefer {language.title()}")
	else:
		print(f"{name.title()}, whats your favorite language?")