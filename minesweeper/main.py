from jatek import Jatek
from palya import Palya

new_game = input("Uj jatek?").lower().startswith('y')
Ablak_meret = (800,900)

if new_game:
    akna  = int(input('aknák száma: '))
    mag = int(input('pálya magassága: '))
    szel= int(input('pálya szélessége: '))
    if szel > mag:
        cella = szel
    else:
        cella = mag
    Palya_meret = (mag,szel)
    palya = Palya(Palya_meret,akna).tabla
else:
    palya = []
    cover = []
    with open("cover.txt", "r") as f:
        for sor in f:
            cover.append(list(map(int, sor.strip().split())))
    with open("save.txt", "r") as f:
        for sor in f:
            palya.append(list(map(int, sor.strip().split())))
    akna = sum(sor.count(-1) for sor in palya)
    print(akna)
    mag = len(palya)
    szel = len(palya[0])
    Palya_meret = (mag ,szel)
    # TODO akna
    akna = 5
    if szel > mag:
        cella = szel
    else:
        cella = mag

game = Jatek(palya, Ablak_meret,Palya_meret,akna,cella)
if not new_game:
    game.ures = cover
game.fut()