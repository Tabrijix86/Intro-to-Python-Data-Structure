# # # num1, num2 = 10, 5
# # # result = num1 + num2
# # # print(result)
# # # print(type(result))
# #
# # v = 5.5
# # print(type(v))
# #
# # w = 12345678999999990.1234567899999990
# # print(type(w))
# #
# # s = 'a'
# # print(type(s))
#
# print(2 == 3)
saarc_countries = ["Afghanistan", "Bangladesh", "Bhutan", "India", "Pakistan"]
country = input("Enter a country name: ")
if country in saarc_countries:
    print(country, "exists in SAARC")
else:
    print(country, "is not in SAARC")
print("Program Terminated")