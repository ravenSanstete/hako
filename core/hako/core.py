"""
A　program description of the concept of Hako
Functions:
(A) a high-performance buffer when measuring a random batch of monads

hako still seems a swamp. 
How to implement it becomes an important thing for this framework
"""
import utils

# !!! Important class Hako should be recursively defined


class Hako(object):
    """<!!Important base class>
       # please pass in a feeder. The feeder interface will be soon defined 
    """
    def __init__(self, feeder):
        super(Hako, self).__init__();
        self.__feeder__=feeder;
    # which is a user-interface for running the simulation(learning process of the hako)
    # options is a dictionary which comply with the convention in matlab
    def start(self,options):
        self._start(options);
    # <override> needed, internal method
    def _start(self,options):
        utils.require_override();
    
    
        
    
        
        
