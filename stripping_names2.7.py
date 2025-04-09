p_name = "  cookie"
b_name = "goldy   "
d_name = '  colonel  '
p_name = p_name.lstrip()
b_name = b_name.rstrip()
d_name = d_name.strip()
p_name = p_name.title()
b_name = b_name.title()
d_name = d_name.title()
print(p_name) 
print(b_name)
print(d_name)
print(F"People I know include:\n {b_name}\n {p_name}, \t and {d_name}")
##admittedly it took way to long to figure out stripping and formatting and I probably still did it wrong