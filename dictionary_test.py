my_dict = {
	("A", 1):1,
	("n", 11):2,
	("C", 4):3	
		}

for x in my_dict:
	print(x)
	
print ([y for x in [my_dict[n] * [n] for n in my_dict] for y in x])