DATA = [ # If the variable is written in uppercase, we should always call it constant
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():

    # List comprehensions
    all_python_devs_LC = [worker["name"] for worker in DATA if worker ["language"] == "python"]        # List of people who use Python
    all_Platzi_workers_LC = [worker["name"] for worker in DATA if worker ["organization"] == "Platzi"] # List of people who work at Platzi
    adults_LC = [worker ['name'] for worker in DATA if worker ['age'] > 18]                            # List of people of legal age. ""> 18" counts 18 year olds
    old_people_LC = [{**worker, **{'old': worker['age'] > 70}} for worker in DATA]                     # List of all person data. And that at the end a ": True" or ": False" comes out if they are more or less than 70 years old

    # High order functions
    all_python_devs_HOF = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_devs_HOF = list(map(lambda worker: worker['name'], all_python_devs_HOF))                # List of people who use Python
    all_platzi_workers_HOF = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_workers_HOF = list(map(lambda worker: worker['name'], all_platzi_workers_HOF))          # List of people who work at Platzi
    adults_HOF = list(filter(lambda worker: worker["age"] > 18, DATA))
    adults_HOF = list(map(lambda worker: worker["name"], adults_HOF))                                  # List of people of legal age. ""> 18" counts 18 year olds
    old_people_HOF = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))              # List of all person data. And that at the end a ": True" or ": False" comes out if they are more or less than 70 years old
    old_people_HOF2 = list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA))        # PyVer 3.6 to 3.8

    for worker in old_people_HOF:
        print(worker)

if __name__ == '__main__':
    main()