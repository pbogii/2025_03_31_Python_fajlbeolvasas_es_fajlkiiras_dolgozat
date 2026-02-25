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


