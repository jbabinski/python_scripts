"""
* Assignment: OOP Relations Flatten
* Complexity: medium
* Lines of code: 5 lines
* Time: 13 min

English:
    1. How to write relations to CSV file (contact has many addresses)?
    2. Convert `DATA` to `resul: list[dict[str,str]]`
    3. Non-functional requirements:
        a. Use `,` to separate fields
        b. Use `;` to separate columns
    4. Run doctests - all must succeed

Polish:
    1. Jak zapisać w CSV dane relacyjne (kontakt ma wiele adresów)?
    2. Przekonwertuj `DATA` do `resul: list[dict[str,str]]`
    3. Wymagania niefunkcjonalne:
        b. Użyj `,` do oddzielenia pól
        b. Użyj `;` do oddzielenia kolumn
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'firstname': 'Jan', 'lastname': 'Twardowski', 'missions': '1967,Apollo 1;1970,Apollo 13;1973,Apollo 18'},
     {'firstname': 'Ivan', 'lastname': 'Ivanovic', 'missions': '2023,Artemis 2;2024,Artemis 3'},
     {'firstname': 'Mark', 'lastname': 'Watney', 'missions': '2035,Ares 3'},
     {'firstname': 'Melissa', 'lastname': 'Lewis', 'missions': ''}]
"""

class Astronaut:
    def __init__(self, firstname, lastname, missions=()):
        self.firstname = firstname
        self.lastname = lastname
        self.missions = list(missions)


class Mission:
    def __init__(self, year, name):
        self.year = year
        self.name = name


DATA = [
    Astronaut('Jan', 'Twardowski', missions=[
        Mission('1967', 'Apollo 1'),
        Mission('1970', 'Apollo 13'),
        Mission('1973', 'Apollo 18')]),

    Astronaut('Ivan', 'Ivanovic', missions=[
        Mission('2023', 'Artemis 2'),
        Mission('2024', 'Artemis 3')]),

    Astronaut('Mark', 'Watney', missions=[
        Mission('2035', 'Ares 3')]),

    Astronaut('Melissa', 'Lewis')]


# list[dict]: Convert DATA.
#             Use `,` to separate fields.
#             Use `;` to separate columns.
result = []

for astronaut in DATA:
    astronaut = vars(astronaut)
    missions = [','.join(vars(mission).values())
                for mission in astronaut.pop('missions')]
    astronaut['missions'] = ';'.join(missions)
    result.append(astronaut)
