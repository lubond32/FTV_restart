## Postup vypnutia a zapnutia FV systému
**FV konfigurácia:**
- Striedač GoodWe GW10KN‑ET
- Batériové úložisko Pylontech Force H2 (4 moduly)
- panely 2× PV string

---
<br>
Pre odpojenie domu od verejne siete (GRID) treba v rozvádzačí vypnúť hlavný vypínač:  

| Kde  | Úkon  | Popis / Dôvod   |
|:-----|:------|:----------------|
| HLAVNÝ ROZVÁDZAČ | Vypnúť hlavný vypínač **QM** | Odpojí domový rozvádzač od verejnej siete, dom zostane napájaný z FOTOVOLTIKY ! |

<span style="color:red; font-weight:bold; ">VYPNUTÍM HLAVNÉHO VYPÍNAČA ZOSTÁVA ROZVÁDZAČ A VŠETKY VETVY DOMU POD NAPATÍM !<br>PRE ÚPLNÉ ODPOJENIE DOMU OD ELEKTRIKY TREBA ODPOJIŤ AJ FOTOVOLTIKU !</span>  


## 1. Regulérne vypnutie FV systému

| Krok  | Kde  | Úkon  | Popis / Dôvod   |
|:------|:-----|:------|:----------------|
| **1** | HLAVNÝ ROZVÁDZAČ | Vypnúť GRID istič striedača **FA1**. | Odpojí striedač od verejenej siete (GRID). |
| **2** | HLAVNÝ ROZVÁDZAČ | Vypnúť BACKUP výstup striedača **FA4**. | Odpojí striedač od zálohovanej (BACKUP) vetvy rozvádzača. Tým sa vypne aj celé domové osvetlenie. |
| **3** | BATÉRIA<br>bočný panel | Vypnúť **istič na batérii**, istič pod krytkou. | Odpojí batériu od DC vstupu striedača, zabráni spätnému napätiu od batérie. |
| **4** | STRIEDAČ<br>zospodu vľavo | Vypnúť **otočný DC vypínač**, otočiť proti smeru hod. ručičiek. | Odpojí striedač od DC zdrojov. |
| **5** | ROZVÁDZAČ<br>DC FTV<br>nad striedačom| Vypnúť **poistky stringov** panelov PV1 a PV2, odkopiť držiaky poistiek. | Odpojí PV panely od DC vstupu striedača, zabráni spätnému napätiu od panelov. |

## 2. Regulérne zapnutie FV systému

Ak je vypnutý hlavný vypínač:  

| Kde  | Úkon  | Popis / Dôvod   |
|:-----|:------|:----------------|
| HLAVNÝ ROZVÁDZAČ | Zapnúť hlavný vypínač **QM** | Pripojí hlavný domový rozvádzač k verejnej sieti (GRID) - nabehne nezálohovaná vetva domu.|

| Krok  | Kde  | Úkon  | Popis / Dôvod   |
|:------|:-----|:------|:----------------|
| **1** | HLAVNÝ ROZVÁDZAČ | Zapnúť BACKUP istič striedača **FA4**, označenie *BACKUP VYSTUP*. | Pripojí BACKUP AC výstup striedača k zálohovanej vetve domu.|
| **2** | HLAVNÝ ROZVÁDZAČ | Zapnúť GRID istič striedača **FA1**, označenie *GRID VYSTUP*. | Pripojí AC vstup striedača k verejenej sieti (GRID). Striedač začne svietiť a nabiehať. Ak je GRID, pôjde už aj osvetlenie.|
| **3** | BATÉRIA<br>bočný panel | Zapnúť **istič na batérii** (pod krytkou) a potom **podržať 5 sek stlačené tlačítko START**| Zapne batériu a pripojí ju k DC vstupu striedača. |
| **4** | ROZVÁDZAČ<br>DC FTV<br>nad striedačom| Zapnúť **poistky stringov** panelov PV1 a PV2, zaklopiť držiaky poistiek. | Pripojí PV panely k DC vstupu striedača. |
| **5** | STRIEDAČ<br>spodný panel | Zapnúť **DC vypínač**, otočiť v smere hod. ručičiek. | Pripojí DC zdroje (BAT + PV) ku striedaču. Striedač nabieha niekolko sekúnd. Ak nebol GRID, nabehne aj osvetlenie.|

---

## Poznámky pre bezpečnú prevádzku

- Nikdy neodpájajte HV konektory batérie a PV stringov (vysoké napätie).
- GoodWe ET musí pri štarte vidieť batériu aj AC, inak hlási chyby.
- PV stringy sa zapínajú až po AC (krok 1), aby MPPT neštartoval „naslepo“.
- Tento postup je vhodný pre servis, údržbu aj dlhodobé odstavenie.
