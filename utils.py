"""
Convert from the number of a month to a three-letter abbreviation for that
month. If month is not in range (1, 12), will return "Err."
"""
def num2month(num):
    match num:
        case 1:
            return "Jan"
        case 2:
            return "Feb"
        case 3:
            return "Mar"
        case 4:
            return "Apr"
        case 5:
            return "May"
        case 6:
            return "Jun"
        case 7:
            return "Jul"
        case 8:
            return "Aug"
        case 9:
            return "Sep"
        case 10:
            return "Oct"
        case 11:
            return "Nov"
        case 12:
            return "Dec"
        case _: # default case
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
"""
def dates2range(start_date, end_date):
    # Parse start and end times
    (s_year, s_month, _) = start_date.split('-')
    (e_year, e_month, _) = end_date.split('-')

    s_month_name = num2month(int(s_month))
    e_month_name = num2month(int(e_month))

    # If the dates occur across two years, return "mmm YYYY-mmm YYYY"
    if (s_year != e_year):
        result = '<time datetime="{0}-{1}">{2} {0}</time>-<time datetime="{3}-{4}">{5} {3}</time>'
        return result.format(s_year, s_month, s_month_name,
                             e_year, e_month, e_month_name)

    # If the two dates are the same, return "mmm YYYY"
    if (s_month == e_month):
        result = '<time datetime="{0}-{1}">{2} {0}</time>'
        return result.format(s_year, s_month, s_month_name)

    # Otherwise, the dates occur within one year in different months.
    # return "mmm-mmm YYYY"
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
    
