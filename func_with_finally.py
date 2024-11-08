"""
3. Функция, которая принимает на вход один или несколько параметров.
"""


class DB:
    """Database imitation."""

    def __init__(self, name) -> None:
        self.name = name
        self.access_users = ['Oleg', 'Denis', 'Artem']
        self.content = []

    def write(self, author: str, report: str) -> None:
        """Add report to provided database instance."""
        print(author)
        if author not in self.access_users:
            raise ConnectionError('Access not allowed.')
        self.content.append(report)

    def connect(self):
        """Start connection."""
        return 0

    def close(self):
        """Close connection."""
        return 1


def create_report(author: id, date: str, text: str) -> None:
    """Create report and send to DB."""
    db = DB('Reports')
    db.connect()
    try:
        text += f'\nDate: {date}'
        db.write(author=author, report=text)
    except Exception as e:
        print(f'Error: {e}')
    finally:
        db.close()
