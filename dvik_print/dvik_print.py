# -*- coding: utf8 -*-
from __future__ import division, absolute_import, print_function, unicode_literals

import inspect
import os


class PrettyPrint(object):
    def __init__(self, tab=4, head=2, tail=1, max_str_len=100, filename=None, show_line=False):
        self.tab = tab
        self.head = head
        self.tail = tail
        self.max_str_len = max(10, max_str_len)
        self.filename = os.path.abspath(filename)
        if show_line and self.filename is None:
            raise ValueError('if show_line then filename cannot be None')
        self.show_line = show_line

    def __call__(self, obj, var=None):
        if self.show_line:
            if self.filename is None:
                raise ValueError('if show_line then filename cannot be None')
            print('{}:{}'.format(self.filename, inspect.currentframe().f_back.f_lineno))
        if var is None:
            pref = ''
        else:
            pref = '{} = '.format(var)
        self._parse(obj, 0, pref=pref, nested=False)

    def _parse(self, obj, next_tab, pref='', nested=True):
        if isinstance(obj, dict):
            self._parse_dict(obj, next_tab, pref=pref, nested=nested)
        elif isinstance(obj, list):
            self._parse_list(obj, next_tab, pref=pref, nested=nested)
        elif isinstance(obj, set):
            self._parse_set(obj, next_tab, pref=pref, nested=nested)
        elif isinstance(obj, tuple):
            self._parse_tuple(obj, next_tab, pref=pref, nested=nested)
        else:
            self._parse_non_iterable(obj, next_tab, pref=pref, nested=nested)

    def _parse_dict(self, obj, curr_tab, pref, nested):
        next_tab = curr_tab + self.tab
        c_shift = curr_tab * ' '
        n_shift = next_tab * ' '

        print('{}{}'.format(c_shift, pref) + '{')

        if len(obj) <= self.head + self.tail:
            for k in obj:
                v = obj[k]
                self._parse(v, next_tab, '{}: '.format(repr(k)))
        else:
            for k in list(obj.keys())[:self.head]:
                v = obj[k]
                self._parse(v, next_tab, '{}: '.format(repr(k)))
            print('{}...'.format(n_shift))
            if self.tail > 0:
                for k in list(obj.keys())[-self.tail:]:
                    v = obj[k]
                    self._parse(v, next_tab, '{}: '.format(repr(k)))

        print(c_shift + '}' + (',' if nested else ''))

    def _parse_list(self, obj, curr_tab, pref, nested):
        next_tab = curr_tab + self.tab
        c_shift = curr_tab * ' '
        n_shift = next_tab * ' '

        print('{}{}'.format(c_shift, pref) + '[')

        if len(obj) <= self.head + self.tail:
            for v in obj:
                self._parse(v, next_tab)
        else:
            for v in obj[:self.head]:
                self._parse(v, next_tab)
            print('{}...'.format(n_shift))
            if self.tail > 0:
                for v in obj[-self.tail:]:
                    self._parse(v, next_tab)

        print(c_shift + ']' + (',' if nested else ''))

    def _parse_set(self, obj, curr_tab, pref, nested):
        next_tab = curr_tab + self.tab
        c_shift = curr_tab * ' '
        n_shift = next_tab * ' '
        obj = list(obj)

        print('{}{}'.format(c_shift, pref) + '{')

        if len(obj) <= self.head + self.tail:
            for v in obj:
                self._parse(v, next_tab)
        else:
            for v in obj[:self.head]:
                self._parse(v, next_tab)
            print('{}...'.format(n_shift))
            if self.tail > 0:
                for v in obj[-self.tail:]:
                    self._parse(v, next_tab)

        print(c_shift + '}' + (',' if nested else ''))

    def _parse_tuple(self, obj, curr_tab, pref, nested):
        next_tab = curr_tab + self.tab
        c_shift = curr_tab * ' '
        n_shift = next_tab * ' '

        print('{}{}'.format(c_shift, pref) + '(')

        if len(obj) <= self.head + self.tail:
            for v in obj:
                self._parse(v, next_tab)
        else:
            for v in obj[:self.head]:
                self._parse(v, next_tab)
            print('{}...'.format(n_shift))
            if self.tail > 0:
                for v in obj[-self.tail:]:
                    self._parse(v, next_tab)

        print(c_shift + ')' + (',' if nested else ''))

    def _parse_non_iterable(self, obj, curr_tab, pref, nested):
        shift = ' ' * curr_tab
        print('{}{}{}'.format(shift, pref, self._limited_str(obj)) + (',' if nested else ''))

    def _limited_str(self, obj):
        obj = repr(obj)
        if self.max_str_len == 0 or self.max_str_len is None:
            return obj
        elif len(obj) > self.max_str_len:
            return '{}...{}'.format(obj[:self.max_str_len - 5], obj[-2:])
        else:
            return obj


if __name__ == '__main__':
    import datetime as dt

    # mamy obiekt o

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

    # deklarujemy obiekt dvp.PrettyPrint`
    pp = PrettyPrint(tab=2, head=3, tail=2, max_str_len=50)

    # obiekt jest wywoływalny
    # w ten sposób wypisze na
    # standardowe wyjście obiekt O
    pp(O, var='zmienna')

    # można użyć wartości domyślnych
    pp_domyslny = PrettyPrint()
    pp_domyslny(O)
