#!/usr/bin/env python
# coding: utf-8

# ### DATA CLEANNING EXERCISE

# ***

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


run_times = pd.read_excel('Run Times.xlsx')


# In[4]:


run_times


# In[124]:


run_times.dtypes


# In[125]:


run_times.info()


# In[126]:


run_times.head()


# In[127]:


# To convert Fee feild to floating (changing object type to string first to avoide errors)
run_times.Fee = run_times.Fee.astype(str)


# In[7]:


#run_times['Fee'] = run_times['Fee'].astype('str')


# In[11]:


#run_times['Fee'] = pd.to_numeric(run_times['Fee'].str.replace('$', '', regex=True))


# In[128]:


run_times.Fee = pd.to_numeric(run_times.Fee.str.replace('$', '', regex=True))


# In[12]:


run_times.dtypes


# In[130]:


# To change the Warm up time from object data type to numeric 
run_times['Warm Up Time'] = run_times['Warm Up Time'].astype(str)
run_times['Warm Up Time'] = pd.to_numeric(run_times['Warm Up Time'].str.replace('min', '', regex=True))


# In[131]:


run_times.dtypes


# In[132]:


run_times.head(2)


# In[133]:


# To change the Rain data type to integer
run_times.Rain = run_times.Rain .astype('int')


# In[134]:


run_times.head(2)


# ## Missing Data

# In[135]:


pd.read_excel('../Projects/Maven_Data/Data/Student Grades.xlsx')


# In[136]:


df = pd.read_excel('../Projects/Maven_Data/Data/Student Grades.xlsx')


# In[137]:


# To check if there any null values
df.isna().sum()


# In[138]:


# To see in detail
df.isna().any(axis=1)


# In[139]:


#change the formula to 
# To see in detail
df[df.isna().any(axis=1)]


# In[140]:


df.info()


# In[141]:


df.count()


# In[142]:


import numpy as np # ways to recognize missing(null) values


# In[143]:


np.NaN


# In[144]:


None


# In[145]:


# To check the unique values
df.Year.value_counts()


# In[146]:


# to check the if there any null values within the column
df.Year.value_counts(dropna=False)


# In[147]:


# This formula removes if there any NaN values available in the column#it has droped everything because columns has at least 
#one missing value so I'm not going to save any changes to the dataframe here
df[df.isna().any(axis=1)].dropna()


# In[148]:


# I'm going to drop the null values in student column and the class column
df[df.isna().any(axis=1)].dropna(subset=['Student', 'Class'])


# In[149]:


# To drop those Nan values from the entire data frame
df.dropna(subset=['Student', 'Class'])


# In[150]:


# This is what I got in the original dataset
df.shape


# In[151]:


# To Add the values without the nulls I use inpalce=True
df.dropna(subset=['Student', 'Class'], inplace=True)


# In[152]:


df.shape # Now It's been applied


# ## Imputing Missing Data

# In[153]:


# To chaeck the missing Grades
df[df.Grade.isna()]


# In[154]:


df[df.Year.isna()]


# In[155]:


# To Fill the  NaN Values using mean
df.Grade.mean()


# In[156]:


# Filling the NaN values
df.Grade.fillna(df.Grade.mean())


# In[157]:


# To apply changes 
df.Grade.fillna(df.Grade.mean(), inplace=True)


# In[158]:


df.Grade


# In[159]:


# To chaeck if there any missing values in the data
df[df.isna().any(axis=1)]


# In[160]:


# I can see in year feild, I've nulls so need to further look at that class a bit
df[df.Class == 'Freshman Seminar']


# In[161]:


# To update it I use 
df.loc[7, 'Year'] = 'Freshman'


# In[162]:


df[df.Class == 'Freshman Seminar']


# In[163]:


# Instead of doint it one by one I use
import numpy as np
df.Year = np.where(df.Year.isna(), 'Freshman', df.Year)


# In[164]:


df[df.Class == 'Freshman Seminar']


# ## Inconsistant Text & Typos

# In[165]:


df.head()


# In[166]:


df.Class.value_counts(dropna=False)


# In[167]:


# I can see through the above details EDA and Exploratory Data Analysis, and also Intro to python and python
#Their likely the same clasess
df[df.Class.isin(['Exploratory Data Analysis', 'EDA'])]


# In[168]:


df[df.Class.isin(['Intro to Python', 'Python'])]


# In[169]:


# I can see that thosee are the same. I'm goinng to join
np.where(df.Class == 'EDA', 'Exploratory Data Analysis', df.Class)


# In[170]:


df.Class = np.where(df.Class == 'EDA', 'Exploratory Data Analysis', df.Class)


# In[171]:


df.Class.value_counts()


# In[172]:


df.Class = np.where(df.Class == 'Python', 'Intro to Python', df.Class)


# In[173]:


df.Class.value_counts()


# In[174]:


df.describe()


# In[175]:


# I can see that the max grade is really high neet to further investigate
df[df.Grade > 100]


# In[176]:


# requirement is those who have > 100 turn into 100 so
df.Grade = np.where(df.Grade > 100, 100, df.Grade)


# In[177]:


df.Grade.value_counts()


# In[178]:


df.describe()


# ### Mapping Values

# In[179]:


df1 = pd.read_excel('../Projects/Maven_Data/Data/Student Grades.xlsx')


# In[180]:


df1.info()


# In[181]:


df1.head()


# In[182]:


df1.Class.value_counts()


# In[183]:


# Mapping EDA to Exploratory Data Analysis and python to Intro to Python
Class_mappings = {'Intro to Python': 'Intro to Python',
                 'Intro to SQL': 'Intro to SQL',
                 'EDA' : 'Exploratory Data Analysis',
                 'Exploratory Data Analysis' : 'Exploratory Data Analysis',
                 'python' : 'Intro to Python',
                 'Freshman Seminar' : 'Frshman Seminar'}


# In[184]:


df1.Class = df.Class.map(Class_mappings)


# In[185]:


df1.Class.value_counts()


# ## Handlling Inconsistancies in Data

# In[186]:


# To check the location in detail
run_times.Location


# In[187]:


run_times.Location = run_times.Location.str.lower().str.replace('the', '').str.strip('“”')


# In[188]:


run_times


# ***

# ### Handlling Duplicate Data

# In[189]:


df[df.duplicated(keep=False)] # This will gives the duplicated rows


# In[190]:


# To remove all the dulpicates
df.drop_duplicates(inplace=True)


# In[191]:


df[df.duplicated(keep=False)]


# In[192]:


# To check the records in between 40-45
df.iloc[40:45, :] 


# In[193]:


df.reset_index(drop=True)


# In[194]:


df.reset_index(drop=True, inplace=True)


# In[195]:


df.iloc[40:45, :]
# now I have the correct order


# ### Outlier Detection

# In[196]:


import seaborn as sns


# In[197]:


df.hist()


# In[198]:


# remove the wordingd below the command type ;
df.hist();


# In[199]:



# to make this histogram more fine tune or less we use to select the bins
# i wanna see 1 bar for each grade
# to deside the bins  i'll take the differenece between  max range and the min
df.Grade.max() - df.Grade.min()


# In[200]:


df.hist(bins=55);


# In[201]:


# to get the rough view of histogram
df.hist(bins=3);


# In[202]:


sns.histplot(df);


# In[203]:


sns.histplot(df, binwidth=1);


# In[204]:


sns.boxplot(x=df.Grade);


# #### Above 3 dots are my outliers

# In[205]:


import numpy as np


# In[206]:


Q25, Q50, Q75 = np.percentile(df.Grade, (25, 50, 75))


# In[207]:


#To get the min and max lines
iqr = Q75 - Q25


# In[208]:


min_grade = Q25 - 1.5*iqr
max_grade = Q75 + 1.5*iqr 


# In[209]:


min_grade, Q25, Q50, Q75, max_grade


# In[210]:


# To check the outliers of the dataset
df[df.Grade < 69]


# In[211]:


mean = np.mean(df.Grade)


# In[212]:


sd = np.std(df.Grade)


# In[213]:


mean, sd


# #### My grades are + or - 8 to 84 : I'll check the grades from 3 standard deviation away from the mean

# In[214]:


# Return me the grades when i'm going through the grades within the Grade column if so treturn those if grades < mean -3 *sd
# or if the grade is > mean + 3sd
[grade for grade in df.Grade if (grade < mean - 3*sd) or (grade > mean + 3*sd)]


# In[215]:


# It gives me that outliers are 50 and 45 but if I change the outlier to 2std
[grade for grade in df.Grade if (grade < mean - 2*sd) or (grade > mean +2*sd)]


# In[216]:


# Sorting Data
df.Grade.sort_values()


# In[217]:


# Sorting data in Decending Order
df.Grade.sort_values(ascending=False)


# In[218]:


df.head()


# In[219]:


df.shape


# #### We have 79 Rows and 4 Columns

# In[220]:


# We were to remove the grades < 60
df[df.Grade < 60]


# In[221]:


# impiting Data
min_grade = df[df.Grade >=60]. Grade.min()
min_grade


# In[222]:


df.Grade = np.where(df.Grade < 60, min_grade, df.Grade)


# In[223]:


df[df.Grade == 64]


# In[224]:


# I'm changing Johns marks to 74
df.loc[36, 'Grade'] = 74


# In[225]:


df[df.Student == 'John']


# ### Missing Values

# In[226]:


df[df.isna(). any(axis=1)]


# * I do not have any missing values

# ### Inconsistant text anf Typos

# In[227]:


df.Class.value_counts()


# * I do not have any Inconsistant text or Typos

# ### Duplicate Data

# In[228]:


df[df.duplicated()]


# * I do nt have any Duplicates Values

# ### Outliers

# In[229]:


sns.histplot(df);


# * I do not have any outliers in the data

# ## Creating New Columns 

# In[231]:


import pandas as pd


# In[232]:


groceries = pd.read_excel('Groceries.xlsx')


# In[233]:


groceries.head()


# In[334]:


groceries.isna().sum()


# In[336]:


groceries.shape


# In[337]:


groceries.dtypes


# In[234]:


round(groceries.Price_Dollars *1.05, 2)


# In[235]:


# I need to save it for a new column
groceries['New Column'] = round(groceries.Price_Dollars *1.05, 2)


# In[238]:


groceries.head(2)


# In[241]:


# To find out the percentage of Inventory
groceries['Total Inventory'] = groceries.Inventory.sum()


# In[242]:


groceries.head(3)


# In[243]:


# To find out the percentage of Inventory
groceries['Precent Inventory'] = round(groceries['Inventory'] / groceries['Total Inventory'] *100, 2)


# In[244]:


groceries.head(3)


# In[245]:


#Let's again look at our inventory column and let's say if there's 
#any item that has an inventory of under 50, then I want to 
#flag that as low inventory.So what I can do is first importing numpy 
#as NP and then I'm going to do NP dot where and in the cases
#where the inventory is less than 50, then set it equal to low inventory.
import numpy as np
groceries['Low Inventory'] = np.where(groceries.Inventory < 50, 'Low Inventory', '')


# In[246]:


groceries.head(20)


# * <span style ='color:red'>Extracting Dates</span>.

# In[248]:


groceries['Last_Updated_Time'] = groceries.Last_Updated.dt.time


# In[249]:


groceries.head(3)


# In[251]:


# Extracting day of the week from the schedule shipment feild
groceries['Shipment_Date_DOW'] = groceries.Next_Scheduled_Shipment.dt.dayofweek


# In[254]:


groceries.head(3)


# In[255]:


# to get the day of the week, I use mapping
DOW_mappings = {0 : 'Monday',
                1 : 'Tuesday',
                2 : 'Wednesday',
                3 : 'Thursday',
                4 : 'Friday',
                5 : 'Saturday',
                6 : 'Sunday'}


# In[259]:


groceries['Shipment_Date_DOW'].map(DOW_mappings)


# In[262]:


groceries['Shipment_Date_DOW'] = groceries['Shipment_Date_DOW'].map(DOW_mappings)


# In[263]:


groceries.head(2)


# In[266]:


# I want to add 1 day to all those next scheduled shipment
#goceries.Next_Sceduled_Shipment +1 # I can not add 1 straight away becase its 
# data type is datetime 
groceries.Next_Scheduled_Shipment + pd.to_timedelta(1,'D')


# In[268]:


groceries['Next_Scheduled_Date'] = groceries.Next_Scheduled_Shipment + pd.to_timedelta(1, 'D')


# In[269]:


groceries.head(3)


# In[273]:


# Lets say i only wanted to add a additional date only for the fruit items
groceries['New_Shipment_Date'] = np.where(groceries.Category == 'Produce: Fruit',
                                         groceries.Next_Scheduled_Shipment + pd.to_timedelta(1, 'D'),
                                         groceries.Next_Scheduled_Date)
                                         


# In[274]:


groceries.head(25)


# ### Using Text Data to Create New Columns

# In[276]:


groceries.dtypes


# In[277]:


groceries.head(3)


# * <span style ='color:red'>Removing Charactors</span>.

# In[286]:


# inorder to turn product ID into numeric column we remove the letter
# infront of the ID
groceries['Product_ID_Num'] = groceries.Product_ID.str[1:]


# In[287]:


groceries.dtypes


# In[285]:


groceries.head(2)


# In[299]:


# To change the data type
groceries['Product_ID_Num']. astype('int')


# In[300]:


# To save the changes
groceries['Product_ID_Num'] = groceries['Product_ID_Num']. astype('int')


# In[301]:


groceries.dtypes


# * <span style = 'color : red'>Split into columns</span>

# In[303]:


# going to split the Category column into 2 columns
groceries.Category.value_counts()


# In[304]:


# I need product in one column and items are in anotheter column
groceries.Category.str.split(':').to_list()


# In[306]:


pd.DataFrame(groceries.Category.str.split(':').to_list())


# In[307]:


# To name the above feilds
groceries[['Category', 'Sub_Category']] = pd.DataFrame(groceries.Category.str.split(':').to_list())


# In[323]:


groceries.head(3)


# In[310]:


# To check the items contain organic product
groceries.Item.str.contains('Organic')


# In[311]:


# to save it into a new colum
groceries['Organic'] = groceries.Item.str.contains('Organic')


# In[326]:


groceries


# In[329]:


# To reorganize the column
groceries[['Product_ID', 'Product_ID_Num', 'Category', 'Sub_Category',
          'Item', 'Organic', 'Price_Dollars', 'Inventory', 'Precent Inventory',
          'Low Inventory', 'Last_Updated', 'Last_Updated_Time',
          'New_Shipment_Date', 'Shipment_Date_DOW']]


# In[330]:


# To save the data
groceries_with_new_column = groceries[['Product_ID', 'Product_ID_Num', 'Category', 'Sub_Category',
          'Item', 'Organic', 'Price_Dollars', 'Inventory', 'Precent Inventory',
          'Low Inventory', 'Last_Updated', 'Last_Updated_Time',
          'New_Shipment_Date', 'Shipment_Date_DOW']]


# In[331]:


groceries_with_new_column


# In[332]:


groceries_with_new_column.shape


# In[325]:


groceries.shape


# * <span style = 'color:red'>Creating a new notebook with a new column</span>.

# In[318]:


# To open up with a new notebook to work with Exploratory data analysis
groceries_with_new_column.to_pickle('groceries_with_new_column.pkl')
# the note bookcan be found in the same working folder and when you wanted to use it open up a new python workbook then use the 
#following code
#import pandas as pd
#pd.read_pickle('groceries_with_new_columns.pkl')


# In[333]:


# If I need the clean dats to export into csv
groceries_with_new_column.to_csv('groceries_with_new_column.csv')

