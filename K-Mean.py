#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.cluster import KMeans


# <div style="text-align: center; font-size: large">K-Mean</div>

# In[2]:


df = pd.read_csv("BIG5/data.csv", sep="\t")
df


# <div style="text-align: center; font-size: medium">Prenons uniquement les colonnes utiles pour le K-Mean</div>

# In[3]:


df.drop(['race','age','engnat','gender','hand','source','country'], axis=1,inplace=True)
kmeans = KMeans(n_clusters=5).fit(df)


# <div style="text-align: center; font-size: medium">On utilise évidement 5 clusters qui correspondent aux 5 types de personalités du test</div>

# In[4]:


print(len(kmeans.cluster_centers_))
kmeans.cluster_centers_[4]
#On a bien 5 cluster (vecteur) de dimention 50 (pour 50 question)


# <div style="text-align: center; font-size: medium">Comparont les clusters créés avec le trait de personalité qui ressort le plus chez une personne</div>

# In[5]:


print(len(kmeans.labels_))
cluster = kmeans.labels_ # renvoie une liste avec le cluster de chaque personne
cluster


# In[6]:


personalites = pd.read_csv('data_with_mean&max.csv', usecols=["personality_type"])['personality_type'] #j'import uniquement le type de personalité car je n'ai pas besoin du reste
personalites


# <div style="text-align: center; font-size: medium">La crosstab vas nous permettre de compter chaque personalitée en fonction du cluster</div>

# In[7]:


pd.crosstab(personalites,cluster)


# On tombe en général sur 2 clusters représentant le type N et 3 représentant le type O

# <div style="text-align: center; font-size: medium">Testons en utilisant la moyenne par type de questions</div>

# In[8]:


df = pd.read_csv('data_with_mean&max.csv', usecols=list('ENACO'))
kmeans = KMeans(n_clusters=5).fit(df)
pd.crosstab(personalites, kmeans.labels_)


# Avec la moyenne par type de question on retrouve 1 cluster de représentant le type A, 2 représentant le type O et 2 représentant le type N 

# <div style="text-align: center; font-size: medium">La numérotation des clusters dans le K-Mean varie à chaque execution de celui-ci. En effet les clusters sont des points placés au hasard sur l'hyperplans de dimention 50. Ou chaque participant est représenté par un point qui a pour coordonées les réponses aux questions</div>

# <div style="text-align: center; font-size: medium">On ne retrouve pas les catégories escompté. En effet la manière dont nous choisisons un seul type de personnalité chez une personne grâce au question n'est pas optimal.<br/>
# Une personne est un mélange de plusieurs personnalité et prendre uniquement celle qui ressort le plus empeche une autre qui à peut être, à peu de chose près, la même prépondérance chez la personne.<br/>
# L'algorythme K-Mean prend lui en compte toutes les facettes de personnalité en même temps
# </div>
