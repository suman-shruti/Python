def main():
    while True:
        num=int(input("Enter a number: "))
        if num==0:
            print("Your number is equal to 0.")
        elif num>0:
            print("Your number is greater than 0.")
        else:
            print("Your number is less than 0.")

if __name__ == '__main__':
    main()