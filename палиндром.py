string = input("введите вашу строку: ")


reversed_str = string[::-1]
if string == reversed_str:
    print(True)
else:
    print(False)

