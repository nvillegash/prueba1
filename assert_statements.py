# I assert that this condition is true, if not I print this error message
def divisors(num):
    return [i for i in range (1, num + 1) if num % i == 0]

def main():
    num = input("Enter a number: ")
    assert num.isnumeric(), "You have to enter a number"
    print(divisors(int(num)))
    print("Finished my program.")

if __name__ == '__main__':
    main()