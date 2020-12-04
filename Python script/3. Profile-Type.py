#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import warnings

data = pd.read_csv("data_with_mean&max.csv",sep=",")
data.head()


# Nous allons donc chercher le profile-type grâce à l'aide de différents moyens.
# Nous procéderons par colonnes.

# Race:

race = data["race"].value_counts()
print(race)
race.idxmax(axis=1)
print("Nous allons choisir la race numéro 3 (Caucasian (European)\n")
# Nous allons choisir la race numéro 3 (Caucasian (European)).

# Age :
age = data[data["age"] <= 110]
print(age[['age']].mean(axis=0))
print('On voit que l\'âge moyen est 26,3 ans.\n')
# On voit que l'âge moyen est 26,3 ans.

# Engnat :(Réponse à "is English your native language?")
print('Engnat :(Réponse à "is English your native language?")')
print(data[['engnat']].median(axis=0))
data.pivot_table(columns='engnat',values='age',aggfunc='count')
print('On voit que le résultat est 1, soit "yes" à la question dite précedement.\n')
# On voit que le résultat est 1, soit "yes" à la question dite précedement.

# Gender :(1=Male, 2=Female, 3=Other)
print(data[['gender']].median(axis=0))
data.pivot_table(columns='gender',values='age',aggfunc='count')
print("On voit que le résultat est 2, il s'agit donc d'une femme.\n")
# On voit que le résultat est 2, il s'agit donc d'une femme.

# Hand :("What hand do you use to write with?" 1=Right, 2=Left, 3=Both)
print(data[['hand']].median(axis=0))
data.pivot_table(columns='hand',values='age',aggfunc='count')
print("On voit que le résultat est 1, il s'agit donc d'une droitière.\n")
# On voit que le résultat est 1, il s'agit donc d'une droitière.

# Source (Réponse à "How the participant came to the test."):
data[['source']].median(axis=0)
data.pivot_table(columns='source',values='age',aggfunc='count')
print("On voit que le résultat maximum est 1, le participant vient d'une autre page sur le même site. (from another page on the test website).")
# On voit que le résultat maximum est 1, le participant vient d'une autre page sur le même site. (from another page on the test website).

# Country :
pays = data.pivot_table(columns='country',values='age',aggfunc='count')
print(pays)
print(pays.idxmax(axis=1))
print("On remarque que le pays est Etats-Unis.")
# On remarque que le pays est Etats-Unis.

# Le Profile-Type est donc une femme de type Caucasienne (d'Europe), qui a 26ans, pour qui la langue natale est l'anglais, droitière, qui vit aux Etats-Unis et qui vient d'une autre page sur le même site.

# Nous allons maintenant nous occuper des réponses attendues, celles qui sont le plus répendues.
print("Nous allons maintenant nous occuper des réponses attendues, celles qui sont le plus répendues.\n")
# Pour E :
print(round(data["E"].mean(), 1))
print('On observe que la moyenne pour "E" est environ 3.1')

# On observe que la moyenne pour "E" est environ 3.1

# Pour N :
print(round(data["N"].mean(), 1))
print('On observe que la moyenne pour "N" est également d\'environ 3.1')
# On observe que la moyenne pour "N" est également d'environ 3.1

# Pour A :
print(round(data["A"].mean(), 1))
print('On observe que la moyenne pour "A" est environ 3.2')
# On observe que la moyenne pour "A" est environ 3.2

# Pour C :
print(round(data["C"].mean(), 1))
print('On observe que la moyenne pour "C" est environ 3.1')
# On observe que la moyenne pour "C" est environ 3.1

# Pour O :
print(round(data["O"].mean(), 1))
print('On observe que la moyenne pour "O" est environ 3.3')
# On observe que la moyenne pour "O" est environ 3.3

# Pour le type de personnalité :
print(data["personality_type"].value_counts())
print('On remarque que la peronnalité la plus répendue est "N".\n')
# On remarque que la peronnalité la plus répendue est "N".

# Le Profile-Type a donc un résultat au test, en moyenne de 3.0 pour les questions de type "E" et "N", de 3.2 pour les questions de type "A" et "C" et de 3.4 pour les questions de type "O". De plus, la personnalité définie pour ce profil est 'N'.
Donnée = {'Race':  ['Caucasian (European)'],'Age': ['26,3'],'Native language':  ['English'],'Gender':  ['Female'],'Hand':  ['Right'],'Where is he from':  ['from another page on the test website'],'Country':  ['United States'],'E':  ['3.1'],'N':  ['3.1'],'A':  ['3.2'],'C':  ['3.2'],'O':  ['3.4'],'Personality_type': ['N']}

Profile_Type = pd.DataFrame(Donnée,columns=['Race','Age','Native language','Gender','Hand','Where is he from','Country','E','N','A','C','O','Personality_type'])
print('Le profil type :\n',Profile_Type)





