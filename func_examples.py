"""
8
"""

import os
from typing import Any, Union


def add_to_list(item: Any, max_size: int, items: list = None) -> None:
    """Add items to list with limited size."""
    if items is None:
        items = []
    try:
        if len(items) >= max_size:
            raise OverflowError('Cannot add more items; list is full.')

        items.append(item)
        print(f'Item "{item}" added. Current list: {items}')

    except OverflowError as oe:
        print(f'OverflowError: {oe}')
        print('The list has reached maximum.')


def divide(num1: Union[int, float], num2: Union[int, float]) -> None:
    """Divide num1 by num2."""
    try:
        if not isinstance(num1, (int, float)) or \
             not isinstance(num2, (int, float)):
            raise TypeError('Both nums must be numbers.')

        if num2 == 0:
            raise ZeroDivisionError('Cannot divide by zero.')

        result = num1 / num2
        print(f'Result of division: {result}')

    except TypeError as te:
        print(f'TypeError: {te}')

    except ZeroDivisionError as zde:
        print(f'ZeroDivisionError: {zde}')


def check_env_variable(var_name: str) -> None:
    """Check environment variable and print it."""
    try:
        if var_name not in os.environ:
            raise KeyError(f'The variable "{var_name}" is not set.')

        value = os.environ[var_name]
        print(f'The value of "{var_name}" is: {value}')
        return value

    except TypeError as te:
        print(f'TypeError: {te}')

    except KeyError as ke:
        print(f'KeyError: {ke}')

    except ValueError as ve:
        print(f'ValueError: {ve}')

    finally:
        print('Environment variable check completed.')
