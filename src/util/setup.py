import colorama


def get_date(ts) -> str:
    """
    Return a 🎆 colorized 🎆 version of timestamp
    ts: timestamp (Datetime object)

    return: string
    """
    day = ts.strftime("%-d")

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
        M=ts.strftime("%B"),
        Y=ts.strftime("%Y"))

    return date
