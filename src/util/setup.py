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

    date = "{B}{M}{R} {P}{D}{p},{R} {B}{Y}{R}".format(
        B=colorama.Fore.BLUE,
        P=colorama.Fore.MAGENTA,


        R=colorama.Fore.RESET,
        p=postfix,

        D=day,
        M=_date.strftime("%B"),
        Y=_date.strftime("%Y"))

    return date
