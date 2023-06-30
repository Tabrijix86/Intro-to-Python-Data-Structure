# separate chaining
from collections import deque

table_size = 10
hash_table = dict((key, deque()) for key in range(table_size))


def hash_function(k):
    return k % table_size


def put(new_data):
    hash_value = hash_function(new_data)
    hash_table[hash_value].appendleft(new_data)


def search(search_data):
    hash_value = hash_function(search_data)
    if search_data in hash_table[hash_value]:
        return True
    else:
        return False


def delete(data):
    hash_value = hash_function(data)
    if data in hash_table[hash_value]:
        hash_table[hash_value].remove(data)
    else:
        print("Element does not exist")


put(45)
put(35)
put(33)
print(search(15))
delete(33)

for x in hash_table:
    print(x, ":", list(hash_table[x]))
