def printnum(a, mylist):
    if a == 5:
        print(mylist)
        return
    mylist.append(a)
    a = a + 1
    printnum(a, mylist)


def main():
    mylist = []
    printnum(2, mylist)


main()
