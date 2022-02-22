import time

def fibo_gen(max_counter):
    a, b, n = 0, 1, 0
    while n <= max_counter:
        yield a
        a, b = b, a+b
        n += 1

num = input("Enter a number of interactions: ")
assert num.isnumeric(), "You have to enter a number"
num = int(num)

if __name__ == '__main__':
    fibonacci = fibo_gen
    for element in fibonacci(num-1):
        print(element)
        time.sleep(.3)