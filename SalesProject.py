#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as mpl
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
mpl.rcParams['figure.figsize'] = (20,5)


# In[2]:


m_sales1 = pd.read_csv('allmonthsales/Sales_January_2019.csv')
m_sales2 = pd.read_csv('allmonthsales/Sales_February_2019.csv')
m_sales3 = pd.read_csv('allmonthsales/Sales_March_2019.csv') 
m_sales4 = pd.read_csv('allmonthsales/Sales_April_2019.csv')
m_sales5 = pd.read_csv('allmonthsales/Sales_May_2019.csv')
m_sales6 = pd.read_csv('allmonthsales/Sales_June_2019.csv') 
m_sales7 = pd.read_csv('allmonthsales/Sales_July_2019.csv')
m_sales8 = pd.read_csv('allmonthsales/Sales_August_2019.csv')
m_sales9 = pd.read_csv('allmonthsales/Sales_September_2019.csv')
m_sales10 = pd.read_csv('allmonthsales/Sales_October_2019.csv')
m_sales11 = pd.read_csv('allmonthsales/Sales_November_2019.csv')
m_sales12 = pd.read_csv('allmonthsales/Sales_December_2019.csv') 
monthlysales = pd.concat([m_sales1, m_sales2, m_sales3, m_sales4, m_sales5, m_sales6, m_sales7, m_sales8, m_sales9, m_sales10, m_sales11, m_sales12])
monthlysales.describe()


# In[3]:


monthlysales.head(5)


# monthlysales.isnull.sum()

# In[4]:


monthlysales.isnull().sum()
#missing values from the data set


# In[5]:


#drop null values 
monthlysales.dropna(inplace=True)
monthlysales.isnull().sum()


# monthlysales.type()

# In[6]:


monthlysales.info()


# In[7]:


#changing types order Id needs to be interger, Quantity needs to be interger, Price needs to be float, Order Date needs to be time
# first need to remove any object that not intergers taking the columns names out of the dateframe
monthlysales.loc[monthlysales['Quantity Ordered'] == 'Quantity Ordered'].replace('Quantity Ordered','', inplace = True)
monthlysales.loc[monthlysales['Order ID'] == 'Order ID'].replace('Order ID','', inplace = True)
monthlysales.loc[monthlysales['Price Each'] == 'Price Each'].replace('Price Each','', inplace = True)
monthlysales.loc[monthlysales['Product'] == 'Product'].replace('Product','', inplace = True)
monthlysales.loc[monthlysales['Order Date'] == 'Order Date'].replace('Order Date','', inplace = True)
monthlysales.loc[monthlysales['Purchase Address'] == 'Purchase Address'].replace('Purchase Address','', inplace = True)
monthlysales.info()


# In[8]:


monthlysales['Quantity Ordered'] = pd.to_numeric(monthlysales['Quantity Ordered'], errors='coerce')
monthlysales.info()


# In[9]:


monthlysales['Price Each'] = pd.to_numeric(monthlysales['Price Each'], errors='coerce')
monthlysales.info()


# In[11]:


monthlysales['Order Date'] = pd.to_datetime(monthlysales['Order Date'], errors='coerce')
monthlysales.info()


# In[13]:


df = monthlysales
df.head()


# In[14]:


# seperate state in address
df['city'] = df['Purchase Address'].str.split(',', expand=True)[1]
df.head()


# In[15]:


#What was the best Year for sales? How much was earned that Year?
df['Revenues'] = df['Price Each']*df['Quantity Ordered']
df['month'] = df['Order Date'].dt.month
df['time'] = df['Order Date'].dt.time
highest_sales = df.groupby(['month']).sum()
highest_sales


# In[16]:


highest_sales['Revenues'].plot(kind='bar')
plt.show()


# INSIGHTS = Highest Sales are in the Month of December (likely Christmas holiday), following by October (pre holiday advertisment and sales leading to Black Friday to beat the crowd and budgeting) April and May are tax season for refunds

# In[ ]:


#What was the best month for sales? How much was earned that month?


# In[17]:


city_sales = df.groupby(['city'])['Revenues'].sum()
city_sales.plot(kind='bar')
plt.show()


# In[ ]:


#What City had the highest number of sales? San Francisco has the highest Sales 


# In[18]:


df['hour'] = df['Order Date'].dt.hour
df.groupby(['hour'])['Quantity Ordered'].sum().plot(kind='line')
plt.show()


# #What time should we display adverstisement to maximize likelihood of customer's buying product?
# The likelihood that customr's buying product are between 9:30 am to 3:00 pm so advertisment should be displayed between those times

# In[19]:


group_products= df[['Order ID', 'Product']]
group_products = group_products[group_products['Order ID'].duplicated(keep=False)].sort_values(['Product'])
group_products


# In[20]:


products_1= group_products.groupby(['Order ID']).sum()["Product"]
products_1.head(20)


# #What products are most often sold together? The above code shows the product sold together ex. Apple Airpods Headphones Wired Headphones and sold with iPhone

# In[45]:


highest_product=df.groupby(['Product']).sum()['Quantity Ordered'].sort_values(ascending=False)
highest_product.plot(kind='bar')
plt.show()


# 

# 

# In[46]:


#What product sold the most? Why do you think it sold the most? AAA Batteries Sold the most because most all the highest selling product requires AAA Batteries when you look at what are sold the most  


# In[ ]:


#How much probability for next people will ordered USB-C Charging Cable? 


# In[76]:


port_1=df[df['Product']=='USB-C Charging Cable']
port_1.groupby(['Product'])['Quantity Ordered'].value_counts(normalize=True)


# In[ ]:


#How much probability for next people will ordered iPhone?


# In[71]:


port_2=df[df['Product']=='iPhone']
port_2.groupby(['Product'])['Quantity Ordered'].value_counts(normalize=True)


# In[ ]:


#How much probability for next people will ordered Google Phone?


# In[72]:


port_3=df[df['Product']=='Google Phone']
port_3.groupby(['Product'])['Quantity Ordered'].value_counts(normalize=True)


# In[ ]:


#How much probability other peoples will ordered Wired Headphones?


# In[80]:


port_4=df[df['Product']=='Wired Headphones']
port_4.groupby(['Product'])['Quantity Ordered'].value_counts(normalize=True)


# m_sales1 = pd.read_csv('allmonthsales/Sales_January_2019.csv')
# m_sales2 = pd.read_csv('allmonthsales/Sales_February_2019.csv')
# m_sales3 = pd.read_csv('allmonthsales/Sales_March_2019.csv')
# m_sales4 = pd.read_csv('allmonthsales/Sales_April_2019.csv')
# m_sales5 = pd.read_csv('allmonthsales/Sales_May_2019.csv')
# m_sales6 = pd.read_csv('allmonthsales/Sales_June_2019.csv')
# m_sales7 = pd.read_csv('allmonthsales/Sales_July_2019.csv')
# m_sales8 = pd.read_csv('allmonthsales/Sales_August_2019.csv')
# m_sales9 = pd.read_csv('allmonthsales/Sales_September_2019.csv')
# m_sales10 = pd.read_csv('allmonthsales/Sales_October_2019.csv')
# m_sales11 = pd.read_csv('allmonthsales/Sales_November_2019.csv')
# m_sales12 = pd.read_csv('allmonthsales/Sales_December_2019.csv')
# montlysales = pd.concat()
