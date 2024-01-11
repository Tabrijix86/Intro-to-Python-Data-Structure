import re

s = "Apple a day keeps the Doctor away"
print(re.match(r"[Aa]pple", s))
# The bracket notation is one example of the special syntax of regular expressions. In this case it says that any of
# the characters inside brackets will do: either "A" or "a". The other letters in "pple" will act normally. The
# string r"[Aa]pple" is called a pattern.
