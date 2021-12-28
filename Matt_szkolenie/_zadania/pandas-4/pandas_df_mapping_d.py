"""
* Assignment: DataFrame Mapping Substitute
* Complexity: medium
* Lines of code: 10 lines
* Time: 8 min

English:
    1. Read data from `DATA` as `df: pd.DataFrame`
    2. Select `Polish` spreadsheet
    3. Set header and index to data from file
    4. Mind the encoding
    5. Substitute Polish Diacritics to English alphabet letters
    6. Compare `df.replace(regex=True)` with `df.applymap()`
    7. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `df: pd.DataFrame`
    2. Wybierz arkusz `Polish`
    3. Ustaw nagłówek i index na dane zaczytane z pliku
    4. Zwróć uwagę na encoding
    5. Podmień polskie znaki diakrytyczne na litery z alfabetu angielskiego
    6. Porównaj `df.replace(regex=True)` z `df.applymap()`
    7. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> pd.set_option('display.width', 500)
    >>> pd.set_option('display.max_columns', 3)
    >>> pd.set_option('display.max_rows', 10)
    >>> result  # doctest: +NORMALIZE_WHITESPACE
                                                 Definicja  ...                                 Kryteria wyjsciowe
    TRL                                                     ...
    1    Zaobserwowanie i opisanie podstawowych zasad d...  ...  Zweryfikowane publikacja badania lezacych u po...
    2    Sformulowanie koncepcji technologicznej lub pr...  ...  Udokumentowany opis aplikacji / koncepcji, kto...
    3    Przeprowadzanie eksperymentalnie i analityczni...  ...  Udokumentowane wyniki analityczne / eksperymen...
    4    Przeprowadzenie weryfikacji komponentow techno...  ...  Udokumentowane wyniki testow potwierdzajace zg...
    5    Przeprowadzenie weryfikacji komponentow techno...  ...  Udokumentowane wyniki testow potwierdzajace zg...
    6    Dokonanie demonstracji technologii w srodowisk...  ...  Udokumentowane wyniki testow potwierdzajace zg...
    7    Dokonanie demonstracji prototypu systemu w oto...  ...  Udokumentowane wyniki testow potwierdzajace zg...
    8    Zakonczenie badan i demonstracja ostatecznej f...  ...  Udokumentowane wyniki testow weryfikujacych pr...
    9    Weryfikacja technologii w srodowisku operacyjn...  ...            Udokumentowane wyniki operacyjne misji.
    <BLANKLINE>
    [9 rows x 4 columns]
"""

import pandas as pd


DATA = 'https://python.astrotech.io/_static/astro-trl.xlsx'
LETTERS_PLEN = {'ą': 'a', 'ć': 'c', 'ę': 'e',
                'ł': 'l', 'ń': 'n', 'ó': 'o',
                'ś': 's', 'ż': 'z', 'ź': 'z'}

result = ...
