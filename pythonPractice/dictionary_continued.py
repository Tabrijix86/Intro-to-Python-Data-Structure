# adding elements in dictionary from input
dictionary = {}
li = list()
for _ in range(int(input())):  # int(input()) is comparable to a variable n for desired range
    name = input()
    score = float(input())
    if score in dictionary:
        dictionary[score].append(name)
    else:
        dictionary[score] = [name]  # assigns a name to a new score
    if score not in li:
        li.append(score)
print(dictionary)
print(li)
