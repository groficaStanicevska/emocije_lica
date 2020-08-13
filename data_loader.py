import pandas as pd
import os

def cuvanje_putanja_labela(PATH):
    putanja_fajlova = []
    fajlovi_labelirani = []
    for i in (os.listdir(PATH)):
        for j in (os.listdir(f"{PATH}/{i}/")):
            for x in (os.listdir(f"{PATH}/{i}/{j}/")):
                putanja_fajlova.append((f"{PATH}/{i}/{j}/{x}"))
                fajlovi_labelirani.append(x)
    return putanja_fajlova, fajlovi_labelirani


def cuvanje_putanje_podatka(PATH, imena_fajlova, zadnji_deo):
    putanja_fajlova = []
    for i in (os.listdir(PATH)):
        for j in (os.listdir(f"{PATH}/{i}/")):
            for x in (os.listdir(f"{PATH}/{i}/{j}/")):
                for z in imena_fajlova:
                    z = list(z)
                    z[-12: ] = zadnji_deo
                    z_str = ''
                    for k in z:
                        z_str += k
                    if z_str == x:
                        putanja_fajlova.append((f"{PATH}/{i}/{j}/{x}"))

    return putanja_fajlova

def izvlacenje_labela(lista_putanja):
    lista_podataka = []
    for x in lista_putanja:
        f = open(x)
        for red in f:
            if len(red) == 17:
                lista_podataka.append(float(red))
    return lista_podataka

def izvlacenje_brojeva(lista_fajlova):
    lista = []
    poc = []
    kraj = []
    pom = []
    for x in lista_fajlova:
        f = open(x)
        for red in f:
            for i in range(len(red)-1):
                if red[i].isspace() and red[i+1].isdigit():
                    poc.append(i+1)
                if red[i].isdigit() and red[i+1].isspace():
                    kraj.append(i)

            x = float(red[poc[0]:kraj[0]+1])
            y = float(red[poc[1]:kraj[1] + 1])
            pom.append([x,y])
        lista.append(pom)
        pom = []
    return lista

putanje_label, fajlovi = cuvanje_putanja_labela('Cohn-Kanade Database/CK+/Emotion')
putanje_landmarks = cuvanje_putanje_podatka('Cohn-Kanade Database/CK+/Landmarks',fajlovi, '_landmarks.txt')
#putanje_slika = cuvanje_putanje_podatka('Cohn-Kanade Database/CK+/cohn-kanade-images',fajlovi, '.png')

labels = izvlacenje_labela(putanje_label)
landmarks = izvlacenje_brojeva(putanje_landmarks)

data = {}

data['labels'] = labels
data['landmarks'] = landmarks

columns = ['labels', 'landmarks']
df = pd.DataFrame(data,columns = columns)
df.to_csv('data_loader.csv', index=False)
