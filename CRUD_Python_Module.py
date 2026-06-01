from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self,username,password):
        self.username=username
        self.password=password
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        # USER = 'aacuser' 
        # PASS = 'aacuser_pswd' 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'acc' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (self.username,self.password,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
    
    def read(self,query:dict):
        if isinstance(query,dict):
            return list(self.collection.find(query))
        else:
            return []
    
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data:dict):
        if data is not None and isinstance(data,dict): 
            result=self.database.animals.insert_one(data)  # data should be dictionary       
            return result.acknowledged
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 
    def update(self,query:dict,update_data:dict):
        if isinstance(query,dict) and isinstance(update_data,dict):
            if not any(key.startswith('$') for key in update_data): # incase operator is not provided
                update_data = {"$set": update_data}
            result =self.collection.update_many(query,update_data)
            return result.modified_count
        return 0
                
                
    def delete(self,query:dict):
        if isinstance(query,dict):
            result=self.collection.delete_many(query)
            return result.deleted_count
        return 0