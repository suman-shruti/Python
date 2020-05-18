def main():
    total=0
    num = int(input("Type a number: "))
    while num !=-1:
        total=total + num
        num = int(input("Type a number: "))
    print("The total is " + str(total))


if __name__ == '__main__':
    main()