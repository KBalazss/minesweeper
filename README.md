# Minesweeper

## Első indítás előtt

- Telepítsd a szükséges csomagokat:
  ```bash
  pip install -r requirements.txt
  ```

- A `best_time.txt` fájlban állítsd be az értéket erre:
  ```txt
  0 0
  ```
  *(ha még nincs beállítva)*

---

## Futtatás

A játék a következő fájl futtatásával indítható:

```bash
python main.py
```

---

## Indítás után

A program konzolban megkérdezi:

- **Új játék**
  - Ha **nem**, akkor a `cover.txt` és a `save.txt` fájlokból betölti az előző játék állását.
  - Ha **igen**:
    - meg kell adni az aknák számát
    - meg kell adni a pálya méreteit

---

## Játékmenet

Ezután a játék egy külön ablakban elindul.

### Irányítás

- **Bal klikk** → az adott mező felfedése
- **Jobb klikk** → mező megjelölése aknaként

---

## Új játék

Az **„Új játék”** gombbal bármikor lehet új játékot kezdeni a megadott paraméterek alapján.

---

## Mentés

Az ablak bezárásával a program leáll.

Ha a játék még nem ért véget, akkor az aktuális játékállás automatikusan elmentődik.