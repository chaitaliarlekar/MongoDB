
from pprint import pprint 
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure,OperationFailure
connectionString='mongodb+srv://201701101:201701101@mycluster-yony7.mongodb.net/test?retryWrites=true&w=majority'
#enter your connection String here
client=MongoClient(connectionString)

try:
    client.admin.command('ismaster')

except ConnectionFailure:
    print('Server not available')
    
except OperationFailure:
    print('wrong credentials')
    
else:
    print('connected to database')
    db = client['201701101']
    for docs in db.sales.aggregate([{"$unwind": { "path": "$items" }   },{"$match":{"storeLocation":"Denver"}},{"$group":{"_id": "$storeLocation", "totalSales":{"$sum": {"$multiply":["$items.price","$items.quantity"]}}}}]):
        pprint(docs)
    
finally:
	client.close()

