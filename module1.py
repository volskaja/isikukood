def Sugu(ik_list:list)->str:
    """Esimise tahe j�rgi m��rame sugu
    :param list ik_list: J�rjend isikukoodi numbridest
    :rtype: str
    """
    if int(ik_list[0])%2==0:
        sugu="naine"
    else:
        sugu="mees"
    return sugu

def Sunnikoht(a:int)->str:
    """
    """
    if 1<=a<=10:
        haigla="kuresaare Haigla"
    elif 11<=a<=19:
        haigla="Tartu �likooli Naistekliinik, Tartumaa, Tartu"
    elif 21<=a<=220:
        haigla="Ida-Tallinna Keskhaigla, Pelgulinna s�nnitusmaja, Hiiumaa, Keila, Rapla haigla, Loksa haigla"
    else:
        haigla=" ---"
    return haigla