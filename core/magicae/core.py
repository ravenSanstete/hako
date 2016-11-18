"""
Implementation of an auxiliary class that as an intermediate layer of Monad and Prototype
A Function Class
"""

import functools as F

from __init__ import utils
from __init__ import proto
# a magica determines (A) the way to distribute the difference to each prototype
#                     (B) the way to measure over the prototypes
# By generating functions when invoking the mix functional
# In such a way, magica more like a static class

# constaints should not be contained in this file
# never try to modify the prototype information even it seems necessary
class Magica(object):
    """docstring for Magica"""
    def __init__(self):
        super(Magica,self).__init__()
    # return generated measure method, generated propagate method, individual variables
    def mix(self, prototypes):
        utils.check_types(prototypes,proto.Prototype);
        return F.partial(measure, self, prototypes), F.partial(propagate, self, prototypes), self._allocate(prototypes);
    # you may able to set different sample options for each prototype
    # options should be a list the same length with prototypes, otherwise, the last several will be considered as None
    def measure(self, prototypes, options):
        assert(len(options)<=len(prototypes)); # the less part
        # padding the options list
        while(len(prototypes)!=len(options)): options.append(None);
        self._measure([prototypes[i].measure(options[i]) for i in range(len(options))]);
    def propagate(self, prototypes, diff, parameters):
        sub_diff_list=self._distribute(prototypes, diff, parameters);
        F.map(lambda i:prototypes[i].propagate(sub_diff_list[i]),range(len(sub_diff_list)));
    #
    # <override> is needed. As a measurements
    def _measure(self, sub_measurements, parameters):
        utils.require_override();
    # <override> is needed. return a list of the distributed difference list
    # prototypes passed for reference
    # diff may be a batch, thus the sublist should be a matrix maybe, along axis-0 do the arrangement
    # parameters may be a batch as well, which should correspond to each diff
    def _distribute(self, prototypes, diff, parameters):
        utils.require_override();
    # <override> is needed. return parameters of the instance of this kind of magica for a certain monad
    # a dictionary with name is needed
    def _allocate(self,prototypes):
        utils.require_override();
        
