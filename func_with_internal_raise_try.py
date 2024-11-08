"""
5. Функция, которая принимает на вход один или несколько параметров.
"""

from func_with_finally import DB

postgres = DB('PostgreSQL')


def create_user_account(username: str, age: int) -> None:
    """Create account for user with provided age"""
    postgres.connect()
    try:
        if not isinstance(username, str) or len(username) < 3:
            raise ValueError('Username must be a string with >3 characters.')

        if not isinstance(age, int) or age < 18:
            raise ValueError('Age must be an integer and at least 18.')

        print('User account created successfully!')

    except ValueError as ve:
        print(f'ValueError: {ve}')
        print('Please check your input values.')

    except TypeError as te:
        print(f'TypeError: {te}')
        print('Input data has incorrect type.')

    except Exception as e:
        print(f'Unexpected error: {e}')
        print('An unexpected error occurred. Please contact support.')
    else:
        postgres.write(username, '1234')
    finally:
        postgres.close()
