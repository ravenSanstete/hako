import pymongo
from ..context import preproc



# the predetermined collection names are 'ml_100k_train' 'ml_100k_test'



# which implements the Connector interface thru a mongo db system 
# this can be considered as a module on how you implement them

# will the connector based on mongodb be a common structure?
class MLConnector(preproc.Connector):
    """implementation of MLConnector."""
    def __init__(self,ip,port,version): # you can use 100k 
        super(MLConnector, self).__init__();
        self.client=pymongo.MongoClient(ip,port);
        self.train_set=self.prepare_dataset('ml_%s_train' % (version));
        self.test_set=self.prepare_dataset('ml_%s_test' % (version));  
        self.__train_cursor__=0; # which is used for fetching training data in order
        self.__test_cursor__=0; # which is used for fetching testing data in order
    # to init the database connector
    def prepare_dataset(self,path):
        return self.client[path];
    # return the batch with label, random or not random
    def feed_train_batch(self,batch_size,in_order=False):
        return _random_batch(self,self.train_set,batch_size);
    # always the test batch should be in ordered and a global test ptr may be used
    # devoid the labels that are bound to the test data
    def feed_test_batch(self,batch_size):
        pass;
    # a protected method, which serves for the upper layer
    # lower layer method 
    # which is suggested to implement, also you may not implement this
    def _random_batch(self,ds,batch_size):
        return list(ds.aggregate({"$sample": {"size": batch_size}}));
    def _ordered_batch(self,ds,batch_size):
        pass;
    # a soft abstract method, you can return the metainfo of the training set, in a form of dictionary
    def metainfo(self):
        pass;
    # which is also a soft abstract method, that implement the evaluation 
    def evaluate(self,prediction):
        pass;
     
