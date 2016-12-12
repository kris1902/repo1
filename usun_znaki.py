from string import ascii_lowercase as al

def zostaw_alfabet(tekst):
    """funkcja usuwa wszystkie znaki spoza alfabetu EN"""
    ret = ""
    for znak in tekst:
        if znak in al or znak == " ":
            ret += znak
    return ret


def usun_nadmierne_spacje(tekst):
    """funkcja usuwa nadmiarowe spacje ze zmiennej STR tekst"""
    while "  " in tekst:
        tekst.replace("  ", " ")
    return tekst


if __name__ == "__main__":
    from loremipsum import get_sentences
    lista = get_sentences(10)
    print lista
