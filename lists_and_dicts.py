def main():
    my_lyst = [1,"Hello", True, 4.5]
    my_dict = {"firstname": "Nicolás", "lastname": "Villegas"}

    super_list = [
        {"firstname": "Nicolás", "lastname": "Villegas"},
        {"firstname": "Fernandito", "lastname": "Gordete"},
        {"firstname": "Don", "lastname": "Ectores"},
        {"firstname": "Water", "lastname": "Pillar"},
        {"firstname": "Rulos", "lastname": "Gordete"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "interger_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == '__main__':
    main()