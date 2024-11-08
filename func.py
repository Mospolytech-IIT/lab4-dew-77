"""
1
"""

from datetime import datetime

region__payment_methods = {
    'UK': ['PayPal', 'Credit Card', 'Debit card', 'Phone number'],
    'RU': ['Credit Card', 'Debit card', 'Phone number', 'QR'],
}


def book_room(date: str, room_number: str) -> None:
    """Create booking for selected room and date."""
    now = datetime.now()
    formatted_date = datetime.strptime(date, '%m.%d.%y')
    if formatted_date < now:
        raise TypeError('Booking date cannot be in the past')
    print(f'Booking for room {room_number} on {formatted_date} created')


def create_payment(uid: str, payment_type: str, region: str) -> str:
    """Create link for payment with selected payment type."""
    user_region_payment_types = region__payment_methods[region]
    if payment_type not in user_region_payment_types:
        raise TypeError('Unavailable payment type for selected region.')
    url = f'https://NE_SCAM.ru/payment/{hash(uid)}'
    return url
