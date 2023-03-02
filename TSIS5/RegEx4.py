import re


def text_match(text):
    patterns = '^[A-Z]+[a-z]+$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("aa"))  # Not matched!
print(text_match("AA"))  # Not matched!
print(text_match("Aa"))  # Found a match!
