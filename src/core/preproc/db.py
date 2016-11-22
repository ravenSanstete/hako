# An interface for hako's general usage of the data


# the factual layer that interacts with file system or a database system
# the implementation is totally determined by the user of this framework

from .context import utils


# name as connector, which means that it actually relates the preassumption of the world with the measurements we get
class Connector(object):
    """Reader."""
    def __init__(self):
        super(Reader, self).__init__();
        # a suggested implementation
        self.train_set=None;
        self.test_set=None; 
    # <override> is needed
    # to init the database connector or just load the data into the memory
    def _prepare_dataset(self,path):
        utils.require_override(); 
    # return the batch with label, random or not random
    def feed_train_batch(self,batch_size,in_order=False):
        utils.require_override();
    # always the test batch should be in ordered and a global test ptr may be used
    # devoid the labels that are bound to the test data
    def feed_test_batch(self,batch_size):
        utils.require_override();
    # a protected method, which serves for the upper layer
    # lower layer method 
    # which is suggested to implement, also you may not implement this
    def _random_batch(self,ds,batch_size):
        pass;
    def _ordered_batch(self,ds,batch_size):
        pass;
    # a soft abstract method, you can return the metainfo of the training set, in a form of dictionary
    def metainfo(self):
        pass;
    # which is also a soft abstract method, that implement the evaluation 
    def evaluate(self,prediction):
        pass;
    
        
