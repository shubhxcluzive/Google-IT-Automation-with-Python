import re
result = re.search(r"aza", "plaza") # returns matched string
print(result)
print(re.search(r"^x", "xmas"))
print(re.search(r"p.ng", "Penguin", re.IGNORECASE))
print(re.search(r"[pP]ython", "Python"))
print(re.search(r"[a-z]way", "end of highway"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))
print(re.search(r"[^a-zA-Z]", "876 cloud."))  #find string not preceded by character class
