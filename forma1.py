"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Melyik versenyző nyerte a legkevesebb futamot?
4. Ki teljesítette a legtöbb futamot?
5. Átlagosan hány futamot teljesítettek a versenyzők?"

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik csapat szerezte a legtöbb futamgyőzelmet?

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""

f1emberek = []
with open('beolvasando_adatok/f1.txt', 'r', encoding='utf-8') as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        ember = {'nev': adatok[0],
                'csapat': adatok[1],
                'gyozelmek': int(adatok[2]),
                'futamok': int(adatok[3])}
        f1emberek.append(ember)

print(f'{f1emberek=}')
    
 #1. feladat
print(f"1. A beolvasott fájlban összesen {len(f1emberek)} versenyző szerepel.")

#2. feladat

legtobbgyoz = f1emberek[0]['gyozelmek']
legtobbgyoz_versenyzo = f1emberek[0]['nev']

for ember in f1emberek:
    if ember['gyozelmek'] > legtobbgyoz:
        legtobbgyoz = ember['gyozelmek']
        legtobbgyoz_versenyzo = ember['nev']

print(f"2. A legtöbb futamot nyert versenyző: {legtobbgyoz_versenyzo}")

#3.feladat

legkevgyoz = f1emberek[0]['gyozelmek']
legkevgyoz_versenyzo = f1emberek[0]['nev']

for ember in f1emberek:
    if ember['gyozelmek'] < legkevgyoz:
        legkevgyoz = ember['gyozelmek']
        legkevgyoz_versenyzo = ember['nev']

print(f"3. A legkevesebb futamot nyert versenyző: {legkevgyoz_versenyzo}")


#4. feladat
legfutam = f1emberek[0]['futamok']
legfutam_versenyzo = f1emberek[0]['nev']

for ember in f1emberek:
    if ember['futamok'] > legfutam:
        legfutam = ember['futamok']
        legfutam_versenyzo = ember['nev']

print(f"4. A legtöbb futamot teljesített versenyző: {legfutam_versenyzo}")

#5.feladat
csak_futamok = []
for ember in f1emberek:
    csak_futamok.append(ember['futamok'])

atlag_futam = sum(csak_futamok) / len(csak_futamok)
kerekitett_a_f = round(atlag_futam, 2)

print(f"5. Az átlagos futamszám: {kerekitett_a_f}")


#szorgalmi feladat
sumok = []

nevuk_f = []
csapat_f= []
szamolo_f = []
for ember in f1emberek:
    if ember['csapat'] == 'Ferrari':
        csapat_f.append(ember['gyozelmek'])
szamolo_f.append(sum(csapat_f))
nevuk_f.append(ember['csapat'])
sumok.append(szamolo_f)


nevuk_ml = []
csapat_ml= []
szamolo_ml = []
for ember in f1emberek:
    if ember['csapat'] == 'McLaren':
        csapat_ml.append(ember['gyozelmek'])
szamolo_ml.append(sum(csapat_ml))
nevuk_ml.append(ember['csapat'])
sumok.append(szamolo_ml)

nevuk_r = []
csapat_r= []
szamolo_r = []
for ember in f1emberek:
    if ember['csapat'] == 'Renault':
        csapat_r.append(ember['gyozelmek'])
szamolo_r.append(sum(csapat_r))
nevuk_r.append(ember['csapat'])
sumok.append(szamolo_r)

nevuk_m = []
csapat_m= []
szamolo_m = []
for ember in f1emberek:
    if ember['csapat'] == 'Mercedes':
        csapat_m.append(ember['gyozelmek'])
szamolo_m.append(sum(csapat_m))
nevuk_m.append(ember['csapat'])
sumok.append(szamolo_m)

nevuk_w = []
csapat_w= []
szamolo_w = []
for ember in f1emberek:
    if ember['csapat'] == 'Williams':
        csapat_w.append(ember['gyozelmek'])
szamolo_w.append(sum(csapat_w))
nevuk_w.append(ember['csapat'])
sumok.append(szamolo_w)

nevuk_bgp = []
csapat_bgp= []
szamolo_bgp = []
for ember in f1emberek:
    if ember['csapat'] == 'Brawn GP':
        csapat_bgp.append(ember['gyozelmek'])
szamolo_bgp.append(sum(csapat_bgp))
nevuk_bgp.append(ember['csapat'])
sumok.append(szamolo_bgp)


nevuk_rb = []
csapat_rb= []
szamolo_rb = []
for ember in f1emberek:
    if ember['csapat'] == 'Red Bull':
        csapat_rb.append(ember['gyozelmek'])
szamolo_rb.append(sum(csapat_rb))
nevuk_rb.append(ember['csapat'])
sumok.append(szamolo_rb)

nevuk_b = []
csapat_b= []
szamolo_b = []
for ember in f1emberek:
    if ember['csapat'] == 'Brabham':
        csapat_b.append(ember['gyozelmek'])
szamolo_b.append(sum(csapat_b))
nevuk_b.append(ember['csapat'])
sumok.append(szamolo_b)

nevuk_t = []
csapat_t = []
szamolo_t = []
for ember in f1emberek:
    if ember['csapat'] == 'Tyrrell':
        csapat_t.append(ember['gyozelmek'])
szamolo_t.append(sum(csapat_t))
nevuk_t.append(ember['csapat'])
sumok.append(szamolo_t)

nevuk_l = []
csapat_l= []
szamolo_l = []
for ember in f1emberek:
    if ember['csapat'] == 'Lotus':
        csapat_l.append(ember['gyozelmek'])
szamolo_l.append(sum(csapat_l))
nevuk_l.append(ember['csapat'])
sumok.append(szamolo_l)


legtobb_csap = max(sumok)


if szamolo_f == legtobb_csap:
    print(f"***A legtöbb futamgyőzelmet szerző csapat: {nevuk_f}") 

if szamolo_ml == legtobb_csap:
    print(f"***A legtöbb futamgyőzelmet szerző csapat: {nevuk_ml}")

if szamolo_r == legtobb_csap:
    print(f"***A legtöbb futamgyőzelmet szerző csapat: {nevuk_r}")

if szamolo_m == legtobb_csap:
    print(f"***A legtöbb futamgyőzelmet szerző csapat: {nevuk_m}")

if szamolo_w == legtobb_csap:
    print(f"***A legtöbb futamgyőzelmet szerző csapat: {nevuk_w}")

if szamolo_bgp == legtobb_csap:
    print(f"***A legtöbb futamgyőzelmet szerző csapat: {nevuk_bgp}")

if szamolo_rb == legtobb_csap:
    print(f"***A legtöbb futamgyőzelmet szerző csapat: {nevuk_rb}")

if szamolo_b == legtobb_csap:
    print(f"***A legtöbb futamgyőzelmet szerző csapat: {nevuk_b}")

if szamolo_t == legtobb_csap:
    print(f"***A legtöbb futamgyőzelmet szerző csapat: {nevuk_t}")

if szamolo_l == legtobb_csap: 
    print(f"***A legtöbb futamgyőzelmet szerző csapat: {nevuk_l}")
    