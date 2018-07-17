# -*- coding: utf8 -*-
from __future__ import division, absolute_import, print_function

import os
import sys
import datetime as dt

import dvik_print as dvp

if __name__ == '__main__':
    print(sys.version)

    O = {
        'lista': ['el1', 'el2', 1, 2, 3, 4, None, False],
        'zbiór': {1, 2, 1, 2, 'a', 'a', 'b', 'b'},
        'krotka': ('oto', 'elementy', 'naszej', 'krotki'),
        ('krotka', 'klucz'): {
            'klucz1': ['jakaś', 'lista', 123],
            'klucz2': dt.datetime.now(),
            'klucz3': dt
        },
        (123, 'asd'): {123, 234, 345},
        (123, 'asd1'): (123, 234, 345)
    }

    # deklarujemy obiekt dvp.PrettyPrint
    pp = dvp.PrettyPrint(tab=2, head=3, tail=2, max_str_len=50, show_line=True, filename=__file__)

    # obiekt jest wywoływalny
    # w ten sposób wypisze na
    # standardowe wyjście obiekt O
    pp(O, var='zmienna')

    # można użyć wartości domyślnych
    pp_domyslny = dvp.PrettyPrint()
    pp_domyslny(O)
