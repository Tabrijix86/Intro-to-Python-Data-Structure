year = int(input("Enter the year from which you wish to count: "))
current_year = year
leap_list = list()
while len(leap_list) < 20:
    if year % 100 != 0 and year % 4 == 0:
        leap_list.append(year)
    elif year % 100 == 0 and year % 400 == 0:
        leap_list.append(year)
    else:
        pass
    year += 1
print(f"\nThe list of the next 20 leap years from {current_year}: ")
print(leap_list)
