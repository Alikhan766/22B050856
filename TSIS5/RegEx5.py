import re


def text_match(text):
    patterns = '^a.*b$'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return ('Not matched!')


print(text_match("ab"))  # Found a match!
print(text_match("a b"))  # Found a match!
print(text_match("a_qwerty_b"))  # Found a match!
print(text_match("abc"))  # Not matched!
