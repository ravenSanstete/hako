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
    # db is the same length as the relations also in a corresponding order
    def __init__(self, concepts, relations, dbs):
        super(Feeder, self).__init__();
        # hako should use these information to generate the simulatioin procedure automaticall
        self.concepts=concepts;
        self.relations=relations;
        # db should be then constructed will be classes corresponding to the interface of database reader
    # a function that return a dictionary
    def feed(self):
        return self._feed();
    # <override> needed, internal method
    def _feed(self):
        utils.require_override();
        
        
        
