#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import re
from urllib.parse import urlparse
from sklearn.model_selection import train_test_split


# In[3]:


df = pd.read_csv("../data/final_dataset.csv")


# In[4]:


df['Label'] = df['Label'].map({'good': 0, 'bad': 1})


# In[5]:


df = df.dropna(subset=['URL'])  # Remove rows where URL is missing
df['URL'] = df['URL'].astype(str)


# In[6]:


def extract_features(url):
    parsed_url = urlparse(url)

    # Feature 1: URL Length
    url_length = len(url)

    # Feature 2: Number of Dots (.)
    num_dots = url.count('.')

    # Feature 3: Number of Hyphens (-)
    num_hyphens = url.count('-')

    # Feature 4: Number of Slashes (/)
    num_slashes = url.count('/')

    # Feature 5: Number of Digits in URL
    num_digits = sum(c.isdigit() for c in url)

    # Feature 6: Presence of "https" (1 = Yes, 0 = No)
    has_https = 1 if parsed_url.scheme == 'https' else 0

    # Feature 7: Presence of "www" in domain (1 = Yes, 0 = No)
    has_www = 1 if "www" in parsed_url.netloc else 0

    # Feature 8: Length of Domain Name
    domain_length = len(parsed_url.netloc)

    # Feature 9: Number of Special Characters in URL
    special_chars = len(re.findall(r'[@_!#$%^&*()<>?/|}{~:]', url))

    # Feature 10: Is IP Address? (1 = Yes, 0 = No)
    is_ip = 1 if re.match(r'\d+\.\d+\.\d+\.\d+', parsed_url.netloc) else 0

    return [url_length, num_dots, num_hyphens, num_slashes, num_digits, has_https, has_www, domain_length, special_chars, is_ip]


# In[7]:


feature_columns = ['url_length', 'num_dots', 'num_hyphens', 'num_slashes', 'num_digits', 'has_https', 'has_www', 'domain_length', 'special_chars', 'is_ip']
df_features = df['URL'].apply(extract_features)
df_features = pd.DataFrame(df_features.tolist(), columns=feature_columns)


# In[11]:


df_final = pd.concat([df_features, df['Label']], axis=1)
df_final = df_final.dropna(subset=['Label'])


# In[12]:


X = df_final.drop(columns=['Label'])  # Features
y = df_final['Label']  # Target


# In[13]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)


# In[14]:


df_final.to_csv("../data/processed_dataset.csv", index=False)


# In[15]:


print("✅ Feature extraction and data preprocessing completed!")
print(f"Training set size: {len(X_train)}")
print(f"Testing set size: {len(X_test)}")


# In[17]:


import pandas as pd

# Save training & testing sets
X_train.to_csv("../data/X_train.csv", index=False)
X_test.to_csv("../data/X_test.csv", index=False)
y_train.to_csv("../data/y_train.csv", index=False)
y_test.to_csv("../data/y_test.csv", index=False)


# In[ ]:




