"""
4
"""

from exceptions import (
    ZeroTotalError, NegativeTotalError,
    UserDoesNotExistsError, ZeroBalanceError
)

USER_IDS = [123, 124, 125]


class Account:
    """User's account."""
    def __init__(self, initial_balance) -> None:
        self.balance = initial_balance

    def add(self, total: int) -> None:
        """Increase balance with provided sum."""
        self.balance += total


class Transaction:
    """Transaction imitation."""

    def start(self):
        """Start transaction."""
        return 1

    def process(self):
        """Process something =)"""
        return 1

    def close(self):
        """Close transaction."""
        return 0


def validate_total(total: int) -> None:
    """Validator of money total."""
    if total == 0:
        raise ZeroTotalError
    elif total < 0:
        raise NegativeTotalError


def validate_withdraw(account: Account, to_withdraw: int) -> None:
    """Validate withdraw ability for account."""
    if account.balance < to_withdraw:
        raise ValueError


def user_exists(user_id: int) -> None:
    """Validate existence of user."""
    if user_id not in USER_IDS:
        raise UserDoesNotExistsError


def validate_balance_for_transfer(account: Account) -> None:
    """Balance validator."""
    if account.balance <= 0:
        raise ZeroBalanceError


def transfer_between_accounts(
        user: int, account1: Account, account2: Account, total: int
        ) -> None:
    """Functiom to create transfer beetween 2 accounts."""
    tr = Transaction()
    try:
        tr.start()
        validate_total(total)
        user_exists(user_id=user)
        validate_balance_for_transfer(account1)
    except UserDoesNotExistsError:
        print(f'User {user} does not exists.')
    except ZeroTotalError:
        print('You cant transfer 0 rub.')
    except NegativeTotalError:
        print('You cant transfer negative values.')
    except ZeroBalanceError:
        print('You have zero balance on your account.')
    else:
        account2.add(total)
        tr.process()
    finally:
        tr.close()


def topup_balance(user: int, account: Account, total: int) -> None:
    """Top up balance on account."""
    tr = Transaction()
    try:
        tr.start()
        validate_total(total)
        user_exists(user_id=user)
    except UserDoesNotExistsError:
        print(f'User {user} does not exists.')
    except ZeroTotalError:
        print('You cant transfer 0 rub.')
    except NegativeTotalError:
        print('You cant transfer negative values.')
    else:
        account.add(total)
        tr.process()
    finally:
        tr.close()


def withdraw_money(user: int, account: Account, total: int, to: str) -> None:
    """Withdraw money from account to provided location."""
    tr = Transaction()
    try:
        tr.start()
        validate_total(total)
        user_exists(user_id=user)
        validate_withdraw(account, total)
    except UserDoesNotExistsError:
        print(f'User {user} does not exists.')
    except ZeroTotalError:
        print('You cant transfer 0 rub.')
    except NegativeTotalError:
        print('You cant transfer negative values.')
    except ValueError:
        print('Not enought money to withdraw.')
    print(f'Money withdrawed to {to}')
