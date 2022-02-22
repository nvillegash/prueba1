def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "You can only use strings"
        return string * n
    return repeater

def main():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hellow "))
    repeat_10 = make_repeater_of(10)
    print(repeat_10("Platzi "))

if __name__ == '__main__':
    main()