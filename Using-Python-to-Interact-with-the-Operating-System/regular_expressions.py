import re
result = re.search(r"aza", "plaza") # returns matched string
print(result)
print(re.search(r"^x", "xmas"))
print(re.search(r"p.ng", "Penguin", re.IGNORECASE))
print(re.search(r"[pP]ython", "Python"))
print(re.search(r"[a-z]way", "end of highway"))
print(re.search(r"cloud[a-zA-Z0-9]", "cloud9"))
print(re.search(r"[^a-zA-Z]", "876 cloud."))  #find string not preceded by character class
print(re.search(r"cat| dog", "this is cat"))
print(re.findall(r"cat| dog", "this is cat and dogs."))
print(re.search(r"Py*n", "Pynoloing"))
print(re.search(r"Py[a-zA-Z]*n", "python programming", re.IGNORECASE))
print(re.search(r"o+l+", "golfish"))
print(re.search(r"o+l+", 'woolllen'))
print(re.search(r"p?each", "to each of own"))
print(re.search(r"p?each", "to peach of own"))
print(re.search(r"\.com", "google.com"))
print(re.search(r"\w*", "thiss1 is it"))
print(re.search(r"^A.*a$", "Arjentinan"))
pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "this_is_it")) #validate variable

#Capturing Groups: portion of pattern

def reaarange_name(name):
    result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
print(reaarange_name("malai, das. D"))


print(re.search(r"[a-zA-Z]{5}", "a ghost toast"))
print(re.findall(r"\b[a-zA-Z]{5}\b", "a ghost toast poasrte"))
print(re.findall(r"\w{5,10}", " i like to eat sometime starwberries"))
print(re.findall(r"s\w{,10}", " i like to eat sometime starwberry"))
#strace -o file.strace hu.py
print(re.split(r"[\.\,]", "Once, upon a time. are you there"))