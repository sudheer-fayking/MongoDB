#!/usr/bin/env python
# coding: utf-8

# Mongo DB

# ## Command prompt work

# * Install Mongodb server and then give the downloaded exe files sharepath inside environment

# * Give mongodb as first command to install all required files

# * Once all required files are installed, give mongo to connect to a port

# In[13]:


# to see all databases in pc, use "show dbs" - it will show all databases which atleast have an empty collection created in it


# In[14]:


# Instead of creating a new database, we can directly give - use database name
# if given database exists, it will use else create new one and then uses it
# use sudheer - # here we are using sudheer database


# In[15]:


# Similarly, we no need to create a new collection and insert data into it, we can directlty insert data giving the command, if same collection exists, it will udpate data else create new collection with that name and update data in that
# db.films.insertOne({"filmname":"Robo","Hero":"Rajinikanth","Heroine":"Aishwarya"}
# Here films is the collection created under sudheer
# we are inserting single documents using insertOne command in dict format


# In[16]:


# db.films.find() - to get all the documents inside the films collections
# db.films.find().pretty() - to get output in organized manner


# In[17]:


# db.films.drop() - To completely drop/delete the collection


# # CRUD Operations

# In[18]:


# 1. Create   - giving data to collections

# insertOne(data,options) - to insert one document into collection

# insertMany(data,options) - to insert many documents into collection


# In[19]:


# 2. Read     - to find if data we need is available in system

# find(filter,options) - we can use only find() to get all documents available in given collection
# if we need particular data, we can give filters inside find function

# findOne(filter,options) - Based on given filters, will show only first document and then closes it.


# In[20]:


# 3. update - we can modify data inside collection using update

# updateOne(data,options) - it will check for filters we give and then check for data to modify and then check for options given and update first data accordingly.

# updateMany(data,options) - it will check for filters we give and then check for data to modify and then check for options given and update all data accordingly.

# replaceOne(data,options)  - previous update options will change only one key value pair or multiple values of key, but replaceOne will completely modify the document in a collection satifisfying filters given


# In[21]:


# 4.Delete

# deleteOne(data,options) - deletes the first document satisfying the given filters

# deleteMany(data,options) - delest all documents satisfying the given filters


# In[22]:


# db.films.insertMany([{"filmname":"2.0","Hero":"Rajinikanth","Heroine":"Amy"},{"filmname":"petta","Hero":"Rajinikanth","Heroine":"Trisha"}])
# Here we are inserting two documents inside films collection


# In[23]:


# db.films.find().pretty()  - to see all documents inside films collection


# # Update 

# In[24]:


#  db.films.updateOne({"filmname":"2.0"},{$set : {"producer":"LYCA"}})    - $set - operator - to use when we need to set

# Here we are updating a document by giving new key value pair of {"producer":"LYCA"} to the first document where filmname:"2.0"


# In[25]:


# db.films.updateMany({},{$set : {"status":true}})  - empty {} filter when all documents need updation

# here we are updating all documents in films collection with new key value pair {"status":true}


# In[ ]:


# if we use $set operator, new key value pair will be added else the value of key will be changed to given one


# In[1]:


# if we want to completely remove all the kv pairs and update with given choice, remove $set operator and use update, it will replace whole document with given values

# instead of removing the $set and use update, we can use replaceone command


# # Delete

# In[26]:


# db.films.deleteOne({"filmname":"2.0"})

# Here we are deleting the document where filmname is 2.0(filter)


# In[27]:


# db.films.deleteMany({"Hero":"Rajinikanth"})

# Here if we want to delete all the data, we check for a common kv pair in all documents and give as a filter


# # Find() 

# In[28]:


# db.films.find({"filmname":"Robo"}).pretty()

# it shows all the documents in films collections where filmname is Robo


# In[29]:


# db.films.find({"Hero":"Rajinikanth"}).pretty()

# it shows all the documents in films collections where hero is Rajinikanth


# In[30]:


# db.films.findOne({"Hero":"Rajinikanth"})

# it shows only first instance where hero is rajinikanth, also pretty wont work in findOne command as it already displays pretty


# In[31]:


# db.films.find({"Budget":{$gt: 200}}).pretty() - $gt is operator where it shows all values greater than given value

# it shows all documents where budget is greater than 200 in films collection


# In[32]:


# For Greater than equal - $gte
# For less than - $lt
# for less than equal to-$lte


# # Projection- get custom fields from documents

# In[2]:


# db.films.find({},{"filmname":1,"Budget":1})

# Here first {} will be filter and second {} will be required fields of documents, if we given required fields as 1, only they will be visible


# In[ ]:


# db.films.find({},{"filmname":1,"Budget":1,"_id":0})

# Here if we want to hide specific fields, we can give them as 0.


# # Embedded documents - Nested documents - upto 100 levels of nesting(16MB/document)

# In[ ]:


# db.films.updateOne({"_id" : ObjectId("6267968e605174fc1082ba78")},{$set:{"technical":{"runtime":100,"visualspec":{"MM":50,"color":"3D"}}}})

# Here inside technical key, value is again a document in dict format and inside value again visual spec is having nested document inside it with mm and color keys


# In[ ]:


# we can include arrays inside a document

# db.films.updateOne({"_id" : ObjectId("6267968e605174fc1082ba77")},{$set:{"genre":["action","Sci-fi","romance"]}})


# # Fetching documents

# In[ ]:


# db.films.findOne({"_id" : ObjectId("6267966d605174fc1082ba76")}).genre

# To get genre from a documents, we should use it with find one


# In[ ]:


# db.films.find({"genre":"Sci-fi"}).pretty()

# to get all the documents where genre is Sci-fi, use with find  ## though genre is given as array, we gave as string, so it checks all documents inside genre and gets if there is any sci-fi


# In[ ]:


# if we want to get data from a nested document\

# db.films.find({"technical.visualspec.color":"RGB"}).pretty() # we should give nested keys as string format to get filters
# here color is nested document inside visual spec which is again nested document inside technical document.


# # Schemas

# # Data Types

# In[3]:


# we can store text(str),Bool(T/F),number{(integer(int32),number long(100203424203423054),number decimal(float))}, Object ID: specific to Mongodb, ISODate - Time and date stamp,Embedded document(nested documents), array(multiple datas/multiple documents) 


# # Relationship between data

# In[4]:


# One to One

# when two datas are related only in single way - person and his age, person and his weight, etc


# In[5]:


# One to Many

# When one data is related to multiple datas - person and his activities, person and his likes, person and his groceries list


# In[6]:


# Many to Many

# When Multiple data is related to Multiple data of a category - Shopping of a store - multiple people purchase multiple items


# In[7]:


# Data should be stored in a proper way based on above relationships


# In[1]:


#Giving One to one data using embedded method(nested)

# db.films.updateOne({"_id" : ObjectId("6267966d605174fc1082ba76")},{$set:{"productionhouse":{"company":"LYCA","type":"PVT"}}})
# here we are updating data as one to one directly using set method


# In[2]:


# Giving one to one data using reference method(object ID)

# db.productionhouse.insertOne({"productionhouse":{"company":"LYCA","type":"PVT"}}) - # creating new collection and inserting nested data to it

# now using the resultant object id as reference, we are giving this data to films collections

# db.films.updateOne({"_id" : ObjectId("6267968e605174fc1082ba78")},{$set:{"productionhouse":ObjectId("626a2ff484a6ad2f071891ed")}})

