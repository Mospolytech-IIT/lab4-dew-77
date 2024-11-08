"""
7
"""

from exceptions import IncorrectTableError

tables = {
    'accounts': ['1, artem, 12r31ete5t32', '2, neartem, 3453g5353g'],
    'costs': ['22.02.2024, 1234, 3532'],
    'revenue': ['2024, 232444.23, gap']
}


def fetch_data(tablename: str, rows: int = 10) -> str:
    """Fetch rows from table."""
    try:
        if tablename not in tables:
            raise IncorrectTableError
    except IncorrectTableError:
        print('Check table name and try again.')
        return ''
    return tables[tablename][:rows]
