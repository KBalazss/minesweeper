from jatek import Jatek
from palya import Palya

akna  = int(input('aknák száma: '))
Ablak_meret = (800,900)
mag = int(input('pálya magassága: '))
szel= int(input('pálya szélessége: '))
if szel > mag:
    cella = szel
else:
    cella = mag
Palya_meret = (mag,szel)
palya = Palya(Palya_meret,akna).tabla
game = Jatek(palya, Ablak_meret,Palya_meret,akna,cella)
game.fut()





