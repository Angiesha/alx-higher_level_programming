===========================
How to Use 3-say_my_name.py
===========================

This modules defines a function ``say_my_name(first_name, last_name="")``.

Usage
=====

``say_my_name(...)`` prints "My name is <first_name> <last_name>".

::

    >>> say_my_name = __import__('3-say_my_name').say_my_name
    >>> say_my_name("Angela", "Crabs")
    My name is Angela Crabs

::

    >>> say_my_name("Bill Gates", "Bennie")
    My name is Bill Gates Bennie

The parameter ```last_name``` is optional. If no last name is provided,
an empty string is printed instead.

::

    >>> say_my_name("Angela")
    My name is Angela

Invalid Names
=============

The parameters ``first_name`` and ``last_name``` must be strings. Otherwise,
a TypeError is raised.

::

    >>> say_my_name(6, "Ronaldo")
    Traceback (most recent call last):
    TypeError: first_name must be a string

::

    >>> say_my_name("Cristiano", ["Jimin", "Jungkook", "Angie"])
    Traceback (most recent call last):
    TypeError: last_name must be a string

::

    >>> say_my_name({"Cristiano": 6, "Ronaldo": 37}, 6.1)
    Traceback (most recent call last):
    TypeError: first_name must be a string

::

    >>> say_my_name(None)
    Traceback (most recent call last):
    TypeError: first_name must be a string

At least one name must be provided.

::

    >>> say_my_name()
    Traceback (most recent call last):
    TypeError: say_my_name() missing 1 required positional argument: 'first_name'
