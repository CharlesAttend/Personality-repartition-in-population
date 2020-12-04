#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
try:
    import geopandas as gpd
    import descartes, pycountry
except ModuleNotFoundError:
    raise Warning("Please install geopandas, descartes and pycountry packtages to run this notebook : pip3 install geopandas descartes pycountry")
    #!pip3 install geopandas descartes pycountry


csv = pd.read_csv("data_with_mean&max.csv").drop(['personality_type', 'maximum'], axis=1)

# Filtrons les pays avec moins de 100 participations pour garder une certaine pertinance dans les résultats stastistiques
topCountry = csv['country'].value_counts() #On compte le nombre de réponse par pays
topCountry = topCountry[topCountry > 100].drop("(nu") #On filtre tous les pays avec moins de 100 réponse et les informations manquantes

# Nous ferons donc nos analyses sur un panel de 23 pays.<br/>
# Appliquons ce filtre à notre dataframe.
csv = csv[csv['country'].isin(topCountry.index)] #if country is in (.isin) la liste des pays de plus de 100 réponses

# Observons maintenant la moyenne des réponses aux questions par personalité et par pays. <br/> Dans l'ordre des pays avec le plus de réponses.
countryMean = csv.pivot_table(index='country', values=['E','N','A','C','O']).reindex(topCountry.index) #reindex permet de changer l'ordre des lignes


#  On constate que les moyennes ne varie que de quelques dixième. Cela traduit une répartion des personalités dans la population assez équilibrés. <br/> Attribuons une personalité majeur et une mineur à tous ces pays
countryMean["majeur"] = countryMean[['E','N','A','C','O']].idxmax(axis=1)
countryMean["mineur"] = countryMean[['E','N','A','C','O']].idxmin(axis=1) 



l=list()
for country in countryMean.index:
    l.append(pycountry.countries.get(alpha_2=country).alpha_3)
countryMean['iso_a3'] = l
countryMean.set_index('iso_a3', inplace=True)


colors_dict = {'A':'#C47B84', 'C':'#9591C3', 'E':'#D4A55D', 'N':'#78A1B5', 'O':'#559392'}
l = []
for i in countryMean['majeur']:
    l.append(colors_dict[i])
countryMean['color_majeur'] = l
l = []
for i in countryMean['mineur']:
    l.append(colors_dict[i])
countryMean['color_mineur'] = l



world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
world = world[world.name!='Antarctica']
world.loc[world['name'] == 'France', 'iso_a3'] = 'FRA'
world.loc[world['name'] == 'Norway', 'iso_a3'] = 'NOR' #https://github.com/geopandas/geopandas/issues/1041#issuecomment-603458259



world.set_index('iso_a3', inplace=True)
world['color_majeur'] = countryMean['color_majeur']
world['color_mineur'] = countryMean['color_mineur']
world.fillna("grey", inplace=True)



fig, ax = plt.subplots(1, 1, figsize=(15,9))
l=list()
for i in colors_dict:
    l.append(mpatches.Patch(color=colors_dict[i], label=i))
ax.legend(handles=l)
plt.title('Carte des pays en fonction de leur personalité majeure')
world.plot(color=world['color_majeur'],ax=ax)
plt.draw()
plt.waitforbuttonpress(30)
plt.close()

fig, ax = plt.subplots(1, 1, figsize=(15,9))
l=list()
for i in colors_dict:
    l.append(mpatches.Patch(color=colors_dict[i], label=i))
ax.legend(handles=l)
plt.title('Carte des pays en fonction de leur personalité mineure')
world.plot(color=world['color_mineur'],ax=ax)
plt.draw()
plt.waitforbuttonpress(30)
plt.close()
