import re
text = "SomeTextForExample"
print(re.findall('[A-Z][^A-Z]*', text))
