# Text styles in ANSI format.
class text :
    end = "\033[0m"

class regular(text) :
    bold = "\033[1m"
    underline = "\033[4m"

    blue = "\033[0;34m"
    cyan = "\033[0;36m"
    green = "\033[0;32m"
    red = "\033[0;31m"
    yellow = "\033[0;33m"

class bold(text) :
    blue = "\033[1;34m"
    cyan = "\033[1;36m"
    green = "\033[1;32m"
    red = "\033[1;31m"
    yellow = "\033[1;33m"

class underline(text) :
    blue = "\033[4;34m"
    cyan = "\033[4;36m"
    green = "\033[4;32m"
    red = "\033[4;31m"
    yellow = "\033[4;33m"

class backgroung(text) :
    classic = "\033[0;30m\033[47m"