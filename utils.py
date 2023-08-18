from datetime import datetime

"""
Convert from a string start_date and end_date to HTML code that describes the
appropriate time range.

Dates are assumed to be formatted "YYYY-mm-dd" as they are in sqlite3.

args:
    start_datestr: string representation of start time, YYYY-mm-dd
    end_datestr: string representation of end time, YYYY-mm-dd
returns:
    valid HTML describing the time range provided (see below)

output possibilities
    MMM is the abbreviation of the current month %b (Jan-Dec)
    YYYY is simply the full year

    End date today or in the future:
        MMM YYYY-Present

    Same month of the same year:
        MMM YYYY

    Different months of the same year:
        MMM-MMM YYYY

    Different months of different years:
        MMM YYYY-MMM YYYY
"""
def dates2range(start_datestr: str, end_datestr: str) -> str:
    # Store start and end as the provided values, but add a time of 23:59:59 to ensure
    # that (now <= end) will be true if today is the day of end
    start = datetime.strptime(start_datestr + " 23:59:59", "%Y-%m-%d %H:%M:%S").date()
    end = datetime.strptime(end_datestr + " 23:59:59", "%Y-%m-%d %H:%M:%S").date()
    now = datetime.now().date()

    # String versions of the months involved
    start_month_name = datetime.strftime(start, '%b')
    end_month_name = datetime.strftime(end, '%b')

    if (now <= end): 
        result = '<time datetime="{0}-{1}">{2} {0}</time>-<time datetime="present">Present</time>'
        return result.format(start.year, start.month, start_month_name)

    elif (start.year != end.year):
        result = '<time datetime="{0}-{1}">{2} {0}</time>-<time datetime="{3}-{4}">{5} {3}</time>'.format(
            start.year, start.month, start_month_name,
            end.year, end.month, end_month_name)

    elif (start.month == end.month):
        result = '<time datetime="{0}-{1}">{2} {0}</time>'.format(
            start.year, start.month, start_month_name)

    else:
        result = '<time datetime="{0}-{1}">{2}</time>-<time datetime="{3}-{4}">{5} {3}</time>'.format(
            start.year, start.month, start_month_name,
            end.year, end.month, end_month_name)

    return result
