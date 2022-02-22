import time

class FiboIter():

    def __init__(self, max:int):
        self.max = max

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            if self.counter <= self.max:
                self.aux = self.n1 + self.n2
                # self.n1 = self.n2
                # self.n2 = self.aux
                self.n1, self.n2 = self.n2, self.aux # Swapping
                self.counter += 1
                return self.aux
            else:
                raise StopIteration


num = input("Enter a number of interactions: ")
assert num.isnumeric(), "You have to enter a number"
num = int(num)

if __name__ == "__main__":
    fibonacci = FiboIter
    for element in fibonacci(num):
        print(element)
        time.sleep(.3)