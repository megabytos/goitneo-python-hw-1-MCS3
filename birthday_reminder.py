from datetime import datetime, timedelta
from collections import defaultdict


users = [
    {"name": "Katherine Wagner", "birthday": datetime(year=1975, month=10, day=29)},
    {"name": "Mike Dixon", "birthday": datetime(year=1975, month=10, day=21)},
    {"name": "Bill Gates", "birthday": datetime(year=1955, month=10, day=28)},
    {"name": "Megan Montgomery", "birthday": datetime(year=1955, month=10, day=27)},
    {"name": "Alex Fisher", "birthday": datetime(year=1975, month=10, day=25)},
    {"name": "Robert Sullivan", "birthday": datetime(year=1975, month=10, day=22)},
    {"name": "David Green", "birthday": datetime(year=1975, month=10, day=20)},
    {"name": "Sara Chang", "birthday": datetime(year=1975, month=10, day=25)},
]


def get_birthdays_per_week(users_birthdays):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    week_birthdays = defaultdict(list, {i: [] for i in days_of_week})
    today = datetime.today().date()
    days_to_subtract = {0: 2, 6: 1}
    if today.weekday() in days_to_subtract:  # We must to take the previous weekend
        today = today - timedelta(days=days_to_subtract[today.weekday()])

    for user in users_birthdays:
        birthday_date = user["birthday"].date()
        birthday = birthday_date.replace(year=today.year)
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        delta_days = (birthday - today).days
        if delta_days < 7:
            weekday_num = birthday.weekday()
            # If today is Sunday and birthday in next Saturday
            if (weekday_num == 5 and delta_days == 6):
                continue
            weekday = "Monday" if weekday_num in [5, 6] else birthday.strftime("%A")
            week_birthdays[weekday].append(user["name"])

    for weekday, persons in week_birthdays.items():
        if persons:
            print(f'{weekday}: {", ".join(persons)}')


if __name__ == "__main__":
    get_birthdays_per_week(users)
