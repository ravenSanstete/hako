"""
feeder still seems a perfect name for the preprocessing class

you should always inherit it and pass it to the hako whenever possible

We prefer you to draw data from a local database

Observations refer to the partial observed data.
Two types are common.
One, Image of Measurement. Fit it with what you assume the measurements should be
Two, Image of partial observed tangle information. Fit it with what you assume the tangle should be

"""

from .context import utils


class Feeder(object):
    """docstring for Feeder. """
    # you need to show me the relationship of each concept in the problem
    # relations should be a list of tuples of names
    # names should come from vocabulary 
    # dbs is a list of db(which is an abstract layer[interface] of dataset file)
    def __init__(self, vocabulary, relations, dbs):
        super(Feeder, self).__init__()    
    # a function that return a dictionary
    def feed(self):
        return self._feed();
    # <override> needed, internal method
    def _feed(self):
        utils.require_override();s
        
        
        
