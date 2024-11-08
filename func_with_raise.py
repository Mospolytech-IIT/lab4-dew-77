"""
2. Функция, которая принимает на вход один или несколько параметров.
"""


def validate_email(email: str) -> None:
    """Email validator."""
    if '@' not in email:
        raise ValueError('Incorrect email provided.')


def confirm_email(email: str) -> None:
    """Send code to email."""
    try:
        validate_email(email)
        print('Sent code for confirmation, checkout your inbox.')
    except Exception as e:
        print(f'Error: {e}. Try again.')
