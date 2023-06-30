# linear probing
table_size = 10
hash_table = dict((key, None) for key in range(table_size))


def hash_function(k):
    return k % table_size


def count_none():
    return list(hash_table.values()).count(None)


def put(new_data):
    if count_none() != 0:
        hash_value = hash_function(new_data)
        while hash_table[hash_value] is not None:
            hash_value = (hash_value + 1) % table_size
        hash_table[hash_value] = new_data
    else:
        print("Hash table is full")


def search(search_data):
    count = 0
    hash_value = hash_function(search_data)
    while hash_table[hash_value] is not search_data:
        hash_value = (hash_value + 1) % table_size
        count += 1
        if count == table_size:
            break
    if hash_table[hash_value] is search_data:
        return True
    else:
        return False


def delete(data):
    count = 0
    hash_value = hash_function(data)
    while hash_table[hash_value] is not data:
        hash_value = (hash_value + 1) % table_size
        count += 1
        if count == table_size:
            break
    if hash_table[hash_value] is data:
        hash_table[hash_value] = None
    else:
        print("Element does not exist")


put(45)
put(35)
put(25)
put(46)

for x in hash_table:
    print(x, ":", hash_table[x])
