import os
import shutil
from datetime import date
from random import randint

##### Constante

### Folder destinatie
destin = "C:/Users/aquas/Desktop/XboxDVR/"

### Locatie fisiere XBOX DVR descarcate din Aplicatia Xbox Console Companion
captures = "C:/Users/aquas/Videos/Captures/"

########## Functia efectiva

### Verifica daca exista fisiere in locatia initiala
### Sortarea in foldere se face dupa primul cuvant
### Daca nu exista folder pentru acel joc se face unul
### Redenumim fisierele pentru a evita problemele (adaugam la final data + un numar random)
### Muta fisierele in destiantia finala

def clean_xbox_dvr():
    for file in os.listdir(captures):   # executam pentru fiecare fisier prezent in folder

        sursa = captures+file   # stabilim fiserul sursa
        folder_joc = destin + file.split(' ')[0] + '/'  # stabilim calea folderului in care trebuie sa mutam fisierul in functie de numele fisierului

        extensie = file[-4:]    # retinem extensia ca sa ne fie usor sa redenumim (se poate dezvolta algoritmul in functie de extensie sa faca alte lucruri / alte sortari etc.)

        if not os.path.exists(folder_joc):   # verificam daca NU folderul exista
            os.makedirs(folder_joc)     # creem folderul

        destinatia = folder_joc + file[:-4] + '-' + str(date.today()) + '-' + str(randint(1000,9999)) + extensie # stabilim destinatia + numele fisierului la care adaugam ziua si un numar random intre 1000 si 9999

        shutil.move(sursa,destinatia)    # executam mutarea efectiva

########## Programul efectiv apeleaza functia

clean_xbox_dvr()