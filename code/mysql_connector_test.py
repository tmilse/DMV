
# coding: utf-8

# In[10]:

import MySQLdb
import pandas as pd


# In[11]:

dsn_database = "demographic"
dsn_hostname = "georgetownanalyticscapstone.c50pz9jksixq.us-east-1.rds.amazonaws.com"
dsn_port = 3306
dsn_uid = "sanemkabaca"
dsn_pwd = "georgetowndmv"


# In[12]:

db_connection = MySQLdb.connect(host=dsn_hostname, port=dsn_port, user=dsn_uid, passwd=dsn_pwd, db=dsn_database)


# In[13]:

query = ("""SELECT * FROM demographic.age_sex LIMIT 10""")


# In[14]:

df = pd.read_sql(query, con=db_connection)


# In[16]:

df.head()


# In[ ]:



