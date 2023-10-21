from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'SNHU1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30238
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER, PASS, HOST, PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        print ("Connection Successful")

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    # Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            readData = list(self.database.animals.find(data))  # data should be dictionary
            return readData
        else:
            raise Exception("Nothing to find, because data parameter is empty")
    
    # Create method to implement the U in CRUD.
    def update(self, queryData, updateData):
        if queryData and updateData is not None:
            updateData = self.database.animals.update_many(queryData, {"$set": updateData})  # data should be dictionary
            return updateData.modified_count
        else:
            raise Exception("Nothing to find, because data parameter is empty")
    
     # Create method to implement the D in CRUD.
    def delete(self, data):
        if data is not None:
            deleteData = self.database.animals.delete_many(data)  # data should be dictionary
            return deleteData.deleted_count
        else:
            raise Exception("Nothing to find, because data parameter is empty")       
            
            
            
            
            
            
            
