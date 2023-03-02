def snake_to_camel(word):
    return ''.join(x.title() for x in word.split('_'))


print(snake_to_camel('python_exercises'))
