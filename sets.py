# def remove_duplicates(some_list):
#     without_duplicates = []
#     for element in some_list:
#         if element not in without_duplicates:
#             without_duplicates.append(element)
#     return without_duplicates

# def main():
#     random_list=[1, 1, 2, 2, 4]
#     print(remove_duplicates(random_list))

def remove_duplicates(random_list):
    return list(set(random_list))

def main():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicates(random_list))

if __name__ == '__main__':
    main()