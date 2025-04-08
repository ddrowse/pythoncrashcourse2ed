python_terms = {
'integer':'not letter characters made of numerals',
'character':'letters or numbers not being interpretted as cs language or maths',
'code':'the process of writing programs in computer language'
}
for term, mean in python_terms.items():
	print(f"\nTerm: {term.title()}")
	print(f"Meaning: {mean}")