import datetime
import colorama


def get_date(_date, day=datetime.datetime.now().strftime('%-d')) -> str:
    """
    Return a 🎆 colorized 🎆 version of timestamp
    ts: timestamp (Datetime object)

    return: string
    """
    match int(day):
        case 1:
            postfix = 'st'
        case 2:
            postfix = 'nd'
        case 3:
            postfix = 'rd'
        case _:
            postfix = 'th'

    day = colorama.Fore.MAGENTA + day + postfix + ',' + colorama.Fore.RESET
    month = colorama.Fore.BLUE + _date.strftime("%B") + colorama.Fore.RESET
    year = colorama.Fore.BLUE + _date.strftime("%Y") + colorama.Fore.RESET
    date = f"{month} {day} {year}"

    return date
