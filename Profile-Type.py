#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import warnings


# In[2]:


data = pd.read_csv("data_with_mean&max.csv",sep=",")
data.head()


# <div style="font-size: medium">Nous allons donc chercher le profile-type grâce à l'aide de différents moyens.
# Nous procéderons par colonnes.</div>

# <div style="color: darkviolet; font-size: x-large">Race:</div>

# In[3]:


race = data.pivot_table(columns='race',values='age',aggfunc='count')
race


# In[4]:


race.idxmax(axis=1)


# Nous allons choisir la race numéro 3 (Caucasian (European)).

# <div style="color: darkviolet; font-size: x-large">Age :</div>

# In[5]:


age = data[data["age"] <= 110]


# In[6]:


age[['age']].mean(axis=0)


# On voit que l'âge moyen est 26,3 ans.

# <div style="color: darkviolet; font-size: x-large">Engnat :<div style="font-size: medium">(Réponse à "is English your native language?")</div></div>

# In[7]:


data[['engnat']].median(axis=0)


# In[8]:


data.pivot_table(columns='engnat',values='age',aggfunc='count')


# On voit que le résultat est 1, soit "yes" à la question dite précedement.

# <div style="color: darkviolet; font-size: x-large">Gender :<div style="font-size: medium">(1=Male, 2=Female, 3=Other)</div></div>

# In[9]:


data[['gender']].median(axis=0)


# In[10]:


data.pivot_table(columns='gender',values='age',aggfunc='count')


# On voit que le résultat est 2, il s'agit donc d'une femme.

# <div style="color: darkviolet; font-size: x-large">Hand :<div style="font-size: medium">("What hand do you use to write with?" 1=Right, 2=Left, 3=Both)</div></div>

# In[11]:


data[['hand']].median(axis=0)


# In[12]:


data.pivot_table(columns='hand',values='age',aggfunc='count')


# On voit que le résultat est 1, il s'agit donc d'une droitière.

# <div style="color: darkviolet; font-size: x-large">Source (Réponse à "How the participant came to the test."):</div>

# In[13]:


data[['source']].median(axis=0)


# In[14]:


data.pivot_table(columns='source',values='age',aggfunc='count')


# On voit que le résultat maximum est 1, le participant vient d'une autre page sur le même site. (from another page on the test website).

# <div style="color: darkviolet; font-size: x-large">Country :</div>

# In[15]:


pays = data.pivot_table(columns='country',values='age',aggfunc='count')
pays


# In[16]:


pays.idxmax(axis=1)


# On remarque que le pays est Etats-Unis.

# <div style="color: darkred; font-size: medium">Le <u>Profile-Type</u> est donc une <strong>femme</strong> de type <strong>Caucasienne</strong> (d'Europe), qui a <strong>26</strong>ans, pour qui la langue natale est l'<strong>anglais</strong>, <strong>droitière</strong>, qui vit aux <strong>Etats-Unis</strong> et qui vient d'une autre page sur le même site.</div>

# <div style="font-size: medium">Nous allons maintenant nous occuper des réponses attendues, celles qui sont le plus répendues.</div>

# <div style="color: darkviolet; font-size: x-large">Pour E :</div>

# In[17]:


round(data["E"].mean(), 1)


# On observe que la moyenne pour "E" est environ 3.1

# <div style="color: darkviolet; font-size: x-large">Pour N :</div>

# In[18]:


round(data["N"].mean(), 1)


# On observe que la moyenne pour "N" est également d'environ 3.1

# <div style="color: darkviolet; font-size: x-large">Pour A :</div>

# In[19]:


round(data["A"].mean(), 1)


# On observe que la moyenne pour "A" est environ 3.2

# <div style="color: darkviolet; font-size: x-large">Pour C :</div>

# In[20]:


round(data["C"].mean(), 1)


# On observe que la moyenne pour "C" est environ 3.1

# <div style="color: darkviolet; font-size: x-large">Pour O :</div>

# In[21]:


round(data["O"].mean(), 1)


# On observe que la moyenne pour "O" est environ 3.3

# <div style="color: darkviolet; font-size: large">Pour le type de personnalité :</div>

# In[22]:


data["personality_type"].value_counts()


# On remarque que la peronnalité la plus répendue est "N".

# <div style="color: darkred; font-size: medium">Le <u>Profile-Type</u> a donc un résultat au test, en moyenne de <strong>3.0</strong> pour les questions de type <strong>"E"</strong> et <strong>"N"</strong>, de <strong>3.2</strong> pour les questions de type <strong>"A"</strong> et <strong>"C"</strong> et de <strong>3.4</strong> pour les questions de type <strong>"O"</strong>. De plus, la personnalité définie pour ce profil est <strong>'N'</strong>.</div>

# In[23]:


Donnée = {'Race':  ['Caucasian (European)'],'Age': ['26,3'],'Native language':  ['English'],'Gender':  ['Female'],'Hand':  ['Right'],'Where is he from':  ['from another page on the test website'],'Country':  ['United States'],'E':  ['3.1'],'N':  ['3.1'],'A':  ['3.2'],'C':  ['3.2'],'O':  ['3.4'],'Personality_type': ['N']}

Profile_Type = pd.DataFrame(Donnée,columns=['Race','Age','Native language','Gender','Hand','Where is he from','Country','E','N','A','C','O','Personality_type'])
Profile_Type


# In[ ]:




