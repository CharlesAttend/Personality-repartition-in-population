#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings


data = pd.read_csv("data_with_mean&max.csv",sep=",")
print(data.head())


# <div style="color: darkred; font-size: large">Nous allons introduire le projet grâce à plusieurs graphiques.</div>

# Tout d'abord, nous allons voir le nombre de participant par pays. 

data['country'].value_counts().plot(kind='area')
plt.draw()
plt.waitforbuttonpress(30)
plt.close()
data['country'].value_counts().plot(kind='pie')
plt.draw()
plt.waitforbuttonpress(30)
plt.close()


# Nous allons voir le pourcentage de femme et d'homme dans le monde.

data['gender'].value_counts().plot(kind='pie',figsize=(7,7),labels=['Femme', 'Homme', 'Autre', 'X'], colors=['r', 'g', 'b', 'c'],autopct='%.2f', fontsize=20)
plt.draw()
plt.waitforbuttonpress(30)
plt.close()

# Nous allons voir la répartition des races dans le monde.

Pie = pd.DataFrame({'Donnée': [10537,2553,1861,1518,1434,515,397,259,201,188,153,65,24,14]},

                  index=['Caucasian(European)','Other','South East Asian (Chinese, Thai, Malay, Filipino, etc)','Caucasian (Indian)','Mixed Race','Caucasian (Middle East)','Caucasian (North African, Other)','West African, Bushmen, Ethiopian','Native American','North East Asian (Mongol, Tibetan, Korean Japanese, etc)','X','Pacific (Polynesian, Micronesian, etc)','Indigenous Australian','Arctic(Siberian, Eskimo)'])

Pie.plot.pie(y='Donnée', figsize=(10, 10),labeldistance=None).legend(['Caucasian(European)','Other','South East Asian (Chinese, Thai, Malay, Filipino, etc)','Caucasian (Indian)','Mixed Race','Caucasian (Middle East)','Caucasian (North African, Other)','West African, Bushmen, Ethiopian','Native American','North East Asian (Mongol, Tibetan, Korean Japanese, etc)','X','Pacific (Polynesian, Micronesian, etc)','Indigenous Australian','Arctic(Siberian, Eskimo)'], loc=0, fontsize=10)
plt.draw()
plt.waitforbuttonpress(30)
plt.close()

# <div style="font-size: medium">Moyenne d'age des personnes qui ont effectué le test dans le monde :</div>

# Ayant des données faussées, nous prenons les données où l'âge est inférieur ou égale à 110ans.
dmoyage = data[data["age"] <= 110]
print("age moyen dans le monde: \n", dmoyage[['age']].mean(axis=0))

# <div style="font-size: medium">Et aux Etats-Unis :</div>

ET = data[data["country"] == "US"]
print("age moyen au USA: \n", ET[ET["age"] <= 110][['age']].mean(axis=0))


# Graphique de l'âge dans le monde
sns.kdeplot(dmoyage['age'], shade=True, color="r")
plt.draw()
plt.waitforbuttonpress(30)
plt.close()

# Nous allons voir la répartition des personnes qui parlent l'anglais de naissance.

data['engnat'].value_counts().plot(kind='pie',figsize=(7,7),labels=['English', 'Other', 'X'], colors=['r', 'g', 'b'],autopct='%.2f', fontsize=20)
plt.draw()
plt.waitforbuttonpress(30)
plt.close()

warnings.filterwarnings("ignore")
Femme = data[data["gender"] == 2]
Homme = data[data["gender"] == 1]
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 10))

Femme['engnat'].value_counts().plot(ax=axes[0], title = 'Femme', kind='pie',labels=['English', 'Other', 'X'], colors=['r', 'g', 'b'],autopct='%.2f', fontsize=20)
Homme['engnat'].value_counts().plot(ax=axes[1], title = 'Homme', kind='pie',labels=['English', 'Other', 'X'], colors=['r', 'g', 'b'],autopct='%.2f', fontsize=20)
plt.draw()
plt.waitforbuttonpress(30)
plt.close()
