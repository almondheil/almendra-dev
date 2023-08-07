from datetime import datetime

"""
Convert from the number of a month to a three-letter abbreviation for that
month. If month is not in range (1, 12), will return "Err."
"""
def num2month(num):
    if num == 1:
        return "Jan"
    elif num == 2:
        return "Feb"
    elif num == 3:
        return "Mar"
    elif num == 4:
        return "Apr"
    elif num == 5:
        return "May"
    elif num == 6:
        return "Jun"
    elif num == 7:
        return "Jul"
    elif num == 8:
        return "Aug"
    elif num == 9:
        return "Sep"
    elif num == 10:
        return "Oct"
    elif num == 11:
        return "Nov"
    elif num == 12:
        return "Dec"
    else:
        return "Err"

"""
Convert from a string start_date and end_date to HTML code that describes the
appropriate time range.

Dates are assumed to be formatted "YYYY-mm-dd" as they are in sqlite3, but
days will be ignored when converting.

Examples.
    in:
        2023-01-01, 2023-03-01
    out:
        <time datetime="2023-01">Jan</time>-<time datetime="2023-03">Mar 2023</time>
    in:
        2023-01-01, 2023-01-01
    out:
        <time datetime="2023-01">Jan 2023</time>
    in:
        2022-10-01, 2023-02-01
    out:
        <time datetime="2022-10">Oct 2022</time>-<time datetime="2023-02">Feb 2023</time>
    in:
        2022-10-01, 2100-10-01
    out:
        <time datetime="2022-10">Oct 2022</time>-<time datetime="present">Present</time>

"""
def dates2range(start_date, end_date):
    # Parse start and end times
    (s_year, s_month, _) = start_date.split('-')
    (e_year, e_month, _) = end_date.split('-')

    # Integer versions of these vars
    s_year_int  = int(s_year)
    e_year_int  = int(e_year)
    s_month_int = int(s_month)
    e_month_int = int(e_month)

    # String versions of the months involved
    s_month_name = num2month(s_month_int)
    e_month_name = num2month(e_month_int)

    # Ends later than now, return Aaa YYYY-Present
    curr_month = datetime.now().month
    curr_year = datetime.now().year
    if (curr_year <= e_year_int and curr_month <= e_month_int):
        result = '<time datetime="{0}-{1}">{2} {0}</time>-<time datetime="present">Present</time>'
        return result.format(s_year, s_month, s_month_name)


    # Two different years, return Aaa YYY1-BBB YYY2
    if (s_year != e_year):
        result = '<time datetime="{0}-{1}">{2} {0}</time>-<time datetime="{3}-{4}">{5} {3}</time>'
        return result.format(s_year, s_month, s_month_name,
                             e_year, e_month, e_month_name)

    # Same year same month, return Aaa YYYY
    if (s_month == e_month):
        result = '<time datetime="{0}-{1}">{2} {0}</time>'
        return result.format(s_year, s_month, s_month_name)

    # Same year different months, return Aaa-Bbb YYYY
    result = '<time datetime="{0}-{1}">{2}</time>-<time datetime="{3}-{4}">{5} {3}</time>'
    return result.format(s_year, s_month, s_month_name,
                         e_year, e_month, e_month_name)


"""
Dates which test each case, left here because who cares
"""
if __name__ == '__main__':
    print(dates2range("2023-01-01", "2023-03-01"))
    print(dates2range("2023-01-01", "2023-01-01"))
    print(dates2range("2022-10-01", "2023-02-01"))
    # If this is still going in 2100 I may have done something wrong
    # This should trigger the "Present" case
    print(dates2range("2022-10-01", "2100-10-01"))
    
