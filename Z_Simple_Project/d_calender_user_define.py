import calendar as c


def generate_calendar(year):
    cal = c.TextCalendar(c.SUNDAY)
    calendar_str = cal.formatyear(year, 2, 1, 1, 3)
    return calendar_str


def main():
    try:
        year = int(
            input("Enter the year for which you want to generate the calendar: ")
        )
        if year > 0:
            print("\nCalendar for the year", year, ":\n")
            print(generate_calendar(year))
        else:
            print("Please enter a valid positive integer for the year.")
    except ValueError:
        print("Please enter a valid positive integer for the year.")


if __name__ == "__main__":
    main()
