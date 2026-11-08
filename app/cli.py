import argparse
from datetime import datetime

from app.application.search import search


def print_records(records):
    if not records:
        print("Нічого не знайдено.")
        return

    print(f"Знайдено записів: {len(records)}\n")
    for r in records:
        print(f"Країна:        {r['country']}")
        print(f"Оновлено:      {r['last_updated']:%Y-%m-%d %H:%M}")
        print(f"Схід сонця:    {r['sunrise']:%H:%M}")
        print(f"Вітер:         {r['wind_kph']} км/год, {r['wind_degree']}°, {r['wind_direction']}")
        print(f"Виходити:      {'так' if r['go_outside'] else 'ні'}")
        print("-" * 40)


def main():
    parser = argparse.ArgumentParser(prog="app.cli")
    sub = parser.add_subparsers(dest="command", required=True)

    s = sub.add_parser("search", help="Пошук погоди за країною і датою")
    s.add_argument("--country", required=True, help="Назва країни, як у CSV")
    s.add_argument("--date", required=True, help="Дата у форматі YYYY-MM-DD")

    args = parser.parse_args()

    if args.command == "search":
        try:
            date = datetime.strptime(args.date, "%Y-%m-%d")
        except ValueError:
            print("Неправильний формат дати. Потрібно YYYY-MM-DD, наприклад 2024-05-16.")
            return
        print_records(search(args.country, date))


if __name__ == "__main__":
    main()