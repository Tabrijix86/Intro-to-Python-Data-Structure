import textwrap

string = "This is a very very very very very long string."
print(textwrap.wrap(string, 8))
# ['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.']
