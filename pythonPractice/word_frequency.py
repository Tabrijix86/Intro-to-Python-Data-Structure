def count(word):
    if word[-1] == '.':
        word = word[0:len(word) - 1]
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter.update({word: 1})


Sentence = str(input())
word_counter = {}
li = Sentence.split()
for elements in li:
    count(elements)
print(word_counter)
