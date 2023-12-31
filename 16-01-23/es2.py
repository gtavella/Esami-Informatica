# Si scriva una funzione verifica_comuni che riceve una lista x di stringhe e un intero k. La funzione restituisce
# una lista definita come segue:
# • se le stringhe contenute in x hanno esattamente k lettere in comune, la lista restituita contiene tali
# lettere (in qualsiasi ordine);
# • altrimenti, la lista restituita è vuota.
# Esempio: Se x = ['abcde','abdcf','bwawc','wcabdf'], verifica_comuni(x,3) restituisce ['a','b','c'], mentre
# verifica_comuni(x,2) restituisce una lista vuota


def verifica_comuni(x,k):
    lettere_comuni=[]
    stringa_campione=x[0]
    for l in stringa_campione:
        if tutte_stringhe_hanno(x[1:], l):
            lettere_comuni.append(l)
    return lettere_comuni if len(lettere_comuni) == k else []


def tutte_stringhe_hanno(lista, l):
    for stringa in lista:
        if l not in stringa:
            return False
    return True



print(verifica_comuni(['abcde','abdcf','bwawc','wcabdf'],3))

