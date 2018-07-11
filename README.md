# dvik-print
Funkcja ładnie wypisująca obiekty z możliwością ustawienia wielkości wcięć i limitu pokazywanych kluczy/elementów.

## Użycie

```python
import dvik_print as dvp
import datetime as dt

# mamy obiekt o
o = {
    'lista': ['el1', 'el2', 1, 2, 3, 4, None, False],
    'zbiór': {1, 2, 1, 2, 'a', 'a', 'b', 'b'},
    'krotka': ('oto', 'elementy', 'naszej', 'krotki'),
    ('krotka', 'klucz'): {
        'klucz1': ['jakaś', 'lista', 123],
        'klucz2': dt.datetime.now(),
        'klucz3': dt
    },
}

# deklarujemy obiekt dvp.PrettyPrint`
pp = dvp.PrettyPrint(tab=2, head=3, tail=2, max_str_len=50)

# obiekt jest wywoływalny
# w ten sposób wypisze na standardowe wyjście obiekt o
pp(o, var='zmienna')
```
*wynik:*
```
zmienna = {
  u'krotka': (
    u'oto',
    u'elementy',
    u'naszej',
    u'krotki',
  ),
  u'zbiór': {
    u'a',
    1,
    2,
    u'b',
  },
  u'lista': [
    u'el1',
    u'el2',
    1,
    ...
    None,
    False,
  ],
  (u'krotka', u'klucz'): {
    u'klucz1': [
      u'jakaś',
      u'lista',
      123,
    ],
    u'klucz3': <module 'datetime' (built-in)>,
    u'klucz2': datetime.datetime(2018, 7, 11, 17, 35, 43, 44000),
  },
}
```
Można także zadeklarować bez żadnych parametrów. Wtedy będą użyte wartości domyślne dla klasy ```PrettyPrint```.
```python
pp_domyslny = PrettyPrint()
pp_domyslny(O)
```
*wynik:*
```
{
    u'krotka': (
        u'oto',
        u'elementy',
        ...
        u'krotki',
    ),
    u'zbiór': {
        u'a',
        1,
        ...
        u'b',
    },
    ...
    (u'krotka', u'klucz'): {
        u'klucz1': [
            u'jakaś',
            u'lista',
            123,
        ],
        u'klucz3': <module 'datetime' (built-in)>,
        u'klucz2': datetime.datetime(2018, 7, 11, 17, 39, 22, 528000),
    },
}
```
