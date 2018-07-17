from setuptools import setup

setup(
    name='dvik-print',
    version='0.3',
    description='Funkcja ładnie wypisująca obiekty z możliwością ustawienia wielkości wcięć i limitu pokazywanych kluczy/elementów.',
    url='https://github.com/aquarioos/dvik-print',
    author='Daniel Taranta',
    author_email='aquarioos@yandex.com',
    license='MIT',
    packages=['dvik_print'],
    zip_safe=False,
    python_requires='>=2.7, !=3.0, !=3.1, !=3.2, !=3.3, !=3.4, !=3.5, <3.7',
)
