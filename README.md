# Postup vypnutia a zapnutia FV systému
## GoodWe GW10KN‑ET + Pylontech Force H2 (4 moduly) + 2× PV string

---

## 1. Regulérne vypnutie systému

| Krok | Úkon | Popis / Dôvod |
|------|------|----------------|
| **1** | **Vypnúť striedač GoodWe (hlavný vypínač → OFF)** | Zastaví výrobu a nabíjanie. Počkať 20–30 sekúnd, kým zhasnú LED. |
| **2** | **Vypnúť hlavný 3‑fázový AC istič** | Odpojí striedač od siete aj od domu. |
| **3** | **Vypnúť DC stringy (PV1 a PV2 → OFF)** | Odpojí panely od striedača, zabráni spätnému napätiu. |
| **4** | **Vypnúť batériu Pylontech Force H2 (master modul → OFF)** | Bezpečne vypne HV batériu. Počkať 10–20 sekúnd na zhasnutie LED. |

---

## 2. Regulérne zapnutie systému

| Krok | Úkon | Popis / Dôvod |
|------|------|----------------|
| **1** | **Zapnúť batériu Pylontech Force H2 (master modul → ON)** | GoodWe musí batériu vidieť ako prvú. Počkať 10–20 sekúnd na inicializáciu BMS. |
| **2** | **Zapnúť hlavný 3‑fázový AC istič** | Striedač dostane napájanie zo siete. AC musí byť aktívne skôr než DC. |
| **3** | **Zapnúť DC stringy (PV1 a PV2 → ON)** | Panely sa pripájajú až po AC, aby MPPT štartoval správne. |
| **4** | **Zapnúť striedač GoodWe (hlavný vypínač → ON)** | Striedač sa inicializuje, načíta batériu a spustí výrobu. |

---

## Poznámky pre bezpečnú prevádzku

- Nikdy neodpájajte HV konektory batérie.
- GoodWe ET musí pri štarte vidieť batériu aj AC, inak hlási chyby.
- DC stringy sa zapínajú až po AC, aby MPPT neštartoval „naslepo“.
- Tento postup je vhodný pre servis, údržbu aj dlhodobé odstavenie.
