class Country:
    def __init__(self, new_name, population):
        self.name = new_name
        self.population = population
        self.prev = None
        self.next = None


class CountryList:
    def __init__(self):
        self.head = 0
        self.tail = 0
        self.size = 0

    def append(self, new_name, population):
        new_country = Country(new_name, population)
        if self.head is None:
            self.head = new_country
            self.tail = new_country
        else:
            self.tail.next = new_country
            new_country.prev = self.tail
            self.tail = new_country
        self.size += 1

    def insert_first(self, new_name, population):
        new_country = Country(new_name, population)
        if self.head is None:
            self.head = new_country
            self.tail = new_country
        else:
            self.head.prev = new_country
            new_country.next = self.head
            self.head = new_country
        self.size += 1

    def print_all(self):
        current_country = self.head
        while current_country is not None:
            print(current_country.name, current_country.population)
            current_country = current_country.next


country = CountryList()
country.append("Bangladesh", 16)
# country.append("India", 120)
# country.append("China", 150)
# country.append("Bangladesh", 5)
country.print_all()
