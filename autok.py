def adattarolas():
    adatok = []

    with open('jeladas.txt', 'r', encoding='utf-8') as file:
        for line in file:
            fields = line.strip().split('\t')
            adatok.append(fields)

    return adatok


def masodik(adatok):
    print('2. feladat:')
    print(adatok[-1][1] + ':' + adatok[-1][2], adatok[-1][0])


def harmadik(adatok):
    idopontok = []
    i = 0

    for _ in adatok:
        if adatok[i][0] == adatok[0][0]:
            if len(adatok[i][2]) < 2:
                perc = '0' + adatok[i][2]

            else:
                perc = adatok[i][2]

            idopontok.append(adatok[i][1] + ':' + perc)

        i += 1

    idopontok2 = ''

    for elem in idopontok:  # azért használtam _ -t hogy ne problémázzon az IDEA
        idopontok2 += str(elem) + ' '

    print('3. feladat:')
    print(adatok[0][0], idopontok2)


def negyedik(adatok):
    print('4. feladat:')
    ora = input('Kérem adja meg az órát: ')
    perc = input('Kérem adja meg a percet: ')
    jeladasok = 0
    i = 0

    for _ in adatok:
        if adatok[i][1] == ora and adatok[i][2] == perc:
            jeladasok += 1

        i += 1

    print('Jeladások száma:', jeladasok)


def otodik(adatok):
    print('5. feladat:')
    max_ertek = 0
    autok = []
    i = 0
    j = 0
    rendszamok = ''

    for _ in adatok:
        if int(adatok[i][3]) >= int(max_ertek):
            max_ertek = adatok[i][3]

        i += 1

    for elem in adatok:
        if max_ertek == elem[3]:
            autok.append(elem[0])

        j += 1

    for elem in autok:
        rendszamok += elem + ' '

    print('A legnagyobb elért sebesség km/h:', max_ertek)
    print('A járművek:', rendszamok)


def hatodik_tavolas(time, speed):
    return


def hatodik(adatok):
    print('6. feladat:')
    rendszam = input('Kérem adjon meg egy rendszámot: ')
    ido = []

    for elem in adatok:
        if elem[0] == rendszam:
            ido.append((int(elem[1]) * 60) + int(elem[2]))
            eltelt_ido = ido[-1] - ido[0] # itt valami nem jó
            km = hatodik_tavolas(eltelt_ido, elem[3])

            print(ido)

            print(elem[1] + ':' + elem[2], str(km) + 'km')


data = adattarolas()

masodik(data)
harmadik(data)
# negyedik(data)
otodik(data)
hatodik(data)
