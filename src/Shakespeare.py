
# coding: utf-8

# In[1]:


from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number

# Enable inline plotting
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


spFilePath = r'C:\Users\kumar\OneDrive\Documents\Projects\Shakespeare\data\external\Shakespeare_data.csv'
spDF = pd.read_csv(spFilePath)
spDF


# In[3]:


from sklearn.datasets import load_iris
from sklearn import tree


# In[4]:


players = spDF.Player.unique()
i=0
labPly = dict()
for player in players:
    labPly[player]=i
    i=i+1


# In[62]:


# Shows number of Players in Each Plays
import numpy as np

numberPlayers = spDF.groupby(['Play'])['Player'].nunique().sort_values(ascending= False).to_frame()
numberPlayers['Play'] = numberPlayers.index.tolist()
numberPlayers.columns = ['Num Players','Play']
numberPlayers.index= np.arange(0,len(numberPlayers))
numberPlayers

plt.figure(figsize=(10,10))
ax = sns.barplot(x='Num Players',y='Play',data=numberPlayers)
ax.set(xlabel='Number of Players', ylabel='Play Name')
plt.show()


# In[6]:


# Convert Players to Labels
lbSPDF = spDF.replace({"Player": labPly})


# In[52]:


# Feature Engineering
# Since Text cannot be used to classify, we find tfidf of all the playerlines
# Using this we will get the feature vectors, which then can be used to classify

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')
features = tfidf.fit_transform(lbSPDF.PlayerLine).toarray()
features.shape


# In[54]:


# Split Total Data into Train and Test
from sklearn.model_selection import train_test_split

lbSPDF = lbSPDF.dropna()

# one_hot_data = pd.get_dummies(lbSPDF.PlayerLine,drop_first=True,sparse=True)

#Player Line is the data and Player is the Classification

X_train, X_test, y_train, y_test = train_test_split(lbSPDF.PlayerLine, lbSPDF.Player, random_state=1)


# In[55]:


# Classification using Naive Byes


from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(X_train)
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

# Run Training
clf = MultinomialNB().fit(X_train_tfidf, y_train)


# In[56]:


# Run Testing and print accuracy
clf.score(count_vect.transform(X_test), y_test)


# In[57]:



# Classification using 4 models
#   1)Random Forest 
#   2) Support Vector Machine
#   3)Naive Byes
#   4)Logistic Regression

# Cross Validation is used

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.model_selection import cross_val_score
models = [
    RandomForestClassifier(n_estimators=200, max_depth=3, random_state=0),
    LinearSVC(),
    MultinomialNB(),
    LogisticRegression(random_state=0),
]
CV = 5
cv_df = pd.DataFrame(index=range(CV * len(models)))
entries = []
for model in models:
  model_name = model.__class__.__name__
  accuracies = cross_val_score(model, features, lbSPDF.Player, scoring='accuracy', cv=CV)
  for fold_idx, accuracy in enumerate(accuracies):
    entries.append((model_name, fold_idx, accuracy))
cv_df = pd.DataFrame(entries, columns=['model_name', 'fold_idx', 'accuracy'])
import seaborn as sns
sns.boxplot(x='model_name', y='accuracy', data=cv_df)
sns.stripplot(x='model_name', y='accuracy', data=cv_df, 
              size=8, jitter=True, edgecolor="gray", linewidth=2)
plt.show()


# In[59]:


# Accuracies after Classification using cross validation for all models
cv_df


# In[60]:


# Average accuracy for each model
cv_df.groupby('model_name').accuracy.mean()

