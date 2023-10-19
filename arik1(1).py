from collections import Counter
import os

# Hau izango da gure inputa.
aztertzeko_testua = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCEAX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJTEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPXDIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PENTCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIKHKCZJOI OKEJSZCNHE."
# Testu hau bakarrik hutsik egongo da
hutsune_testua = ""
# Testu honek bakarrik ak izango ditu
prosz_testua = ""
luzera_testua = 0

for c in aztertzeko_testua:
    if c == " " or c == "." or c == ",":
        hutsune_testua = hutsune_testua + c
    elif c.isdigit(): # Zenbakia bada
        hutsune_testua = hutsune_testua + c
    else:
        hutsune_testua = hutsune_testua + "_"
        prosz_testua = prosz_testua + c
        luzera_testua = luzera_testua + 1


def inprimatu():
    print("Testuaren karaktere kopurua: ", luzera_testua)
    letters = Counter(prosz_testua)
    print(letters)
    print("\n")
    print(hutsune_testua)
    print("\n")
    print(aztertzeko_testua)
    print("\n")


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# a, b-ren ordez ordezkatu, aztertzeko matrizea kontuan izanda
def ordezkatu(a, b):
    mut_hutsune_testua = list(hutsune_testua)

    for i, char in enumerate(aztertzeko_testua):
        if char == a:
            mut_hutsune_testua[i] = b
    
    berria = ''.join(mut_hutsune_testua)
    return berria


jarraitu = True
inprimatu()
while jarraitu == True:
    a = input("Ordezkatzeko letra: ")
    b = input("Zeren ordez? ")
    if a == "exit" or b == "exit":
        jarraitu = False
    elif len(a) == 1 and len(b) == 1 and a.isalpha() and b.isalpha():
        hutsune_testua = ordezkatu(a, b)
        clear()
        inprimatu()


# hutsune_testua = ordezkatu("X", "E")
# hutsune_testua = ordezkatu("E", "A")
# hutsune_testua = ordezkatu("K", "R")
# hutsune_testua = ordezkatu("A", "D")
# hutsune_testua = ordezkatu("I", "O")
# hutsune_testua = ordezkatu("V", "Y")
# hutsune_testua = ordezkatu("J", "N")
# hutsune_testua = ordezkatu("P", "M")
# hutsune_testua = ordezkatu("V", "Y")
# hutsune_testua = ordezkatu("v", "V")
# hutsune_testua = ordezkatu("C", "I")
# hutsune_testua = ordezkatu("Q", "B")
# hutsune_testua = ordezkatu("T", "L")
# hutsune_testua = ordezkatu("Z", "U")
# hutsune_testua = ordezkatu("R", "C")
# hutsune_testua = ordezkatu("N", "S")
# hutsune_testua = ordezkatu("D", "P")
# hutsune_testua = ordezkatu("O", "F")
# hutsune_testua = ordezkatu("H", "T")
# hutsune_testua = ordezkatu("S", "Q")
# hutsune_testua = ordezkatu("L", "Z")
# hutsune_testua = ordezkatu("G", "J")
# hutsune_testua = ordezkatu("U", "G")
# hutsune_testua = ordezkatu("M", "H")

# inprimatu()