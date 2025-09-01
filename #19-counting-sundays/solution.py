
def zeller_congruence(year: int, month: int, day: int = 1) -> int:
    """
    Returns the day of the week using Zeller's Congruence.
    0 = Saturday, 1 = Sunday, 2 = Monday, ..., 6 = Friday
    """
    # Adjust for January and February
    # Because, Zeller’s formula starts the year in March
    if month < 3:
        month += 12
        year -= 1

    K = year % 100      # Year within the century
    J = year // 100     # Zero-based century

    h = (day + (13 * (month + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
    return h

def counting_sundays():

    sundays_count = 0

    for year in range(1901, 2001):
        for month in range(1, 13):

            h = zeller_congruence(year, month, 1)
            if h == 1:  # Zeller's formula: 1 = Sunday
                sundays_count += 1

    return sundays_count


sundays_count = counting_sundays()

print(f"The total sundays count is: {sundays_count}")  # Output: 171
