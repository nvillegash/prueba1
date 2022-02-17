def divisors(num):
    # divisors = []
    # for i in range(1, num + 1):
    #     if num % i == 0:
    #         divisors.append(i)
    # return divisors
    return [i for i in range (1, num + 1) if num % i == 0]

def main():
    try:
        num = int(input("Enter a number: "))
        if num < 1:
            raise Exception("Please enter a positive number.")
        print(divisors(num))
        print("Finished my program.")
    except ValueError:
        print("You must enter a number.")
    except Exception:
        print("You must enter a positive number.")

if __name__ == '__main__':
    main()