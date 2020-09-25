import sys
import GADDAG
import json
import base64
wordlist = []

"""
with open ("words.py", "r") as words:
	for w in words:
		wordlist.append(w.rstrip())
"""		
#with open("words.json", "w") as grid:
#	json.dump(wordlist, grid)
"""	
with open("words.json", "r") as grid:
	g = json.load(grid)
"""
my_dict = ""
with open(str(sys.path[0]) + "/dictionary", "r") as dict_file:
	my_dict = dict_file.read().strip().upper().split("\n")
	
	
	
gaddag = GADDAG.GADDAG(my_dict)
print ("hi")

print (str(gaddag))
with open("gaddag_variable", "w") as grid:
	json.dump(base64.b64encode(gaddag).decode('ascii'), grid)
	
