terran_rivers = {
'nile':'egypt',
'mississippi':'usa',
'rheine':'france'
}
for river, country in terran_rivers.items():
	print(f"{river.title()} runs in {country.title()}!")

for river, country in terran_rivers.items():
	print(river.title())
	print(country.title())