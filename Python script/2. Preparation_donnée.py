#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv("data.csv",sep="\t")
data.head()


#Moyenne par catégorie de questions pour le monde :

dmoy = data[['race','age','engnat','gender','hand','source','country']]
dmoy["E"] = data[['E1','E2','E3','E4','E5','E6','E7','E8','E9','E10']].mean(axis=1)

dmoy["N"]=data[['N1','N2','N3','N4','N5','N6','N7','N8','N9','N10']].mean(axis=1)

dmoy["A"]=data[['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10']].mean(axis=1)

dmoy["C"]=data[['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10']].mean(axis=1)

dmoy["O"]=data[['O1','O2','O3','O4','O5','O6','O7','O8','O9','O10']].mean(axis=1)
dmoy.head()


dmoy11=dmoy[['E','N','A','C','O']].max(axis=1)
Max = pd.DataFrame(data=dmoy11,columns=["max"])
Max


personality_type = dmoy[['E','N','A','C','O']].idxmax(axis=1)
personality_type


dmoy["maximum"] = Max
dmoy["personality_type"] = personality_type


# Donc voici le tableau des moyennes et du maximum aux questions de personnalités sur le monde.
print("Donc voici le tableau des moyennes et du maximum aux questions de personnalités sur le monde.\n", dmoy.head())
dmoy.to_csv("data_with_mean&max.csv", index=False) # On l'exporte en CSV pour toute les autres analyses plus tard
print("On l'exporte en CSV pour toute les autres analyses plus tard")

# Voici là la moyenne par catégorie de question :
print("""Voici là la moyenne par catégorie de question :
    'E': {},
    'N': {},
    'A': {},
    'C': {},
    'O': {},
""".format(dmoy[['E']].mean(axis=0),
dmoy[['N']].mean(axis=0),
dmoy[['A']].mean(axis=0),
dmoy[['C']].mean(axis=0),
dmoy[['O']].mean(axis=0)))



# Etats-Unis :

# Maintenant, nous allons faire la même chose pour les Etats-Unis.

# Moyenne par catégorie de questions :

det1 = data[data["country"] == "US"]
det = det1[['race','age','engnat','gender','hand','source','country']]

det["E"] = det1[['E1','E2','E3','E4','E5','E6','E7','E8','E9','E10']].mean(axis=1)

det["N"]=det1[['N1','N2','N3','N4','N5','N6','N7','N8','N9','N10']].mean(axis=1)

det["A"]=det1[['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10']].mean(axis=1)

det["C"]=det1[['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10']].mean(axis=1)

det["O"]=det1[['O1','O2','O3','O4','O5','O6','O7','O8','O9','O10']].mean(axis=1)

det.head()


det22=det[['E','N','A','C','O']].max(axis=1)
Maxe = pd.DataFrame(data=det22,columns=["max"])
Maxe


personality_type_us = det[['E','N','A','C','O']].idxmax(axis=1)
personality_type_us


det["Maximum"] = Maxe
det["personality_type"] = personality_type_us


# Donc voici le tableau des moyennes et du maximum aux questions de personnalités aux Etats-Unis.
print("Donc voici le tableau des moyennes et du maximum aux questions de personnalités aux Etats-Unis\n.", det)



# Voici là la moyenne par catégorie de question :


print("""Voici là la moyenne par catégorie de question :
    'E': {},
    'N': {},
    'A': {},
    'C': {},
    'O': {},
""".format(det[['E']].mean(axis=0),
det[['N']].mean(axis=0),
det[['A']].mean(axis=0),
det[['C']].mean(axis=0),
det[['O']].mean(axis=0)))


