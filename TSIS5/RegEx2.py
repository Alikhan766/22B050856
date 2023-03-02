import re


def text_match(text):
    patterns = 'ab{2,3}'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("ac"))  # Not matched!
print(text_match("abb"))  # Found a match!
print(text_match("abbb"))  # Found a match!
