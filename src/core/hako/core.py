"""
A　program description of the concept of Hako
Functions:
(A) a high-performance buffer when measuring a random batch of monads

hako still seems a swamp. 
How to implement it becomes an important thing for this framework
"""
import utils
from .monad_table import Monad_T

# !!! Important class Hako should be recursively defined
# later improvements

class Hako(object):
    """<!!Important base class>
       # please pass in a feeder. 
       # prototype dict is as the same length of the concept list of feeder
    """
    def __init__(self, feeder, prototype_dict):
        super(Hako, self).__init__();
        self.__feeder__=feeder; # feeder will actually bring the meta-info about the problem with itself
        self.__monads__=Monad_T();
    # which is a user-interface for running the simulation(learning process of the hako)
    # options is a dictionary which comply with the convention in matlab
    def start(self,options):
        self._start(options);
    # <override> needed, internal method
    # to implement a universal procedure for training
    def _start(self,options):
        utils.require_override();
    # mostly initialize the monad table according to the problem setting
    
    
        
    
        
        
