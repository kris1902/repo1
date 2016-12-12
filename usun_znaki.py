from string import ascii_lowercase as al

def zostaw_alfabet(tekst):
    """funkcja usuwa wszystkie znaki spoza alfabetu EN"""
    assert isinstance(tekst, str)
    tekst = tekst.lower()
    ret = ""
    for znak in tekst:
        if znak in al or znak == " ":
            ret += znak
    return ret


def usun_nadmierne_spacje(tekst):
    """funkcja usuwa nadmiarowe spacje ze zmiennej STR tekst"""
    while "  " in tekst:
        tekst = tekst.replace("  ", " ")
    return tekst


if __name__ == "__main__":
    with open('lorem.txt', 'r') as f:
        txt = f.read()
        print txt
        txt = zostaw_alfabet(txt)
        print txt
        txt = usun_nadmierne_spacje(txt)
        print txt
