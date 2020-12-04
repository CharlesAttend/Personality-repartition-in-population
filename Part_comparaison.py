#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
try:
    import seaborn as sns
except:
    raise Warning('Please install seaborn to run this notebook')

def make_percentage(l):
    sum = 0
    for i in l:
        sum += i
    return pd.Series([x/sum for x in l], index=l.index)


# In[2]:


csv = pd.read_csv("data_with_mean&max.csv").drop(['E','N','A','C','O','maximum'], axis=1)
csv


# Dans cette partie nous allons à chaque fois comparer les résultats en USA vs le reste du monde. Pour voir si les USA on une réelle différence de personalité.

# Pour cela coupons notre DataFramme en deux, une avec uniquement les résultats des USA et l'autre avec le reste

# In[3]:


usa = csv[csv['country'] == 'US']
monde = csv[csv['country'] != 'US']
print("""Il y a {} réponse au US contre {} ailleur dans le monde""".format(len(usa), len(monde)))


# In[4]:


réponses = pd.DataFrame({'rép': [8753, 10966]}, index=['US','Monde'])
réponses.plot.pie(y='rép', figsize=(5, 5),autopct='%.2f')


# In[19]:


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(14, 10))
colorsDict = {'E':'red','N':'orange','A':'green','C':'purple','O':'blue'}

usa['personality_type'].value_counts().plot.pie(
    ax=axes[0], 
    title='USA', 
    autopct='%.0f', 
    colors=[colorsDict[x] for x in usa['personality_type'].value_counts().index] #Créer un liste des couleurs dans le même ordre que l'index
)                                                                                #Pour avoir les mêmes couleurs sur les deux
monde['personality_type'].value_counts().plot.pie(
    ax=axes[1], 
    title='Monde', 
    autopct='%.0f', 
    colors=[colorsDict[x] for x in monde['personality_type'].value_counts().index] 
)


# In[6]:


usa_series = make_percentage(usa['personality_type'].value_counts())
monde_series = make_percentage(monde['personality_type'].value_counts())
pd.DataFrame([usa_series,monde_series], index=["USA", "Monde"]).plot.bar()


# On peut observer quelques légères variations. Les USA aurait 5% de N en moins par rapport au reste du monde ainsi que 3% de C en plus. Ces valeurs ne sont pas assez pertinantes et surrement du au fait que plus de personne ont répondu dans le monde par rapport à dans les USA.

# Y'a t-il des variations de personnalité entre les femmes et les hommes ?

# In[7]:


usa[usa['gender'] == 1]['personality_type']


# In[8]:


fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(14, 10))
fig.suptitle('Répartition des personalité en fonction du genre, au USA et dans le monde', fontsize=16)

usa[usa['gender'] == 1]['personality_type'].value_counts().plot.pie(ax=ax1, title="USA - Homme", autopct='%.0f', colors=[colorsDict[x] for x in usa[usa['gender'] == 1]['personality_type'].value_counts().index])

usa[usa['gender'] == 2]['personality_type'].value_counts().plot.pie(ax=ax2, title="USA - Femme", autopct='%.0f', colors=[colorsDict[x] for x in usa[usa['gender'] == 2]['personality_type'].value_counts().index])

monde[monde['gender'] == 1]['personality_type'].value_counts().plot.pie(ax=ax3, title="Monde - Homme", autopct='%.0f', colors=[colorsDict[x] for x in monde[monde['gender'] == 1]['personality_type'].value_counts().index])

monde[monde['gender'] == 2]['personality_type'].value_counts().plot.pie(ax=ax4, title="Monde - Femme", autopct='%.0f', colors=[colorsDict[x] for x in monde[monde['gender'] == 2]['personality_type'].value_counts().index])


# In[9]:


USA_Homme = make_percentage(usa[usa['gender'] == 1]['personality_type'].value_counts())
USA_Femme = make_percentage(usa[usa['gender'] == 2]['personality_type'].value_counts())
Monde_Homme = make_percentage(monde[monde['gender'] == 1]['personality_type'].value_counts())
Monde_Femme = make_percentage(monde[monde['gender'] == 2]['personality_type'].value_counts())


# In[10]:


pd.DataFrame([USA_Homme, USA_Femme, Monde_Homme, Monde_Femme], index=["USA - Homme","USA - Femme","Monde - Homme","Monde - Femme"]).plot.bar(title='Répartition des personalité en fonction du genre, au USA et dans le monde', figsize=(14,10))


# On constate que les hommes sont plus O alors que les femmes ont plutot un profil N, et cela au USA ou dans le monde. <br/>
# On observe également un plus grand taux de d'Hommes de type O au Etat-Unis en comparaison avec le monde entier. Chez les femmes, la balance entre les profils O et N est plus équilibré que dans le monde entier, où le profil N l'emporte. 

# Y'a t'il une corrélation entre l'age et la personalité ? 

# In[11]:


filter = usa[["personality_type", "age"]]
filter = filter[filter["age"] <= 100]

bins = pd.IntervalIndex.from_tuples([(13,20), (20,30), (30,40), (40,50), (50,60)])
filter['age'] = pd.cut(filter['age'], bins)
filter


# In[12]:


crosstab = pd.crosstab(filter['age'], filter['personality_type']).apply(lambda r: (r/r.sum())*100, axis=1)
crosstab


# In[13]:


crosstab.plot.bar(title="Répartition des personnalités par catégorie d'âge aux Etat-Unis", stacked=False, figsize=(14, 10))


# In[14]:


crosstab.plot.bar(title="Répartition des personnalités par catégorie d'âge aux Etat-Unis", stacked=True, figsize=(14, 10))


# On peut remarquer de nettes variations sur les deux profils opposés O et N en fonction de l'âge ! En effet il s'emblerai que plus l'age augmente plus il y aurait de profil O, et de moins en moins de profil N.

# In[15]:


filter = monde[["personality_type", "age"]]
filter = filter[filter["age"] <= 100]
filter['age'] = pd.cut(filter['age'], bins)
crosstab = pd.crosstab(filter['age'], filter['personality_type']).apply(lambda r: (r/r.sum())*100, axis=1)
crosstab.plot.bar(title="Répartition des personnalités par catégorie d'âge dans le monde", stacked=False, figsize=(14, 10))


# In[16]:


crosstab.plot.bar(title="Répartition des personnalités par catégorie d'âge dans le monde", stacked=True, figsize=(14, 10))


# Y'a t-il une différence dans la répartion des personalités chez les différentes races ? 

# Pour garder une pertinance statistique nous allons comparer uniquement les 2 races : Caucasien (europeen) et South East Asian (Chinese, Thai, Malay, Filipino, etc)

# In[17]:


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 7))
fig.suptitle("Répartition des personnalités en fonction de l'origine", fontsize=16,)

caucasien = csv[csv['race'] == 3]['personality_type'].value_counts()
asian = csv[csv['race'] == 11]['personality_type'].value_counts()

asian.plot.pie(ax=axes[0], title='Asian', autopct='%.0f',colors=[colorsDict[x] for x in asian.index])
caucasien.plot.pie(ax=axes[1],title="Europeen", autopct='%.0f', colors=[colorsDict[x] for x in caucasien.index])


# In[18]:


pd.DataFrame([make_percentage(asian),make_percentage(caucasien)], index=['Asian','Europeen']).plot.bar()


# In[ ]:




