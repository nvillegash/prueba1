def main():
    # squares = []                  # I create the list "squares"
    # for i in range(1,101):        # It does not include 101, it is up to 100
    #     if i % 3 != 0:            # If the remainder of the division of the number i by 3 is different from 0
    #         squares.append(i**2)  # Incluyo en la lista a todos los i**2

    # squares = [i**2 for i in range(1,101) if i % 3 !=0]
    # For each i from 1 to 100 that is not divisible by 3, its i squared will be displayed

    squares = [i for i in range(1,100000) if i % 36 ==0]
    # For each i from 1 to 99999 that is divisible by 4, 6 and 9, its i will be displayed

    print(squares)

if __name__ == '__main__':
    main()
