

# We will use the pymysql package to connect to the database. After that, we will use Pandas for data analysis.

# In[1]:


import pandas as pd
import pymysql


# Connect to database
# To connect to the database, we use the connect function from pymysql. The connect function returns a Connection object.

# In[2]:


host="Aws RDS Endpoint will come here"
port=3306
dbname="test"
user="your_user._name"
password="your_pass"

conn = pymysql.connect(host, user=user,port=port,
                           passwd=password, db=dbname)


# Let's query our table

pd.read_sql('select count(*) AS "Count of Genders", gender from employees group by gender;', con=conn) 

# Visualize our data


import matplotlib.pyplot as plt
pandas_df=pd.read_sql('select gender from employees;', con=conn) 
pandas_df.groupby(pandas_df.gender).size().plot(kind='bar')
plt.xlabel('Gender')
plt.ylabel('Count of Genders')
plt.show()







