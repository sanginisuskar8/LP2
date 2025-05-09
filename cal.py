while True:
    print("Calculator")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exit")
    inp = int(input("Enter your input: "))

    if (inp == 1):
        a = int(input("Enter No 1: "))
        b = int(input("Enter No 2: "))
        print(f"{a} + {b} = {a+b}")
    elif (inp == 2):
        a = int(input("Enter No 1: "))
        b = int(input("Enter No 2: "))
        print(f"{a} - {b} = {a-b}")
    elif (inp == 3):
        a = int(input("Enter No 1: "))
        b = int(input("Enter No 2: "))
        print(f"{a} x {b} = {a*b}")
    elif (inp == 4):
        a = int(input("Enter No 1: "))
        b = int(input("Enter No 2: "))
        print(f"{a} / {b} = {a/b}")
    elif (inp == 5):
        print("Bye!")
        break
    else:
        print("Enter a valid input!")
    print()
