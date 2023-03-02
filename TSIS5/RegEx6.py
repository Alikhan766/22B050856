import re


def text_match(text):
    patterns = re.sub("[ .,]", ":", text)
    return patterns


print(text_match(' a'))  # :a
print(text_match('.b'))  # :b
print(text_match(',c'))  # :c
print(text_match(' a.b,c'))  # :a:b:c
