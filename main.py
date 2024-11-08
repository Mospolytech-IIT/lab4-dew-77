"""
Entrypoint.
"""

from func import book_room, create_payment
from func_with_raise import confirm_email
from func_with_finally import create_report
from func_with_few_exceptions import (
    Account, transfer_between_accounts,
    topup_balance, withdraw_money
)
from func_with_internal_raise_try import create_user_account
from func_with_custom_exceptions import fetch_data
from func_examples import add_to_list, divide, check_env_variable


def run():
    """Functions runner."""
    # Шаг 1
    book_room('12.02.25', 'A232')
    print(create_payment('231', 'PayPal', 'UK'))

    # Шаг 2
    confirm_email('yurkov.artyom21@gmail.com')

    # Шаг 3
    create_report('Oleg', '14.02.24', 'Some cool info xd')

    # Шаг 4
    acc1 = Account(100)
    acc2 = Account(20)
    transfer_between_accounts(user=123, account1=acc1, account2=acc2, total=30)
    topup_balance(user=123, account=acc1, total=200)
    withdraw_money(user=123, account=acc2, total=2, to='Sber')

    # Шаг 5
    create_user_account('Artem', 20)

    # Шаг 6 - exceptions.py
    # Шаг 7
    print(fetch_data('accounts', 1))

    # Шаг 8
    add_to_list(item=23, max_size=3)
    divide(3, 4)
    check_env_variable('HOME')


if __name__ == "__main__":
    # Шаг 9
    run()
