
RATES = {"DOM": 3, "COM": 6}
SLAB = {"A": 1, "B": 2}


def units_consumed(reading):
    if not isinstance(reading, str):
        return None
    parts = reading.split(':')
    if len(parts) != 2:
        return None
    try:
        previous, current = map(int, parts)
        return current - previous
    except (ValueError, TypeError):
        return None


def daily_average(units_csv):
    if not isinstance(units_csv, str) or not units_csv.strip():
        return None
    try:
        units = [int(u.strip()) for u in units_csv.split(',')]
        return round(sum(units) / len(units), 2)
    except (ValueError, TypeError, ZeroDivisionError):
        return None


def tariff_rate(code):
    if not isinstance(code, str):
        return None
    parts = code.split('-')
    if len(parts) != 2:
        return None
    category, slab = parts
    try:
        return RATES[category.strip().upper()] * SLAB[slab.strip().upper()]
    except (KeyError, AttributeError):
        return None


def main():
    print("==== Running units_consumed ====")
    print("Units Consumed:", units_consumed(
        input("Enter readings (previous:current): ")))

    print("\n==== Running daily_average ====")
    print("Daily Average:", daily_average(
        input("Enter daily units (CSV): ")))

    print("\n==== Running tariff_rate ====")
    print("Rate per Unit:", tariff_rate(
        input("Enter tariff code (DOM-A): ")))


if __name__ == "__main__":
    main()
