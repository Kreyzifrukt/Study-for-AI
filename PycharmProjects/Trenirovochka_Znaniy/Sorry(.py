a = input("Текст для повторения\n")
# b = int(input("Введите количевство повторений\n"))
b = 2**3**3
if b < 0:
    print("Wrong data")
else:
    for i in range(1,b+1):
        print(i,":", a, sep=" ")
